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
            if 'mastery_level' not in word_data:
                word_data['mastery_level'] = 0
            if 'last_practiced' not in word_data:
                word_data['last_practiced'] = None
            if 'streak' not in word_data:
                word_data['streak'] = 0
    
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
    
    def record_attempt(self, russian_word: str, english_word: str, user_answer: str, is_correct: bool):
        """Record a practice attempt for a word"""
        if russian_word not in self.data['words']:
            self.data['words'][russian_word] = {
                'english': english_word,
                'total_attempts': 0,
                'correct': 0,
                'incorrect': 0,
                'streak': 0,
                'last_practiced': None,
                'mastery_level': 0  # 0-5 scale
            }
        
        word_data = self.data['words'][russian_word]
        word_data['total_attempts'] += 1
        word_data['last_practiced'] = datetime.now().isoformat()
        
        if is_correct:
            word_data['correct'] += 1
            word_data['streak'] += 1
            # Increase mastery level (max 5)
            if word_data['streak'] >= 5 and word_data['mastery_level'] < 5:
                word_data['mastery_level'] = min(5, word_data['mastery_level'] + 1)
        else:
            word_data['incorrect'] += 1
            word_data['streak'] = 0
            # Decrease mastery level on mistakes
            word_data['mastery_level'] = max(0, word_data['mastery_level'] - 1)
        
        self._save_data()
    
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
        - Not practiced recently: medium priority
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
        
        # Time since last practice
        if word_stats['last_practiced']:
            last_practice = datetime.fromisoformat(word_stats['last_practiced'])
            days_ago = (datetime.now() - last_practice).days
            
            if days_ago > 7:
                priority += 20  # Not practiced in a week
            elif days_ago > 3:
                priority += 10  # Not practiced in 3 days
            elif days_ago < 1:
                priority -= 20  # Practiced very recently
        
        return max(0, priority)
    
    def get_words_for_practice(self, available_words: List[Dict], num_words: int = 30) -> List[Dict]:
        """
        Select words for practice session using intelligent priority-based algorithm:
        - ~33% previous mistakes (low accuracy/mastery)
        - ~33% new words
        - ~33% review words (mixed mastery levels)
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
        mistakes = [wp for wp in word_priorities if wp['stats']['total_attempts'] > 0 and 
                   (wp['stats']['correct'] / wp['stats']['total_attempts'] < 0.7 or 
                    wp['stats']['mastery_level'] < 2)]
        review = [wp for wp in word_priorities if wp['stats']['total_attempts'] > 0 and 
                 wp['stats']['correct'] / wp['stats']['total_attempts'] >= 0.7]
        
        # Calculate targets (flexible based on availability)
        target_mistakes = int(num_words * 0.33)
        target_new = int(num_words * 0.33)
        target_review = num_words - target_mistakes - target_new
        
        practice_list = []
        
        # Add mistakes (prioritize recent errors and low accuracy)
        mistakes_to_add = min(len(mistakes), target_mistakes)
        practice_list.extend([wp['word'] for wp in mistakes[:mistakes_to_add]])
        
        # Add new words
        new_to_add = min(len(never_seen), target_new)
        practice_list.extend([wp['word'] for wp in never_seen[:new_to_add]])
        
        # Fill remaining with review words (prefer variety of mastery levels)
        remaining = num_words - len(practice_list)
        if remaining > 0:
            # Mix of all remaining words by priority
            remaining_pool = mistakes[mistakes_to_add:] + never_seen[new_to_add:] + review
            remaining_pool.sort(key=lambda x: x['priority'], reverse=True)
            practice_list.extend([wp['word'] for wp in remaining_pool[:remaining]])
        
        # Final shuffle to mix categories
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