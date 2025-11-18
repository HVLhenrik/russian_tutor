from typing import List, Dict
from data.word_practice_database import WordPracticeDatabase
from data.vocabulary_extractor import VocabularyExtractor
from data.russian_norwegian_extractor import RussianNorwegianExtractor
from utils.display import display_feedback
from utils.input_helpers import get_quit_input

class WordPractice:
    """Interactive word practice with intelligent rotation and tracking"""
    
    def __init__(self, use_norwegian: bool = False):
        self.use_norwegian = use_norwegian
        
        if use_norwegian:
            self.extractor = RussianNorwegianExtractor()
        else:
            self.extractor = VocabularyExtractor()
        
        self.db = WordPracticeDatabase()
        
        # Check if CSV file exists
        if not self.extractor.check_csv_file():
            print("\n⚠️  Warning: Could not load vocabulary data")
            print("   Make sure the CSV file is in the correct location")

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
        print("\n" + "=" * 60)
        print("  📚 WORD PRACTICE SESSION")
        print("=" * 60)
        
        # Get all available words
        all_words = self.extractor.extract_unique_words()
        
        if not all_words:
            print("\n❌ No words found in database. Please check CSV file.")
            return
        
        print(f"\n📖 Total vocabulary size: {len(all_words)} unique words")
        
        # Show appropriate filter options based on mode
        if self.use_norwegian:
            # Norwegian mode - filter by verb prefix "å"
            print("\nPractice mode:")
            print("1. All words (mixed)")
            print("2. Verbs only")
            
            choice = input("\nEnter choice (1-2, default=1): ").strip()
            
            if choice == '2':
                # Filter words where Norwegian translation starts with "å"
                words_pool = [w for w in all_words if w.get('norwegian', '').startswith('å')]
                print(f"📝 Practicing verbs only ({len(words_pool)} words available)")
            else:
                words_pool = all_words
                print(f"📝 Practicing all words ({len(words_pool)} words available)")
        else:
            # English mode - filter by POS
            print("\nPractice mode:")
            print("1. All words (mixed)")
            print("2. Nouns only")
            print("3. Verbs only")
            print("4. Adjectives only")
            
            choice = input("\nEnter choice (1-4, default=1): ").strip()
            
            if choice == '2':
                words_pool = self.extractor.get_words_by_pos('N')
                print(f"📝 Practicing nouns only ({len(words_pool)} words available)")
            elif choice == '3':
                words_pool = self.extractor.get_words_by_pos('V')
                print(f"📝 Practicing verbs only ({len(words_pool)} words available)")
            elif choice == '4':
                words_pool = self.extractor.get_words_by_pos('A')
                print(f"📝 Practicing adjectives only ({len(words_pool)} words available)")
            else:
                words_pool = all_words
                print(f"📝 Practicing all word types ({len(words_pool)} words available)")
        
        if not words_pool:
            print("\n❌ No words available for this filter.")
            return
        
        # Select words intelligently based on practice history
        # Progress tracking uses Russian word as key, so it works across both modes
        practice_words = self.db.get_words_for_practice(
            words_pool, 
            num_words=min(words_per_session, len(words_pool))
        )
        
        print(f"\n🎯 Session: {len(practice_words)} words")
        print("=" * 60)
        print("\n💡 Tip: Type 'quit' or 'q' at any time to exit the session")
        
        input("\nPress Enter to start...")
        
        # Start session
        session_id = self.db.start_session()
        correct_count = 0
        incorrect_words = []
        session_aborted = False
        
        # Practice each word
        for i, word in enumerate(practice_words, 1):
            russian = word['russian']
            
            # Use correct translation based on language mode
            if self.use_norwegian:
                translation = word.get('norwegian', word.get('english', ''))
                target_lang = "Norwegian"
            else:
                translation = word.get('english', word.get('norwegian', ''))
                target_lang = "English"
            
            pos = word.get('pos', '')
            
            # Add to session (uses Russian as key for consistent tracking)
            self.db.add_word_to_session(session_id, russian)
            
            # Get stats for this specific word (always based on Russian word)
            stats = self.db.get_word_stats(russian)
            
            print(f"\n{'─' * 60}")
            print(f"Word {i}/{len(practice_words)}")
            
            # Show stats if the word has been practiced before
            # Stats are consistent across both English and Norwegian modes
            if stats and stats['total_attempts'] > 0:
                accuracy = (stats['correct'] / stats['total_attempts'] * 100)
                mastery_stars = '⭐' * stats['mastery_level']
                print(f"Your history: {stats['correct']}/{stats['total_attempts']} correct ({accuracy:.0f}%) | {mastery_stars}")
            
            print(f"{'─' * 60}")
            
            # Display question based on direction
            if self.use_norwegian:
                print(f"\n📖 Translate to Russian: {translation}")
                # Show if it's a verb by checking "å" prefix
                if translation.startswith('å'):
                    print(f"   (Verb)")
            else:
                print(f"\n📖 Translate to {target_lang}: {translation}")
                # Only show POS for English mode
                if pos:
                    print(f"   Part of speech: {pos}")
            
            user_answer = input("\n   Your answer: ").strip()
            
            # Check if user wants to quit
            if get_quit_input(user_answer):
                print("\n⚠️  Session aborted by user")
                session_aborted = True
                break
            
            # Check answer against Russian word
            is_correct = self.check_answer(user_answer, russian)
            
            # Record attempt - always use Russian as the key for consistent tracking
            self.db.record_attempt(russian, translation, user_answer, is_correct)
            
            if is_correct:
                display_feedback(True, russian)
                correct_count += 1
            else:
                display_feedback(False, russian)
                incorrect_words.append({
                    'russian': russian,
                    'translation': translation,
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
        words_practiced = i if session_aborted else len(practice_words)
        
        # End session
        incorrect_count = len(incorrect_words)
        self.db.end_session(session_id, correct_count, incorrect_count)
        
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
        print("\n" + "=" * 60)
        if aborted:
            print("  📊 SESSION ABORTED (Partial Results)")
        else:
            print("  📊 SESSION COMPLETE")
        print("=" * 60)
        
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
            print("\n" + "─" * 60)
            print("Words to review:")
            print("─" * 60)
            for item in incorrect_words:
                print(f"\n  {item['translation']}")
                print(f"  ❌ Your answer: {item['user_answer']}")
                print(f"  ✅ Correct: {item['russian']}")
        
        # Show overall statistics
        stats = self.db.get_statistics()
        print("\n" + "=" * 60)
        print("  📈 OVERALL STATISTICS")
        print("=" * 60)
        print(f"\nTotal words practiced: {stats['total_words_practiced']}")
        print(f"Total attempts: {stats['total_attempts']}")
        print(f"Overall accuracy: {stats['accuracy']:.1f}%")
        print(f"Mastered words: {stats['mastered_words']}")
        print(f"Total sessions: {stats['total_sessions']}")
        print("=" * 60)
    
    def view_statistics(self):
        """View detailed practice statistics"""
        stats = self.db.get_statistics()
        
        print("\n" + "=" * 60)
        print("  📊 YOUR PRACTICE STATISTICS")
        print("=" * 60)
        
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
        recent_sessions = self.db.get_session_history(limit=5)
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
        
        print("=" * 60)