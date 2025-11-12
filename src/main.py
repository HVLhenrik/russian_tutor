import random
from data.noun_database import NounDatabase
from data.adjective_database import AdjectiveDatabase
from data.pronoun_database import PronounDatabase
from data.word_pair_database import WordPairDatabase
from quiz.quiz_engine import QuizEngine
from quiz.exam_prep import ExamPrep
from quiz.word_practice import WordPractice
from utils.display import display_feedback, display_results
from utils.input_helpers import get_yes_no_input, get_quit_input
from utils.declension_rules import (
    display_noun_declension_rules,
    display_adjective_declension_rules,
    display_pronoun_declension_rules,
    display_case_usage_guide,
    display_declension_menu
)

def view_declension_rules():
    """View declension rules reference"""
    while True:
        choice = display_declension_menu()
        
        if choice == '1':
            display_noun_declension_rules()
        elif choice == '2':
            display_adjective_declension_rules()
        elif choice == '3':
            display_pronoun_declension_rules()
        elif choice == '4':
            display_case_usage_guide()
        elif choice == '5':
            break
        else:
            print("\n❌ Invalid choice. Please select 1-5.")
        
        input("\nPress Enter to continue...")

def learn_nouns():
    """Interactive noun learning with practice quiz"""
    noun_db = NounDatabase()
    nouns = noun_db.get_all_nouns()
    
    print("\n=== LEARN RUSSIAN NOUNS ===\n")
    print("💡 Tip: Review the noun declension rules before practicing!")
    print("💡 Type 'quit' or 'q' at any time to exit")
    
    if get_yes_no_input("\nWould you like to view the noun declension rules first? (y/n): "):
        display_noun_declension_rules()
        input("\nPress Enter to continue...")
    
    # Choose practice mode
    print("\nChoose practice mode:")
    print("1. Singular Forms (By Declension)")
    print("2. Plural Forms")
    print("3. Random (All forms)")
    
    mode = input("\nEnter your choice (1-3): ").strip()
    
    practice_plurals = False
    
    if mode == '1':
        print("\nSingular - Choose declension pattern:")
        print("1. First (masculine: consonant/-й, neuter: -о/-е)")
        print("2. Second (feminine: -а/-я)")
        print("3. Third (feminine: -ь)")
        print("4. All singular forms")
        declension = input("Choose (1-4): ").strip()
        declension_map = {'1': 'first', '2': 'second', '3': 'third'}
        selected_declension = declension_map.get(declension)
        
        if selected_declension:
            nouns_to_practice = noun_db.get_nouns_by_declension(selected_declension)
        else:
            nouns_to_practice = nouns
    elif mode == '2':
        # Practice only plural forms
        nouns_to_practice = noun_db.get_nouns_with_plurals()
        practice_plurals = True
        print(f"\n📝 Practicing plural forms ({len(nouns_to_practice)} nouns)")
    else:
        nouns_to_practice = nouns
    
    # Convert to list and shuffle for random practice
    noun_list = list(nouns_to_practice.items())
    random.shuffle(noun_list)
    
    if not noun_list:
        print("\n❌ No nouns found for your selection.")
        return
    
    print(f"\n📚 Practicing {len(noun_list)} nouns")
    print("=" * 40)
    
    session_aborted = False
    
    for noun_word, declensions in noun_list:
        print(f"\n{'=' * 40}")
        print(f"Noun: {noun_word}")
        if 'gender' in declensions:
            print(f"Gender: {declensions['gender']}")
        if 'declension' in declensions:
            print(f"Declension: {declensions['declension']}")
        print(f"{'=' * 40}")
        
        # Quiz on each case
        if practice_plurals:
            cases = ['nominative_plural', 'accusative_plural', 'genitive_plural', 'dative_plural', 'prepositional_plural']
            case_names = ['Nominative (plural)', 'Accusative (plural)', 'Genitive (plural)', 'Dative (plural)', 'Prepositional (plural)']
        else:
            cases = ['nominative', 'accusative', 'genitive', 'dative', 'prepositional']
            case_names = ['Nominative', 'Accusative', 'Genitive', 'Dative', 'Prepositional']
        
        correct_in_row = 0
        
        for case, case_name in zip(cases, case_names):
            if case not in declensions:
                continue
                
            correct_form = declensions[case]
            print(f"\n{case_name}:")
            user_answer = input("Your answer: ").strip()
            
            # Check for quit
            if get_quit_input(user_answer):
                print("\n⚠️  Practice session aborted by user")
                session_aborted = True
                break
            
            if user_answer.lower() == correct_form.lower():
                display_feedback(True, correct_form)
                correct_in_row += 1
            else:
                display_feedback(False, correct_form)
                correct_in_row = 0
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {correct_form}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if get_quit_input(practice_answer):
                        print("\n⚠️  Practice session aborted by user")
                        session_aborted = True
                        break
                    
                    if practice_answer.lower() == correct_form.lower():
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {correct_form}")
                
                if session_aborted:
                    break
        
        if session_aborted:
            break
        
        # Show summary after completing the noun
        expected_cases = len([c for c in cases if c in declensions])
        if correct_in_row == expected_cases:
            print(f"\n🌟 Perfect! You got all forms of '{noun_word}' correct!")
        
        if not get_yes_no_input("\nContinue with next noun? (y/n): "):
            break
    
    if session_aborted:
        print("\n⚠️ Practice session incomplete")
    else:
        print("\n✅ Finished learning nouns!\n")

