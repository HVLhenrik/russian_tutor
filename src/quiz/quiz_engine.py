class QuizEngine:
    def __init__(self, nouns, adjectives, pronouns=None, word_pairs=None):
        self.nouns = nouns
        self.adjectives = adjectives
        self.pronouns = pronouns or {}
        self.word_pairs = word_pairs or {}

    def generate_quiz(self):
        # This method generates a quiz based on nouns and adjectives
        # For simplicity, we will just return a sample question
        sample_question = {
            "question": "What is the genitive case of 'кот' (cat)?",
            "options": ["кота", "кот", "котом", "коте"],
            "answer": "кота"
        }
        return sample_question

    def evaluate_answer(self, user_answer, correct_answer):
        """Evaluate if the user's answer matches the correct answer"""
        # Normalize answers by removing extra whitespace and converting to lowercase
        user_normalized = user_answer.strip().lower()
        correct_normalized = correct_answer.strip().lower()

        return user_normalized == correct_normalized

    def evaluate_pair_answer(self, user_adj, user_noun, correct_adj, correct_noun):
        """Evaluate a complete adjective-noun pair answer"""
        adj_correct = self.evaluate_answer(user_adj, correct_adj)
        noun_correct = self.evaluate_answer(user_noun, correct_noun)

        return adj_correct, noun_correct

    def get_declined_pair(self, adjective, noun, gender, case, adj_db, noun_db):
        """Get the declined forms of both adjective and noun for a given case"""
        # Get adjective declension
        if adjective in adj_db:
            adj_forms = adj_db[adjective]
            if gender in adj_forms and case in adj_forms[gender]:
                declined_adj = adj_forms[gender][case]
            else:
                return None, None
        else:
            return None, None

        # Get noun declension
        if noun in noun_db:
            noun_forms = noun_db[noun]
            if case in noun_forms:
                declined_noun = noun_forms[case]
            else:
                return None, None
        else:
            return None, None

        return declined_adj, declined_noun

    def run_quiz(self, num_questions: int = 10) -> dict:
        """Run a quiz with the specified number of questions"""
        results = {
            'correct': 0,
            'total': num_questions,
            'questions': []
        }
        
        print(f"\n{'=' * 50}")
        print(f"  Starting quiz with {num_questions} questions")
        print(f"{'=' * 50}")
        print("\n💡 Type 'quit' or 'q' at any time to exit")
        
        session_aborted = False
        
        for i in range(num_questions):
            question = self.generate_question()
            
            print(f"\n{'-' * 50}")
            print(f"Question {i + 1}/{num_questions}")
            print(f"{'-' * 50}")
            print(f"\n{question['prompt']}")
            
            user_answer = input("\nYour answer: ").strip()
            
            # Check for quit
            if user_answer.lower() in ['quit', 'q', 'exit']:
                print("\n⚠️  Quiz aborted by user")
                session_aborted = True
                results['total'] = i
                break
            
            is_correct = user_answer.lower() == question['answer'].lower()
            
            if is_correct:
                print("✅ Correct!")
                results['correct'] += 1
            else:
                print(f"❌ Incorrect. The correct answer is: {question['answer']}")
                
                # Make user write correct answer
                print(f"\n✍️  Please write the correct answer: {question['answer']}")
                for attempt in range(3):
                    practice_answer = input("   Type it here: ").strip()
                    
                    if practice_answer.lower() in ['quit', 'q', 'exit']:
                        print("\n⚠️  Quiz aborted by user")
                        session_aborted = True
                        results['total'] = i + 1
                        break
                    
                    if practice_answer.lower() == question['answer'].lower():
                        print("   ✅ Correct! Moving on...")
                        break
                    elif attempt < 2:
                        print(f"   ❌ Try again ({attempt + 2}/3)")
                    else:
                        print(f"   ⚠️  The correct answer is: {question['answer']}")
                
                if session_aborted:
                    break
            
            results['questions'].append({
                'question': question['prompt'],
                'user_answer': user_answer,
                'correct_answer': question['answer'],
                'is_correct': is_correct
            })
        
        if session_aborted:
            print(f"\n⚠️  Quiz incomplete: {results['correct']}/{results['total']} questions")
        
        return results

    def check_agreement(self, adjective_form, noun_form, pair_info, case, adj_db, noun_db):
        """
        Check if the adjective and noun agree in gender, number, and case
        Returns: (is_correct, error_message)
        """
        correct_adj, correct_noun = self.get_declined_pair(
            pair_info['adjective'],
            pair_info['noun'],
            pair_info['gender'],
            case,
            adj_db,
            noun_db
        )

        if correct_adj is None or correct_noun is None:
            return False, "Case not available for this word pair"

        adj_matches = self.evaluate_answer(adjective_form, correct_adj)
        noun_matches = self.evaluate_answer(noun_form, correct_noun)

        if adj_matches and noun_matches:
            return True, "Perfect! Adjective and noun agree in gender, number, and case."
        elif adj_matches:
            return False, f"Adjective is correct, but noun should be '{correct_noun}'"
        elif noun_matches:
            return False, f"Noun is correct, but adjective should be '{correct_adj}'"
        else:
            return False, f"Correct answer: {correct_adj} {correct_noun}"