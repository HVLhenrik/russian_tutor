def get_adjective_declensions(adjective):
    declensions = {
        'красивый': {
            'nominative': 'красивый',
            'genitive': 'красивого',
            'dative': 'красивому',
            'accusative': 'красивого',
            'instrumental': 'красивым',
            'prepositional': 'красивом'
        },
        'умный': {
            'nominative': 'умный',
            'genitive': 'умного',
            'dative': 'умному',
            'accusative': 'умного',
            'instrumental': 'умным',
            'prepositional': 'умном'
        },
        'смешной': {
            'nominative': 'смешной',
            'genitive': 'смешного',
            'dative': 'смешному',
            'accusative': 'смешного',
            'instrumental': 'смешным',
            'prepositional': 'смешном'
        },
        # Add more adjectives and their declensions here
    }
    
    return declensions.get(adjective, "Adjective not found.")

def display_declensions(adjective):
    declensions = get_adjective_declensions(adjective)
    if isinstance(declensions, str):
        print(declensions)
    else:
        print(f"Declensions for '{adjective}':")
        for case, form in declensions.items():
            print(f"{case.capitalize()}: {form}")

if __name__ == "__main__":
    print("Welcome to the Russian Adjective Declension Tutor!")
    user_input = input("Enter an adjective to see its declensions: ")
    display_declensions(user_input)