def learn_adjectives():
    """Interactive adjective learning with practice quiz"""
    adj_db = AdjectiveDatabase()
    adjectives = adj_db.get_all_adjectives()
    
    print("\n=== LEARN RUSSIAN ADJECTIVES ===\n")
    print("💡 Tip: Review the declension rules before practicing!")
    print("💡 Type 'quit' or 'q' at any time to exit")
    
    if get_yes_no_input("\nWould you like to view the adjective declension rules first? (y/n): "):
        display_adjective_declension_rules()
        input("\nPress Enter to continue...")
    
    # Get random sample of adjectives to practice
    adj_list = list(adjectives.items())
    random.shuffle(adj_list)
    
    # Case order for systematic practice (exam cases only)
    case_order = ['nominative', 'accusative', 'genitive', 'dative', 'prepositional']
    
    session_aborted = False
    
    for adj_word, declensions in adj_list:
        print(f"\n{'=' * 40}")
        print(f"Adjective: {adj_word}")
        print(f"{'=' * 40}")
        
        # Don't show the forms - that's what they need to learn!
        print("\n" + "-" * 40)
        print("Decline this adjective (masculine forms):")
        print("-" * 40)
        
        # Practice masculine forms
        correct_in_row = 0
        
        for case in case_order:
            # Access the masculine forms correctly
            if 'masculine' not in declensions or case not in declensions['masculine']:
                continue
                
            correct_form = declensions['masculine'][case]
            print(f"\n{case.capitalize()} (masculine):")
            user_answer = input("Your answer: ").strip()
            
            # Check for quit
            if get_quit_input(user_answer):
                print("\n⚠️  Practice session aborted by user")
                session_aborted = True
                break
            
            if user_answer.lower() == correct_form.lower():
                display_feedback(True, correct_form)
                correct_in_row += 1
            else:
                display_feedback(False, correct_form)
                correct_in_row = 0
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {correct_form}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if get_quit_input(practice_answer):
                        print("\n⚠️  Practice session aborted by user")
                        session_aborted = True
                        break
                    
                    if practice_answer.lower() == correct_form.lower():
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {correct_form}")
                
                if session_aborted:
                    break
        
        if session_aborted:
            break
        
        # Show summary after completing the adjective
        if correct_in_row == len([c for c in case_order if 'masculine' in declensions and c in declensions['masculine']]):
            print(f"\n🌟 Perfect! You got all forms of '{adj_word}' correct!")
        
        if not get_yes_no_input("\nContinue with next adjective? (y/n): "):
            break
    
    if session_aborted:
        print("\n⚠️ Practice session incomplete")
    else:
        print("\n✅ Finished learning adjectives!\n")

