def get_yes_no_input(prompt: str) -> bool:
    """
    Get yes/no input from user, accepting both English and Russian keyboard layouts.
    
    Accepts:
    - English: y/yes/n/no
    - Russian: ы/н (when user forgets to switch keyboard)
    
    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input(prompt).lower().strip()
        
        # Yes responses (English and Russian keyboard)
        if response in ['y', 'yes', 'ы', 'ыес']:  # 'ы' is 'y' on Russian keyboard
            return True
        
        # No responses (English and Russian keyboard)
        if response in ['n', 'no', 'н', 'но']:  # 'т' is 'n' on Russian keyboard
            return False
        
        print("❌ Please enter 'y' for yes or 'n' for no (or 'ы'/'н' if using Russian keyboard)")

def get_quit_input(user_input: str) -> bool:
    """
    Check if user wants to quit, accepting both English and Russian keyboard layouts.
    
    Accepts:
    - English: quit/q/exit
    - Russian: йгше/й/учшею (when user forgets to switch keyboard)
    
    Returns:
        bool: True if user wants to quit, False otherwise
    """
    user_input_lower = user_input.lower().strip()
    
    # English quit commands
    english_quit = ['quit', 'q', 'exit']
    
    # Russian keyboard equivalents
    # 'quit' = 'йгше', 'q' = 'й', 'exit' = 'учшею'
    russian_quit = ['яуит', 'я', 'ехит']
    
    return user_input_lower in english_quit or user_input_lower in russian_quit