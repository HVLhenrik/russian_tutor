def display_instructions():
    instructions = (
        "Welcome to the Russian Declension Tutor!\n"
        "This program will help you learn how to decline Russian nouns and adjectives.\n"
        "You will be presented with various words and their declensions across different cases.\n"
        "Follow the prompts to practice and improve your understanding of Russian declension.\n"
        "To start, type 'start' and hit Enter.\n"
    )
    print(instructions)

def display_results(correct_count, total_count):
    """Display final quiz results"""
    percentage = (correct_count / total_count) * 100
    
    print("\n" + "=" * 50)
    print("📊 QUIZ RESULTS")
    print("=" * 50)
    print(f"Correct answers: {correct_count}/{total_count}")
    print(f"Score: {percentage:.1f}%")
    
    if percentage >= 90:
        print("🌟 Excellent! You're mastering Russian declensions!")
    elif percentage >= 70:
        print("👍 Good job! Keep practicing!")
    elif percentage >= 50:
        print("📚 Not bad, but more practice would help!")
    else:
        print("💪 Keep studying! Practice makes perfect!")
    print("=" * 50 + "\n")

def display_feedback(is_correct, correct_answer):
    """Display feedback for user's answer"""
    if is_correct:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect! The correct answer is: {correct_answer}")