def learn_pronouns():
    """Interactive personal pronoun learning with practice quiz"""
    pronoun_db = PronounDatabase()
    pronouns = pronoun_db.get_all_pronouns()
    
    print("\n=== LEARN RUSSIAN PERSONAL PRONOUNS ===\n")
    print("💡 Tip: Review the pronoun declension table before practicing!")
    print("💡 Type 'quit' or 'q' at any time to exit")
    
    if get_yes_no_input("\nWould you like to view the pronoun declension table first? (y/n): "):
        display_pronoun_declension_rules()
        input("\nPress Enter to continue...")
    
    # Get random sample of pronouns to practice
    pronoun_list = list(pronouns.items())
    random.shuffle(pronoun_list)
    
    # Cases to practice (NO instrumental - only exam cases)
    exam_cases = ['accusative', 'genitive', 'dative', 'prepositional']
    
    session_aborted = False
    
    for pronoun_word, declensions in pronoun_list:
        print(f"\n{'=' * 40}")
        print(f"Pronoun: {pronoun_word}")
        print(f"{'=' * 40}")
        
        # Don't show the forms - that's what they need to learn!
        print("\n" + "-" * 40)
        print("Decline this pronoun:")
        print("-" * 40)
        
        correct_in_row = 0
        
        for case in exam_cases:
            if case not in declensions:
                continue
                
            correct_form = declensions[case]
            print(f"\n{case.capitalize()}:")
            user_answer = input("Your answer: ").strip()
            
            # Check for quit
            if get_quit_input(user_answer):
                print("\n⚠️  Practice session aborted by user")
                session_aborted = True
                break
            
            if user_answer.lower() == correct_form.lower():
                display_feedback(True, correct_form)
                correct_in_row += 1
            else:
                display_feedback(False, correct_form)
                correct_in_row = 0
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {correct_form}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if get_quit_input(practice_answer):
                        print("\n⚠️  Practice session aborted by user")
                        session_aborted = True
                        break
                    
                    if practice_answer.lower() == correct_form.lower():
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {correct_form}")
                
                if session_aborted:
                    break
        
        if session_aborted:
            break
        
        # Show summary after completing the pronoun
        if correct_in_row == len([c for c in exam_cases if c in declensions]):
            print(f"\n🌟 Perfect! You got all forms of '{pronoun_word}' correct!")
        
        if not get_yes_no_input("\nContinue with next pronoun? (y/n): "):
            break
    
    if session_aborted:
        print("\n⚠️ Practice session incomplete")
    else:
        print("\n✅ Finished learning pronouns!\n")

