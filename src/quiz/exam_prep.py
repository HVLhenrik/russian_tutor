import random

class ExamPrep:
    """Exam preparation module for RUS100-style questions"""
    
    def __init__(self, noun_db, adj_db, pronoun_db, pair_db):
        self.noun_db = noun_db
        self.adj_db = adj_db
        self.pronoun_db = pronoun_db
        self.pair_db = pair_db
    
    def generate_declension_table_exercise(self):
        """
        Generate a full declension table exercise like exam question 1
        Returns: (pair_info, required_cases, answers)
        """
        # Get a random pair
        pairs = self.pair_db.get_all_pairs()
        pair_name = random.choice(list(pairs.keys()))
        pair_info = pairs[pair_name]
        
        adjective = pair_info['adjective']
        noun = pair_info['noun']
        gender = pair_info['gender']
        
        # Cases required in exam (NO instrumental - only akkusativ, genitiv, dativ, lokativ/prepositional)
        required_cases = ['accusative', 'genitive', 'dative', 'prepositional']
        
        # Get all forms
        answers = {}
        adj_forms = self.adj_db.get_all_adjectives()[adjective][gender]
        noun_forms = self.noun_db.get_all_nouns()[noun]
        
        for case in required_cases:
            if case in adj_forms and case in noun_forms:
                answers[case] = {
                    'adjective': adj_forms[case],
                    'noun': noun_forms[case]
                }
        
        return pair_info, required_cases, answers
    
    def present_declension_table_exercise(self):
        """Present and evaluate a full declension table exercise"""
        print("\n" + "=" * 80)
        print("EXAM EXERCISE 1: FULL DECLENSION TABLE")
        print("=" * 80)
        print("\nDecline the following adjective and noun in accusative, genitive, dative, and prepositional.")
        print("=" * 80)
        
        pair_info, required_cases, answers = self.generate_declension_table_exercise()
        
        adjective = pair_info['adjective']
        noun = pair_info['noun']
        gender = pair_info['gender']
        translation = pair_info['translation']
        
        # Get nominative forms
        adj_nom = self.adj_db.get_all_adjectives()[adjective][gender]['nominative']
        noun_nom = self.noun_db.get_all_nouns()[noun]['nominative']
        
        print(f"\n{gender.upper()}: {adj_nom} {noun_nom} ({translation})")
        print("\n{:<20} {:<30} {:<30}".format("Case", "Adjective", "Noun"))
        print("-" * 80)
        print("{:<20} {:<30} {:<30}".format("Nominative", adj_nom, noun_nom))
        
        user_answers = {}
        
        # Collect user answers
        for case in required_cases:
            print(f"\n{case.upper()}:")
            user_adj = input(f"  Adjective: ").strip()
            user_noun = input(f"  Noun: ").strip()
            user_answers[case] = {'adjective': user_adj, 'noun': user_noun}
        
        # Evaluate
        print("\n" + "=" * 80)
        print("RESULTS:")
        print("=" * 80)
        
        correct_count = 0
        total_count = len(required_cases) * 2  # 2 words per case
        
        print("\n{:<20} {:<30} {:<30}".format("Case", "Your Answer", "Correct Answer"))
        print("-" * 80)
        print("{:<20} {:<30} {:<30}".format("Nominative", 
                                             f"{adj_nom} {noun_nom}", 
                                             f"{adj_nom} {noun_nom}"))
        
        for case in required_cases:
            user_adj = user_answers[case]['adjective']
            user_noun = user_answers[case]['noun']
            correct_adj = answers[case]['adjective']
            correct_noun = answers[case]['noun']
            
            adj_correct = user_adj.lower() == correct_adj.lower()
            noun_correct = user_noun.lower() == correct_noun.lower()
            
            if adj_correct:
                correct_count += 1
            if noun_correct:
                correct_count += 1
            
            status_adj = "✅" if adj_correct else "❌"
            status_noun = "✅" if noun_correct else "❌"
            
            print("{:<20} {:<30} {:<30}".format(
                case.upper(),
                f"{status_adj} {user_adj} | {status_noun} {user_noun}",
                f"{correct_adj} {correct_noun}"
            ))
        
        percentage = (correct_count / total_count) * 100
        print("\n" + "=" * 80)
        print(f"Score: {correct_count}/{total_count} ({percentage:.1f}%)")
        print("=" * 80 + "\n")
        
        return correct_count, total_count
    
    def generate_fill_in_blank_exercise(self):
        """
        Generate fill-in-the-blank exercises like exam question 2
        This creates contextualized sentences requiring correct case/form
        NO INSTRUMENTAL CASE
        """
        # Template sentences with blanks (removed instrumental cases)
        templates = [
            {
                'text': "(Я) _____ зовут Иван. (Я) _____ 25 _____ (год).",
                'blanks': [
                    {'word': 'меня', 'explanation': 'Accusative of я (меня зовут pattern)'},
                    {'word': 'мне', 'explanation': 'Dative of я (age construction)'},
                    {'word': 'лет', 'explanation': 'Genitive plural of год (after 5+)'}
                ]
            },
            {
                'text': "Живу в _____ (Москва). Работаю в _____ (большой офис).",
                'blanks': [
                    {'word': 'Москве', 'explanation': 'Prepositional case after в (location)'},
                    {'word': 'большом офисе', 'explanation': 'Prepositional case of adjective + noun'}
                ]
            },
            {
                'text': "У _____ (я) есть _____ (хороший друг). Я _____ (он) часто звоню.",
                'blanks': [
                    {'word': 'меня', 'explanation': 'Genitive after у (possession)'},
                    {'word': 'хороший друг', 'explanation': 'Nominative (subject)'},
                    {'word': 'ему', 'explanation': 'Dative after звонить (to call someone)'}
                ]
            },
            {
                'text': "Моя мама любит _____ (вкусная еда). Она готовит для _____ (мы).",
                'blanks': [
                    {'word': 'вкусную еду', 'explanation': 'Accusative of adjective + noun (direct object)'},
                    {'word': 'нас', 'explanation': 'Genitive after для (for us)'}
                ]
            },
            {
                'text': "Мы живём в _____ (новый дом). Около _____ (наш дом) есть парк.",
                'blanks': [
                    {'word': 'новом доме', 'explanation': 'Prepositional case (location)'},
                    {'word': 'нашего дома', 'explanation': 'Genitive after около (near)'}
                ]
            },
            {
                'text': "Студенты идут к _____ (университет). Они говорят о _____ (экзамен).",
                'blanks': [
                    {'word': 'университету', 'explanation': 'Dative after к (toward)'},
                    {'word': 'экзамене', 'explanation': 'Prepositional after о (about)'}
                ]
            },
            {
                'text': "Я вижу _____ (красивая девушка). Хочу дать _____ (она) цветы.",
                'blanks': [
                    {'word': 'красивую девушку', 'explanation': 'Accusative (direct object - animate)'},
                    {'word': 'ей', 'explanation': 'Dative of она (to her)'}
                ]
            }
        ]
        
        return random.choice(templates)
    
    def present_fill_in_blank_exercise(self):
        """Present and evaluate fill-in-the-blank exercise"""
        print("\n" + "=" * 80)
        print("EXAM EXERCISE 2: FILL IN THE BLANKS")
        print("=" * 80)
        print("\nSett inn rett form av substantiv, adjektiv og pronomen i parentes.")
        print("(Insert the correct form of nouns, adjectives, and pronouns in parentheses.)")
        print("=" * 80)
        
        exercise = self.generate_fill_in_blank_exercise()
        
        print(f"\n{exercise['text']}\n")
        
        user_answers = []
        for i, blank in enumerate(exercise['blanks'], 1):
            answer = input(f"Blank {i}: ").strip()
            user_answers.append(answer)
        
        # Evaluate
        print("\n" + "=" * 80)
        print("RESULTS:")
        print("=" * 80 + "\n")
        
        correct_count = 0
        for i, blank in enumerate(exercise['blanks']):
            user_answer = user_answers[i]
            correct_answer = blank['word']
            is_correct = user_answer.lower() == correct_answer.lower()
            
            if is_correct:
                correct_count += 1
                print(f"Blank {i+1}: ✅ {user_answer}")
            else:
                print(f"Blank {i+1}: ❌ {user_answer}")
                print(f"         Correct: {correct_answer}")
            print(f"         Explanation: {blank['explanation']}\n")
        
        percentage = (correct_count / len(exercise['blanks'])) * 100
        print("=" * 80)
        print(f"Score: {correct_count}/{len(exercise['blanks'])} ({percentage:.1f}%)")
        print("=" * 80 + "\n")
        
        return correct_count, len(exercise['blanks'])
    
    def run_full_exam_practice(self):
        """Run a full exam-style practice session"""
        print("\n" + "=" * 80)
        print("FULL EXAM PRACTICE SESSION")
        print("=" * 80)
        print("\nThis practice session mimics the RUS100 exam format:")
        print("  1. Full declension tables")
        print("  2. Fill-in-the-blank contextual exercises")
        print("\nYou will complete both types of exercises.")
        print("=" * 80)
        
        input("\nPress Enter to begin...")
        
        # Exercise 1: Declension table
        correct1, total1 = self.present_declension_table_exercise()
        
        input("\nPress Enter to continue to Exercise 2...")
        
        # Exercise 2: Fill in blanks
        correct2, total2 = self.present_fill_in_blank_exercise()
        
        # Final results
        total_correct = correct1 + correct2
        total_questions = total1 + total2
        final_percentage = (total_correct / total_questions) * 100
        
        print("\n" + "=" * 80)
        print("FINAL EXAM PRACTICE RESULTS")
        print("=" * 80)
        print(f"\nExercise 1 (Declension Table): {correct1}/{total1}")
        print(f"Exercise 2 (Fill in Blanks): {correct2}/{total2}")
        print(f"\nTotal Score: {total_correct}/{total_questions} ({final_percentage:.1f}%)")
        
        if final_percentage >= 90:
            print("\n🌟 Excellent! You're well prepared for the exam!")
        elif final_percentage >= 75:
            print("\n👍 Good work! A bit more practice and you'll be ready!")
        elif final_percentage >= 60:
            print("\n📚 Keep practicing! Focus on the areas you struggled with.")
        else:
            print("\n💪 You need more practice. Review the declension rules and try again!")
        
        print("=" * 80 + "\n")
    
    def practice_exam(self):
        """Run a practice exam session"""
        print("\n" + "=" * 60)
        print("  📝 PRACTICE EXAM SESSION")
        print("=" * 60)
        print("\n💡 Type 'quit' or 'q' at any time to exit")
        
        num_questions = input("\nNumber of questions (default 20): ").strip()
        num_questions = int(num_questions) if num_questions.isdigit() else 20
        
        session_aborted = False
        correct = 0
        
        for i in range(num_questions):
            question = self._generate_exam_question()
            
            print(f"\n{'-' * 60}")
            print(f"Question {i + 1}/{num_questions}")
            print(f"{'-' * 60}")
            print(f"\n{question['prompt']}")
            
            user_answer = input("\nYour answer: ").strip()
            
            # Check for quit
            if user_answer.lower() in ['quit', 'q', 'exit']:
                print("\n⚠️  Practice exam aborted by user")
                session_aborted = True
                break
            
            is_correct = self._check_answer(user_answer, question['answer'])
            
            if is_correct:
                print("✅ Correct!")
                correct += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {question['answer']}")
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {question['answer']}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if practice_answer.lower() in ['quit', 'q', 'exit']:
                        print("\n⚠️  Practice exam aborted by user")
                        session_aborted = True
                        break
                    
                    if self._check_answer(practice_answer, question['answer']):
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {question['answer']}")
                
                if session_aborted:
                    break
            
            self._record_result(question, is_correct)
        
        # Show results
        total = i + 1 if not session_aborted else i
        if total > 0:
            percentage = (correct / total) * 100
            print(f"\n{'=' * 60}")
            if session_aborted:
                print("  ⚠️  PRACTICE EXAM INCOMPLETE")
            else:
                print("  ✅ PRACTICE EXAM COMPLETE")
            print(f"{'=' * 60}")
            print(f"\nScore: {correct}/{total} ({percentage:.1f}%)")
            
            if percentage >= 90:
                print("🌟 Excellent! You're ready for the exam!")
            elif percentage >= 75:
                print("👍 Good job! A bit more practice and you'll ace it!")
            elif percentage >= 60:
                print("📚 Keep studying! Review your weak areas.")
            else:
                print("💪 More practice needed! Focus on the basics.")