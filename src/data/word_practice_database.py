import json
import os
from datetime import datetime
from typing import Dict, List, Any
import random

class WordPracticeDatabase:
    """Database for tracking word practice statistics and performance"""
    
    def __init__(self, db_file: str = None):
        if db_file is None:
            # Default to data directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            db_file = os.path.join(current_dir, 'word_practice_data.json')
        
        self.db_file = db_file
        self.data = self._load_data()
    
    def _load_data(self) -> Dict:
        """Load data from JSON file or create new structure"""
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Migrate old data to new format
                    self._migrate_data(data)
                    return data
            except json.JSONDecodeError:
                print(f"⚠️  Warning: Could not read {self.db_file}, creating new database")
                return self._create_empty_db()
        else:
            return self._create_empty_db()
    
    def _migrate_data(self, data: Dict):
        """Migrate old data format to include new fields"""
        for word_key, word_data in data.get('words', {}).items():
            # Add missing fields for new mastery calculation
            if 'mastery_level' not in word_data:
                word_data['mastery_level'] = 0
            if 'last_practiced' not in word_data:
                word_data['last_practiced'] = None
            if 'streak' not in word_data:
                word_data['streak'] = 0
            if 'attempts_history' not in word_data:
                word_data['attempts_history'] = []
            if 'first_seen' not in word_data:
                # Use last_practiced as fallback, or current time if not available
                word_data['first_seen'] = word_data.get('last_practiced', datetime.now().isoformat())
            
            # Ensure 'russian' field exists (for backward compatibility)
            if 'russian' not in word_data:
                word_data['russian'] = word_key

    def _create_empty_db(self) -> Dict:
        """Create empty database structure"""
        return {
            'words': {},  # word -> {attempts, correct, incorrect, streak, last_practiced, mastery_level}
            'sessions': []  # list of session records
        }
    
    def _save_data(self):
        """Save data to JSON file"""
        os.makedirs(os.path.dirname(self.db_file), exist_ok=True)
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def _calculate_mastery_level(self, stats: Dict) -> int:
        """
        Calculate mastery level (0-5) using multiple factors
        
        Mastery Criteria:
        Level 0: Never practiced or <20% accuracy
        Level 1: 20-40% accuracy, inconsistent
        Level 2: 40-60% accuracy, needs more practice
        Level 3: 60-80% accuracy, showing progress
        Level 4: 80-90% accuracy, nearly mastered
        Level 5: 90%+ accuracy with retention over time
        """
        from datetime import datetime, timedelta
        
        total_attempts = stats.get('total_attempts', 0)
        correct = stats.get('correct', 0)
        streak = stats.get('streak', 0)
        last_practiced = stats.get('last_practiced')
        
        # Level 0: No practice yet
        if total_attempts == 0:
            return 0
        
        # Calculate base accuracy
        accuracy = (correct / total_attempts) * 100
        
        # Factor 1: Base accuracy score (0-5 points)
        if accuracy >= 90:
            accuracy_points = 5.0
        elif accuracy >= 80:
            accuracy_points = 4.0
        elif accuracy >= 70:
            accuracy_points = 3.5
        elif accuracy >= 60:
            accuracy_points = 3.0
        elif accuracy >= 50:
            accuracy_points = 2.5
        elif accuracy >= 40:
            accuracy_points = 2.0
        elif accuracy >= 30:
            accuracy_points = 1.5
        elif accuracy >= 20:
            accuracy_points = 1.0
        else:
            accuracy_points = 0.5
        
        # Factor 2: Consistency bonus (streak modifier: -1.0 to +1.0)
        if streak >= 5:
            consistency_bonus = 1.0  # Very consistent
        elif streak >= 3:
            consistency_bonus = 0.5  # Good consistency
        elif streak >= 1:
            consistency_bonus = 0.2  # Some consistency
        elif streak == 0:
            consistency_bonus = 0.0  # Neutral
        elif streak >= -2:
            consistency_bonus = -0.3  # Recent mistakes
        elif streak >= -4:
            consistency_bonus = -0.6  # Struggling
        else:
            consistency_bonus = -1.0  # Very inconsistent
        
        # Factor 3: Experience modifier (need minimum attempts)
        # Fewer attempts = less confident in mastery
        if total_attempts >= 10:
            experience_modifier = 1.0  # Full confidence
        elif total_attempts >= 5:
            experience_modifier = 0.8  # Good sample size
        elif total_attempts >= 3:
            experience_modifier = 0.6  # Moderate confidence
        else:
            experience_modifier = 0.4  # Low confidence
        
        # Factor 4: Recency penalty (time decay)
        recency_modifier = 1.0
        if last_practiced:
            try:
                last_date = datetime.fromisoformat(last_practiced)
                days_since = (datetime.now() - last_date).days
                
                # Apply decay based on how long ago
                if days_since <= 1:
                    recency_modifier = 1.0  # Very recent
                elif days_since <= 3:
                    recency_modifier = 0.95  # Recent
                elif days_since <= 7:
                    recency_modifier = 0.9  # Within a week
                elif days_since <= 14:
                    recency_modifier = 0.8  # Two weeks
                elif days_since <= 30:
                    recency_modifier = 0.7  # A month
                else:
                    recency_modifier = 0.6  # Very old, might be forgotten
            except (ValueError, TypeError):
                recency_modifier = 0.8  # Unknown date, slight penalty
        
        # Calculate final mastery score
        mastery_score = (accuracy_points + consistency_bonus) * experience_modifier * recency_modifier
        
        # Convert to 0-5 level (with strict requirements for level 5)
        if mastery_score >= 5.5 and accuracy >= 90 and total_attempts >= 5:
            return 5  # True mastery: high accuracy, consistent, experienced
        elif mastery_score >= 4.5:
            return 4  # Nearly mastered
        elif mastery_score >= 3.5:
            return 3  # Good progress
        elif mastery_score >= 2.5:
            return 2  # Learning
        elif mastery_score >= 1.5:
            return 1  # Beginner
        else:
            return 0  # Struggling or no practice

    def record_attempt(self, russian: str, translation: str, user_answer: str, is_correct: bool):
        """Record a practice attempt and update statistics"""
        from datetime import datetime
        
        # Initialize word if not exists
        if russian not in self.data['words']:
            self.data['words'][russian] = {
                'russian': russian,
                'english': translation,  # Keep 'english' for backward compatibility
                'translation': translation,  # Also store as 'translation'
                'total_attempts': 0,
                'correct': 0,
                'incorrect': 0,
                'streak': 0,
                'mastery_level': 0,
                'first_seen': datetime.now().isoformat(),
                'last_practiced': datetime.now().isoformat(),
                'attempts_history': []
            }
        
        word_data = self.data['words'][russian]
        
        # Ensure all required fields exist (for backward compatibility)
        if 'attempts_history' not in word_data:
            word_data['attempts_history'] = []
        if 'first_seen' not in word_data:
            word_data['first_seen'] = word_data.get('last_practiced', datetime.now().isoformat())
        if 'russian' not in word_data:
            word_data['russian'] = russian
        
        # Update counts
        word_data['total_attempts'] += 1
        if is_correct:
            word_data['correct'] += 1
            word_data['streak'] = max(0, word_data['streak']) + 1
        else:
            word_data['incorrect'] += 1
            word_data['streak'] = min(0, word_data['streak']) - 1
        
        # Update timestamps
        word_data['last_practiced'] = datetime.now().isoformat()
        
        # Store attempt in history (keep last 20 attempts)
        word_data['attempts_history'].append({
            'date': datetime.now().isoformat(),
            'correct': is_correct,
            'user_answer': user_answer
        })
        if len(word_data['attempts_history']) > 20:
            word_data['attempts_history'] = word_data['attempts_history'][-20:]
        
        # Recalculate mastery level using new algorithm
        word_data['mastery_level'] = self._calculate_mastery_level(word_data)
        
        # Save to file
        self._save_data()

    def get_statistics(self) -> Dict:
        """Get comprehensive practice statistics"""
        total_words = len(self.data['words'])
        total_attempts = sum(w['total_attempts'] for w in self.data['words'].values())
        total_correct = sum(w['correct'] for w in self.data['words'].values())
        total_incorrect = sum(w['incorrect'] for w in self.data['words'].values())
        
        # Count mastered words (level 4-5 with high accuracy)
        mastered_words = sum(
            1 for w in self.data['words'].values()
            if w['mastery_level'] >= 4 and 
            (w['correct'] / w['total_attempts'] * 100 >= 80 if w['total_attempts'] > 0 else False)
        )
        
        # Count words needing review (level 0-2 or accuracy < 60%)
        needs_review = sum(
            1 for w in self.data['words'].values()
            if w['mastery_level'] <= 2 or
            (w['correct'] / w['total_attempts'] * 100 < 60 if w['total_attempts'] > 0 else True)
        )
        
        # Calculate overall accuracy
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        
        return {
            'total_words_practiced': total_words,
            'total_attempts': total_attempts,
            'total_correct': total_correct,
            'total_incorrect': total_incorrect,
            'accuracy': accuracy,
            'mastered_words': mastered_words,
            'needs_review': needs_review,
            'total_sessions': len(self.data['sessions'])
        }
    
    def get_word_stats(self, russian_word: str) -> Dict:
        """Get statistics for a specific word"""
        if russian_word not in self.data['words']:
            return {
                'total_attempts': 0,
                'correct': 0,
                'incorrect': 0,
                'streak': 0,
                'last_practiced': None,
                'mastery_level': 0
            }
        
        # Ensure all required fields exist
        word_data = self.data['words'][russian_word]
        return {
            'total_attempts': word_data.get('total_attempts', 0),
            'correct': word_data.get('correct', 0),
            'incorrect': word_data.get('incorrect', 0),
            'streak': word_data.get('streak', 0),
            'last_practiced': word_data.get('last_practiced'),
            'mastery_level': word_data.get('mastery_level', 0)
        }
    
    def _calculate_word_priority(self, word_stats: Dict) -> float:
        """
        Calculate priority score for a word (higher = more important to practice)
        
        Priority factors:
        - Never seen: highest priority
        - Recent mistakes: very high priority
        - Low accuracy: high priority
        - Low mastery level: high priority
        - Spaced repetition timing: practice at optimal intervals
        - High mastery: low priority (but still review occasionally)
        """
        if word_stats['total_attempts'] == 0:
            return 100  # Never seen - highest priority
        
        priority = 50  # Base priority
        
        # Accuracy factor (0-100%)
        accuracy = word_stats['correct'] / word_stats['total_attempts']
        if accuracy < 0.5:
            priority += 40  # Very low accuracy
        elif accuracy < 0.7:
            priority += 25  # Low accuracy
        elif accuracy < 0.85:
            priority += 10  # Medium accuracy
        else:
            priority -= 15  # High accuracy
        
        # Mastery level factor (0-5)
        mastery = word_stats['mastery_level']
        priority += (5 - mastery) * 8  # Lower mastery = higher priority
        
        # Recent mistakes factor
        if word_stats['streak'] == 0 and word_stats['total_attempts'] > 0:
            priority += 30  # Just made a mistake
        
        # Spaced repetition: time since last practice based on mastery level
        if word_stats['last_practiced']:
            last_practice = datetime.fromisoformat(word_stats['last_practiced'])
            hours_ago = (datetime.now() - last_practice).total_seconds() / 3600
            
            # Optimal review intervals based on mastery level (in hours)
            # Lower mastery = shorter intervals
            optimal_intervals = {
                0: 4,      # Review after 4 hours
                1: 12,     # Review after 12 hours
                2: 24,     # Review after 1 day
                3: 72,     # Review after 3 days
                4: 168,    # Review after 1 week
                5: 336     # Review after 2 weeks
            }
            
            optimal = optimal_intervals.get(mastery, 24)
            
            # Calculate how overdue this word is
            if hours_ago >= optimal * 1.2:  # 20% past optimal time
                priority += 25
            elif hours_ago >= optimal:
                priority += 15
            elif hours_ago >= optimal * 0.8:  # Within 80% of optimal
                priority += 5
            elif hours_ago < optimal * 0.3:  # Too recent
                priority -= 30
        
        return max(0, priority)
    
    def get_words_for_practice(self, available_words: List[Dict], num_words: int = 30) -> List[Dict]:
        """
        Select words for practice session using intelligent priority-based algorithm:
        - ~50% new words
        - ~50% review (mistakes, low mastery, spaced repetition)
        """
        # Calculate priority for each word
        word_priorities = []
        for word in available_words:
            russian = word['russian']
            stats = self.get_word_stats(russian)
            priority = self._calculate_word_priority(stats)
            word_priorities.append({
                'word': word,
                'priority': priority,
                'stats': stats
            })
        
        # Sort by priority (highest first)
        word_priorities.sort(key=lambda x: x['priority'], reverse=True)
        
        # Categorize words
        never_seen = [wp for wp in word_priorities if wp['stats']['total_attempts'] == 0]
        
        # Review words: mistakes, low mastery, or due for spaced repetition
        review = [wp for wp in word_priorities if wp['stats']['total_attempts'] > 0]
        
        # Calculate targets: 50% new, 50% review
        target_new = int(num_words * 0.5)
        target_review = num_words - target_new
        
        practice_list = []
        
        # Add new words (up to 50%)
        new_to_add = min(len(never_seen), target_new)
        practice_list.extend([wp['word'] for wp in never_seen[:new_to_add]])
        
        # Add review words (mistakes, low mastery, spaced repetition)
        review_to_add = min(len(review), target_review)
        practice_list.extend([wp['word'] for wp in review[:review_to_add]])
        
        # Fill any remaining slots with highest priority words
        remaining = num_words - len(practice_list)
        if remaining > 0:
            remaining_pool = never_seen[new_to_add:] + review[review_to_add:]
            remaining_pool.sort(key=lambda x: x['priority'], reverse=True)
            practice_list.extend([wp['word'] for wp in remaining_pool[:remaining]])
        
        # Final shuffle to mix new and review words
        random.shuffle(practice_list)
        
        return practice_list[:num_words]
    
    def start_session(self) -> int:
        """Start a new practice session and return session ID"""
        session_id = len(self.data['sessions'])
        session = {
            'id': session_id,
            'start_time': datetime.now().isoformat(),
            'end_time': None,
            'words_practiced': [],
            'correct_count': 0,
            'incorrect_count': 0
        }
        self.data['sessions'].append(session)
        self._save_data()
        return session_id
    
    def add_word_to_session(self, session_id: int, russian_word: str):
        """Add a word to the current session's word list"""
        if session_id < len(self.data['sessions']):
            session = self.data['sessions'][session_id]
            if russian_word not in session['words_practiced']:
                session['words_practiced'].append(russian_word)
            self._save_data()
    
    def end_session(self, session_id: int, correct_count: int, incorrect_count: int):
        """End a practice session with final counts"""
        if session_id < len(self.data['sessions']):
            self.data['sessions'][session_id]['end_time'] = datetime.now().isoformat()
            self.data['sessions'][session_id]['correct_count'] = correct_count
            self.data['sessions'][session_id]['incorrect_count'] = incorrect_count
            self._save_data()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get overall practice statistics"""
        # Only count words that have actually been practiced (attempts > 0)
        practiced_words = {k: v for k, v in self.data['words'].items() if v.get('total_attempts', 0) > 0}
        
        total_words_practiced = len(practiced_words)
        total_attempts = sum(word['total_attempts'] for word in practiced_words.values())
        total_correct = sum(word['correct'] for word in practiced_words.values())
        total_incorrect = sum(word['incorrect'] for word in practiced_words.values())
        
        # Count mastered words (mastery level 4-5 AND accuracy > 80%)
        mastered_words = sum(
            1 for word in practiced_words.values() 
            if word.get('mastery_level', 0) >= 4 and 
            (word['correct'] / word['total_attempts']) > 0.8
        )
        
        # Words needing review (accuracy < 70% or mastery < 2)
        needs_review = sum(
            1 for word in practiced_words.values()
            if (word['correct'] / word['total_attempts']) < 0.7 or
            word.get('mastery_level', 0) < 2
        )
        
        # Calculate overall accuracy
        accuracy = (total_correct / total_attempts * 100) if total_attempts > 0 else 0
        
        return {
            'total_words_practiced': total_words_practiced,
            'total_attempts': total_attempts,
            'total_correct': total_correct,
            'total_incorrect': total_incorrect,
            'accuracy': accuracy,
            'mastered_words': mastered_words,
            'needs_review': needs_review,
            'total_sessions': len(self.data['sessions'])
        }
    
    def get_session_history(self, limit: int = 10) -> List[Dict]:
        """Get recent session history"""
        sessions = sorted(
            self.data['sessions'],
            key=lambda s: s['start_time'],
            reverse=True
        )
        return sessions[:limit]
    
    def reset_statistics(self):
        """Reset all statistics (use with caution!)"""
        # Delete the old file
        if os.path.exists(self.db_file):
            os.remove(self.db_file)
        
        # Create fresh database
        self.data = self._create_empty_db()
        self._save_data()
        print("\n✅ All statistics have been reset successfully!")