def learn_word_pairs():
    """Interactive learning of adjective-noun pairs with practice quiz"""
    pair_db = WordPairDatabase()
    noun_db = NounDatabase()
    adj_db = AdjectiveDatabase()
    
    print("\n=== LEARN RUSSIAN ADJECTIVE-NOUN PAIRS ===\n")
    print("📚 СЛОВООБРАЗОВАНИЕ & КОНГРУЭНС (Word Formation & Agreement)")
    print("=" * 70)
    print("\nIn Russian, adjectives MUST agree with nouns they describe in:")
    print("  • Gender (masculine, feminine, neuter)")
    print("  • Case (nominative, accusative, genitive, dative, prepositional)")
    print("\nExample: красивый дом → красивого дома (genitive)")
    print("💡 Type 'quit' or 'q' at any time to exit")
    print("=" * 70)
    
    input("\nPress Enter to continue...")
    
    # Choose practice intensity
    print("\nChoose practice intensity:")
    print("1. Quick Review (3 cases per pair, 5 pairs max)")
    print("2. Full Practice (all 4 cases per pair, unlimited)")
    intensity = input("Choice (1-2): ").strip()
    
    # Practice mode selection
    practice_mode = input("\nChoose practice mode:\n1. By Gender\n2. By Category\n3. Random\nChoice: ").strip()
    
    quiz_engine = QuizEngine(
        noun_db.get_all_nouns(),
        adj_db.get_all_adjectives(),
        word_pairs=pair_db.get_all_pairs()
    )
    
    if practice_mode == '1':
        gender = input("Choose gender (masculine/feminine/neuter): ").strip().lower()
        pairs_to_practice = {k: v for k, v in pair_db.get_all_pairs().items() 
                            if v.get('gender') == gender}
    elif practice_mode == '2':
        print("\nCategories: people, places, things, abstract")
        category = input("Choose category: ").strip().lower()
        pairs_to_practice = {k: v for k, v in pair_db.get_all_pairs().items() 
                            if category in v.get('category', '').lower()}
    else:
        pairs_to_practice = pair_db.get_all_pairs()
    
    if not pairs_to_practice:
        print("\n❌ No word pairs found for your selection.")
        return
    
    # Limit pairs based on intensity
    if intensity == '1':
        pairs_list = list(pairs_to_practice.items())[:5]
        practice_cases = ['nominative', 'accusative', 'genitive']
    else:
        pairs_list = list(pairs_to_practice.items())
        practice_cases = ['nominative', 'accusative', 'genitive', 'dative', 'prepositional']
    
    random.shuffle(pairs_list)
    
    correct_count = 0
    total_count = 0
    session_aborted = False
    
    for pair_name, pair_info in pairs_list:
        print(f"\n{'=' * 60}")
        print(f"Word Pair: {pair_name}")
        print(f"Gender: {pair_info.get('gender', 'unknown')}")
        print(f"{'=' * 60}")
        
        adjective = pair_info.get('adjective')
        noun = pair_info.get('noun')
        
        print(f"\nAdjective: {adjective}")
        print(f"Noun: {noun}")
        
        for case in practice_cases:
            total_count += 1
            
            print(f"\n{'-' * 40}")
            print(f"Form the {case} case:")
            user_answer = input(f"{adjective} {noun} ({case}): ").strip()
            
            # Check for quit
            if get_quit_input(user_answer):
                print("\n⚠️  Practice session aborted by user")
                session_aborted = True
                break
            
            # Get correct answer from quiz engine
            correct_form = quiz_engine.get_word_pair_form(pair_name, case)
            
            if user_answer.lower() == correct_form.lower():
                display_feedback(True, correct_form)
                correct_count += 1
            else:
                display_feedback(False, correct_form)
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {correct_form}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if get_quit_input(practice_answer):
                        print("\n⚠️  Practice session aborted by user")
                        session_aborted = True
                        break
                    
                    if practice_answer.lower() == correct_form.lower():
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {correct_form}")
                
                if session_aborted:
                    break
        
        if session_aborted:
            break
        
        if not get_yes_no_input("\nContinue with next pair? (y/n): "):
            break
    
    if total_count > 0:
        percentage = (correct_count / total_count) * 100
        print(f"\n{'=' * 60}")
        if session_aborted:
            print("⚠️  PRACTICE SESSION INCOMPLETE")
        else:
            print("✅ PRACTICE SESSION COMPLETE")
        print(f"{'=' * 60}")
        print(f"\nScore: {correct_count}/{total_count} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🌟 Excellent! You've mastered agreement!")
        elif percentage >= 75:
            print("👍 Great work! Keep practicing!")
        elif percentage >= 60:
            print("📚 Good effort! Review the rules.")
        else:
            print("💪 Keep studying! Agreement takes practice!")

