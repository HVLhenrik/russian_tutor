from typing import List, Dict
from data.word_practice_database import WordPracticeDatabase
from data.vocabulary_extractor import VocabularyExtractor
from utils.display import display_feedback
from utils.input_helpers import get_quit_input

class WordPractice:
    """Interactive word practice with intelligent rotation and tracking"""
    
    def __init__(self):
        self.practice_db = WordPracticeDatabase()
        self.vocab_extractor = VocabularyExtractor()
    
    def normalize_answer(self, answer: str) -> str:
        """Normalize user answer for comparison"""
        return answer.lower().strip()
    
    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        """Check if user answer matches (with some flexibility)"""
        user_normalized = self.normalize_answer(user_answer)
        correct_normalized = self.normalize_answer(correct_answer)
        
        # Exact match
        if user_normalized == correct_normalized:
            return True
        
        # Check if answer contains the correct word (for multi-word translations)
        if ',' in correct_answer:
            # If multiple options given (e.g., "do, make"), accept any
            options = [self.normalize_answer(opt) for opt in correct_answer.split(',')]
            if user_normalized in options:
                return True
        
        return False
    
    def run_practice_session(self, words_per_session: int = 30):
        """Run a complete practice session"""
        print("\n" + "=" * 70)
        print("  📚 WORD PRACTICE SESSION")
        print("=" * 70)
        
        # Get all available words
        all_words = self.vocab_extractor.extract_unique_words()
        
        if not all_words:
            print("\n❌ No words found in database. Please check CSV file.")
            return
        
        print(f"\n📖 Total vocabulary size: {len(all_words)} unique words")
        
        # Let user choose filter
        print("\nPractice mode:")
        print("1. All words (mixed)")
        print("2. Nouns only")
        print("3. Verbs only")
        print("4. Adjectives only")
        
        choice = input("\nEnter choice (1-4, default=1): ").strip()
        
        if choice == '2':
            words_pool = self.vocab_extractor.get_words_by_pos('N')
            print(f"📝 Practicing nouns only ({len(words_pool)} words available)")
        elif choice == '3':
            words_pool = self.vocab_extractor.get_words_by_pos('V')
            print(f"📝 Practicing verbs only ({len(words_pool)} words available)")
        elif choice == '4':
            words_pool = self.vocab_extractor.get_words_by_pos('A')
            print(f"📝 Practicing adjectives only ({len(words_pool)} words available)")
        else:
            words_pool = all_words
            print(f"📝 Practicing all word types ({len(words_pool)} words available)")
        
        # Select words intelligently based on practice history
        practice_words = self.practice_db.get_words_for_practice(
            words_pool, 
            num_words=min(words_per_session, len(words_pool))
        )
        
        print(f"\n🎯 Session: {len(practice_words)} words")
        print("=" * 70)
        print("\n💡 Tip: Type 'quit' or 'q' at any time to exit the session")
        
        input("\nPress Enter to start...")
        
        # Start session
        session_id = self.practice_db.start_session()
        correct_count = 0
        incorrect_words = []
        session_aborted = False
        
        # Practice each word
        for i, word in enumerate(practice_words, 1):
            russian = word['russian']
            english = word['english']
            pos = word['pos']
            
            # Add to session
            self.practice_db.add_word_to_session(session_id, russian)
            
            # Get stats for motivation
            stats = self.practice_db.get_word_stats(russian)
            
            print(f"\n{'─' * 70}")
            print(f"Word {i}/{len(practice_words)}")
            if stats['total_attempts'] > 0:
                accuracy = (stats['correct'] / stats['total_attempts'] * 100)
                print(f"Your history: {stats['correct']}/{stats['total_attempts']} correct ({accuracy:.0f}%) | Streak: {stats['streak']}")
            print(f"{'─' * 70}")
            
            print(f"\n📖 Translate to Russian: {english}")
            print(f"   Part of speech: {pos}")
            
            user_answer = input("\n   Your answer: ").strip()
            
            # Check if user wants to quit
            if get_quit_input(user_answer):
                print("\n⚠️  Session aborted by user")
                session_aborted = True
                break
            
            is_correct = self.check_answer(user_answer, russian)
            
            # Record attempt
            self.practice_db.record_attempt(russian, english, user_answer, is_correct)
            
            if is_correct:
                display_feedback(True, russian)
                correct_count += 1
            else:
                display_feedback(False, russian)
                incorrect_words.append({
                    'russian': russian,
                    'english': english,
                    'user_answer': user_answer
                })
                
                # Make user write the correct answer
                print(f"\n✍️  Please write the correct answer to continue: {russian}")
                
                max_attempts = 3
                for attempt in range(max_attempts):
                    practice_answer = input("   Type it here: ").strip()
                    
                    # Allow quitting during practice too
                    if get_quit_input(practice_answer):
                        print("\n⚠️  Session aborted by user")
                        session_aborted = True
                        break
                    
                    if self.check_answer(practice_answer, russian):
                        print("   ✅ Correct! Moving on...")
                        break
                    else:
                        if attempt < max_attempts - 1:
                            print(f"   ❌ Not quite. Try again ({attempt + 2}/{max_attempts})")
                        else:
                            print(f"   ⚠️  The correct answer is: {russian}")
                            print("   Please practice this word!")
                
                if session_aborted:
                    break
        
        # Calculate words practiced (only count words that were attempted)
        words_practiced = i if not session_aborted else i
        
        # End session
        incorrect_count = len(incorrect_words)
        self.practice_db.end_session(session_id, correct_count, incorrect_count)
        
        # Display session results
        if session_aborted:
            print(f"\n📊 Partial session results ({words_practiced}/{len(practice_words)} words)")
        
        self._display_session_results(
            correct_count, 
            words_practiced, 
            incorrect_words,
            aborted=session_aborted
        )
    
    def _display_session_results(self, correct: int, total: int, 
                                  incorrect_words: List[Dict],
                                  aborted: bool = False):
        """Display session results with detailed feedback"""
        print("\n" + "=" * 70)
        if aborted:
            print("  📊 SESSION ABORTED (Partial Results)")
        else:
            print("  📊 SESSION COMPLETE")
        print("=" * 70)
        
        percentage = (correct / total * 100) if total > 0 else 0
        
        print(f"\n✅ Correct: {correct}/{total}")
        print(f"❌ Incorrect: {len(incorrect_words)}/{total}")
        print(f"📈 Accuracy: {percentage:.1f}%")
        
        if not aborted:
            if percentage >= 90:
                print("\n🌟 Excellent work! You're mastering Russian vocabulary!")
            elif percentage >= 75:
                print("\n👍 Good job! Keep practicing!")
            elif percentage >= 60:
                print("\n📚 Not bad! Review the words you missed.")
            else:
                print("\n💪 Keep studying! Practice makes perfect!")
        else:
            print("\n💡 Come back and finish your practice session when you're ready!")
        
        # Show words to review
        if incorrect_words:
            print("\n" + "─" * 70)
            print("Words to review:")
            print("─" * 70)
            for item in incorrect_words:
                print(f"\n  {item['english']}")
                print(f"  ❌ Your answer: {item['user_answer']}")
                print(f"  ✅ Correct: {item['russian']}")
        
        # Show overall statistics
        stats = self.practice_db.get_statistics()
        print("\n" + "=" * 70)
        print("  📈 OVERALL STATISTICS")
        print("=" * 70)
        print(f"\nTotal words practiced: {stats['total_words_practiced']}")
        print(f"Total attempts: {stats['total_attempts']}")
        print(f"Overall accuracy: {stats['accuracy']:.1f}%")
        print(f"Mastered words: {stats['mastered_words']}")
        print(f"Total sessions: {stats['total_sessions']}")
        print("=" * 70)
    
    def view_statistics(self):
        """View detailed practice statistics"""
        stats = self.practice_db.get_statistics()
        
        print("\n" + "=" * 70)
        print("  📊 YOUR PRACTICE STATISTICS")
        print("=" * 70)
        
        print(f"\n📚 Vocabulary Progress:")
        print(f"  Total words practiced: {stats['total_words_practiced']}")
        print(f"  ✅ Mastered words (level 4-5, 80%+ accuracy): {stats['mastered_words']}")
        print(f"  ⚠️  Needs review (low accuracy/proficiency): {stats['needs_review']}")
        print(f"  Overall accuracy: {stats['accuracy']:.1f}%")
        
        print(f"\n📝 Practice History:")
        print(f"  Total sessions: {stats['total_sessions']}")
        print(f"  Total attempts: {stats['total_attempts']}")
        print(f"  Correct answers: {stats['total_correct']}")
        print(f"  Incorrect answers: {stats['total_incorrect']}")
        
        # Show recent sessions
        recent_sessions = self.practice_db.get_session_history(limit=5)
        if recent_sessions:
            print(f"\n📅 Recent Sessions:")
            for i, session in enumerate(recent_sessions, 1):
                if session['end_time']:
                    total_questions = session['correct_count'] + session['incorrect_count']
                    if total_questions > 0:
                        accuracy = (session['correct_count'] / total_questions * 100)
                        print(f"\n  Session {i}:")
                        print(f"    Date: {session['start_time'][:10]}")
                        print(f"    Score: {session['correct_count']}/{total_questions}")
                        print(f"    Accuracy: {accuracy:.1f}%")
        
        print("=" * 70)