def take_quiz():
    """Run a comprehensive quiz on nouns, adjectives, pronouns, and word pairs"""
    noun_db = NounDatabase()
    adj_db = AdjectiveDatabase()
    pronoun_db = PronounDatabase()
    pair_db = WordPairDatabase()
    
    quiz_engine = QuizEngine(
        noun_db.get_all_nouns(),
        adj_db.get_all_adjectives(),
        pronouns=pronoun_db.get_all_pronouns(),
        word_pairs=pair_db.get_all_pairs()
    )
    
    print("\n=== COMPREHENSIVE RUSSIAN QUIZ ===\n")
    print("💡 Type 'quit' or 'q' at any time to exit")
    
    num_questions = input("How many questions? (default 10): ").strip()
    num_questions = int(num_questions) if num_questions.isdigit() else 10
    
    results = quiz_engine.run_quiz(num_questions)
    display_results(results)

def exam_preparation_mode():
    """Exam preparation mode with focus on exam-relevant cases"""
    # Initialize databases
    noun_db = NounDatabase()
    adj_db = AdjectiveDatabase()
    pronoun_db = PronounDatabase()
    pair_db = WordPairDatabase()
    
    exam_prep = ExamPrep(noun_db, adj_db, pronoun_db, pair_db)
    
    while True:
        print("\n" + "=" * 50)
        print("  📝 EXAM PREPARATION MODE (RUS100)")
        print("=" * 50)
        print("\n1. Practice Declension Tables")
        print("2. Practice Fill-in-the-Blanks")
        print("3. Full Exam Practice (Both Exercises)")
        print("4. View Case Guide")
        print("5. Return to Main Menu")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            exam_prep.present_declension_table_exercise()
            input("\nPress Enter to continue...")
        elif choice == '2':
            exam_prep.present_fill_in_blank_exercise()
            input("\nPress Enter to continue...")
        elif choice == '3':
            exam_prep.run_full_exam_practice()
            input("\nPress Enter to continue...")
        elif choice == '4':
            display_case_usage_guide()
            input("\nPress Enter to continue...")
        elif choice == '5':
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

def word_practice_mode():
    """Word practice mode with intelligent tracking"""
    word_practice = WordPractice()
    
    while True:
        print("\n" + "=" * 50)
        print("  📚 WORD PRACTICE MODE")
        print("=" * 50)
        print("\n1. Start Practice Session (30 words)")
        print("2. View Your Statistics")
        print("3. Reset Statistics")
        print("4. Return to Main Menu")
        print("=" * 50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            word_practice.run_practice_session()
            input("\nPress Enter to continue...")
        elif choice == '2':
            word_practice.view_statistics()
            input("\nPress Enter to continue...")
        elif choice == '3':
            confirm = input("\n⚠️  Are you sure you want to reset all statistics? (yes/no): ")
            if confirm.lower() == 'y':
                word_practice.practice_db.reset_statistics()
            input("\nPress Enter to continue...")
        elif choice == '4':
            break
        else:
            print("\n❌ Invalid choice. Please select 1-4.")

def main():
    print("\n" + "=" * 50)
    print("  🇷🇺 RUSSIAN DECLENSION TUTOR 🇷🇺")
    print("=" * 50)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Learn Nouns")
        print("2. Learn Adjectives")
        print("3. Learn Personal Pronouns")
        print("4. Learn Adjective-Noun Pairs & Agreement")
        print("5. Take a Quiz")
        print("6. Exam Preparation Mode (RUS100)")
        print("7. Word Practice (Vocabulary)")
        print("8. View Declension Rules")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ").strip()
        
        if choice == '1':
            learn_nouns()
        elif choice == '2':
            learn_adjectives()
        elif choice == '3':
            learn_pronouns()
        elif choice == '4':
            learn_word_pairs()
        elif choice == '5':
            take_quiz()
        elif choice == '6':
            exam_preparation_mode()
        elif choice == '7':
            word_practice_mode()
        elif choice == '8':
            view_declension_rules()
        elif choice == '9':
            print("\n👋 Goodbye! Keep practicing your Russian!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-9.")

if __name__ == "__main__":
    main()