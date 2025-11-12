def display_noun_declension_rules():
    """Display the general rules for noun declensions in Russian"""
    print("\n" + "=" * 80)
    print("📚 RUSSIAN NOUN DECLENSION RULES")
    print("=" * 80)
    print("\n{:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Case", "1st Declension", "2nd Declension", "3rd Declension", "Plural"
    ))
    print("-" * 80)
    
    rules = [
        ("Nominative", "-/-ь, -о/-е", "-а/-я", "-ь", "-ы (-и)/-а (-я)"),
        ("Accusative", "= Nominative", "-у/-ю", "= Nominative", "= Nominative"),
        ("Genitive", "-а/-я", "-ы/-и", "-и", "-ов/-ей/—"),
        ("Dative", "-у/-ю", "-е (-и)", "-и", "-ам/-ям"),
        ("Prepositional", "-е", "-е (-и)", "-и", "-ах/-ях")
    ]
    
    for case, decl1, decl2, decl3, plural in rules:
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(
            case, decl1, decl2, decl3, plural
        ))
    
    print("\n" + "=" * 80)
    print("📝 NOTES:")
    print("• 1st Declension: Masculine nouns ending in consonant/-ь, Neuter nouns (-о/-е)")
    print("• 2nd Declension: Feminine nouns ending in -а/-я")
    print("• 3rd Declension: Feminine nouns ending in -ь")
    print("• Animate masculine nouns: Accusative = Genitive")
    print("• Inanimate masculine nouns: Accusative = Nominative")
    print("=" * 80 + "\n")

def display_adjective_declension_rules():
    """Display the general rules for adjective declensions in Russian"""
    print("\n" + "=" * 90)
    print("📚 RUSSIAN ADJECTIVE DECLENSION RULES")
    print("=" * 90)
    print("\n{:<20} {:<22} {:<22} {:<22} {:<22}".format(
        "Case", "Masculine Sing.", "Neuter Sing.", "Feminine Sing.", "Plural"
    ))
    print("-" * 90)
    
    rules = [
        ("Nominative", "-ый(-ой)/-ий", "-ое/-ее", "-ая/-яя", "-ые/-ие"),
        ("Accusative", "= Nom / Gen", "-ое/-ее", "-ую/-юю", "= Nominative"),
        ("Genitive", "-ого/-его", "-ого/-его", "-ой/-ей", "-ых/-их"),
        ("Dative", "-ому/-ему", "-ому/-ему", "-ой/-ей", "-ым/-им"),
        ("Prepositional", "-ом/-ем", "-ом/-ем", "-ой/-ей", "-ых/-их")
    ]
    
    for case, masc, neut, fem, plural in rules:
        print("{:<20} {:<22} {:<22} {:<22} {:<22}".format(
            case, masc, neut, fem, plural
        ))
    
    print("\n" + "=" * 90)
    print("📝 IMPORTANT NOTES:")
    print("\n1. Endings after the slash (/) are used with soft consonants.")
    print("   Russian has only a few soft adjectives. Learn си́ний 'dark blue' as an example.")
    
    print("\n2. In masculine singular, the ending is -ой if the adjective has stress on")
    print("   the ending: большо́й 'big'. Otherwise the ending is -ый: но́вый 'new'.")
    print("   You must learn for each adjective whether the stress falls on the ending.")
    
    print("\n3. Masculine and neuter have the same endings in all cases different from")
    print("   nominative.")
    
    print("\n4. In feminine, we have the same ending in genitive, dative, and prepositional:")
    print("   -ой/-ей.")
    
    print("\n5. In plural, all endings begin with ы/и, and we have the same ending in")
    print("   genitive and prepositional: -ых/-их.")
    
    print("\n• Masculine Accusative: = Nominative (inanimate) / = Genitive (animate)")
    print("• Neuter Accusative: Always = Nominative")
    print("=" * 90 + "\n")

def display_pronoun_declension_rules():
    """Display the declension rules for personal pronouns in Russian"""
    print("\n" + "=" * 100)
    print("📚 RUSSIAN PERSONAL PRONOUN DECLENSIONS")
    print("=" * 100)
    print("\n{:<18} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Case", "я", "ты́", "он", "она́", "мы", "вы", "они́"
    ))
    print("-" * 100)
    
    pronoun_forms = [
        ("Nominative", "я", "ты́", "он", "она́", "мы", "вы", "они́"),
        ("Accusative", "меня́", "тебя́", "(н)его́", "(н)её", "нас", "вас", "(н)их"),
        ("Genitive", "меня́", "тебя́", "(н)его́", "(н)её", "нас", "вас", "(н)их"),
        ("Dative", "мне", "тебе́", "(н)ему́", "(н)ей", "нам", "вам", "(н)им"),
        ("Prepositional", "мне", "тебе́", "нём", "ней", "нас", "вас", "них")
    ]
    
    for case, ya, ty, on, ona, my, vy, oni in pronoun_forms:
        print("{:<18} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            case, ya, ty, on, ona, my, vy, oni
        ))
    
    print("\n" + "=" * 100)
    print("📝 IMPORTANT NOTES:")
    print("\n1. Third person pronouns (он, она́, они́) add н- when used after prepositions:")
    print("   Examples: у него́ (at his place), с ней (with her), о них (about them)")
    
    print("\n2. Forms in parentheses (н) show the optional н- prefix used after prepositions.")
    
    print("\n3. Accusative and Genitive are identical for all personal pronouns.")
    
    print("\n4. First person (я, мы) and second person (ты, вы) pronouns never take the н- prefix.")
    
    print("\n5. Dative and Prepositional are the same for я (мне) and ты (тебе́).")
    print("=" * 100 + "\n")

def display_case_overview():
    """Display overview table of case usage"""
    print("\n" + "=" * 100)
    print("OVERVIEW: SENTENCE ELEMENTS AND CASES")
    print("=" * 100)
    print("\n{:<25} {:<45} {:<25}".format(
        "Sentence Element", "Question", "Case"
    ))
    print("-" * 100)
    
    overview = [
        ("Subject", "Who/What + verb", "Nominative"),
        ("Predicative", "Who/What + be/become + subject?", "Nominative"),
        ("Direct Object", "Who/What + verb (not be/become)?", "Accusative"),
        ("Indirect Object", "To/For whom + verb?", "Dative"),
        ("Adverbial", "Where? When? How?", "Various cases")
    ]
    
    for element, question, case in overview:
        print("{:<25} {:<45} {:<25}".format(element, question, case))
    print("=" * 100 + "\n")

def display_nominative_usage():
    print("\n--- NOMINATIVE ---")
    print("\n{:<5} {:<30} {:<60}".format("No.", "Usage", "Examples"))
    print("-" * 100)
    print("{:<5} {:<30} {:<60}".format(
        "1", "Subject", "Мария работает. 'Maria works.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "2", "Predicative", "Петер – студент. 'Peter is a student.'"
    ))

def display_accusative_usage():
    print("\n--- ACCUSATIVE ---")
    print("\n{:<5} {:<30} {:<60}".format("No.", "Usage", "Examples"))
    print("-" * 100)
    print("{:<5} {:<30} {:<60}".format(
        "1", "Direct object", "Я читаю книгу. 'I read a book.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "2", "Motion towards (в, на)", "Я иду в театр. 'I go to theater.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "3", "Time duration", "Я работал всю неделю. 'I worked all week.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "4", "Days of the week", "в понедельник 'on Monday'"
    ))

def display_genitive_usage():
    print("\n--- GENITIVE ---")
    print("\n{:<5} {:<30} {:<60}".format("No.", "Usage", "Examples"))
    print("-" * 100)
    print("{:<5} {:<30} {:<60}".format(
        "1", "Possession", "книга Марии 'Maria's book'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "2", "Negation (нет)", "У меня нет времени. 'I have no time.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "3", "Quantity", "много студентов 'many students'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "4", "After numbers", "два студента, пять студентов"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "5", "Prepositions", "из, от, у, без, до, после, около"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "6", "Origin", "Я из Лондона. 'I'm from London.'"
    ))

def display_dative_usage():
    print("\n--- DATIVE ---")
    print("\n{:<5} {:<30} {:<60}".format("No.", "Usage", "Examples"))
    print("-" * 100)
    print("{:<5} {:<30} {:<60}".format(
        "1", "Indirect object", "Я даю книгу Марии. 'I give Maria a book.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "2", "Recipient", "Он пишет другу. 'He writes to a friend.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "3", "Age", "Мне 25 лет. 'I am 25 years old.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "4", "Necessity", "Мне надо работать. 'I need to work.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "5", "Prepositions", "к (towards), по (along/by)"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "6", "Emotions", "Мне холодно. 'I am cold.'"
    ))

def display_prepositional_usage():
    print("\n--- PREPOSITIONAL ---")
    print("\n{:<5} {:<30} {:<60}".format("No.", "Usage", "Examples"))
    print("-" * 100)
    print("{:<5} {:<30} {:<60}".format(
        "1", "Location (в, на)", "Я в театре. 'I am at the theater.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "2", "Topic (о/об)", "Мы говорим о фильме. 'We talk about film.'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "3", "Time (в, на)", "в январе 'in January'"
    ))
    print("{:<5} {:<30} {:<60}".format(
        "4", "Always with prep", "Never used without a preposition"
    ))

def display_preposition_notes():
    print("\n" + "=" * 100)
    print("KEY PREPOSITION-CASE PAIRS:")
    print("\n• Motion TO (accusative): в театр, на работу")
    print("• Location AT (prepositional): в театре, на работе")
    print("• Motion FROM (genitive): из театра, с работы")
    print("• Time ON (accusative): в понедельник")
    print("• Time IN (prepositional): в январе")
    print("=" * 100 + "\n")

def display_case_usage_guide():
    """Display comprehensive guide on when to use each Russian case"""
    print("\n" + "=" * 100)
    print("RUSSIAN CASE USAGE GUIDE")
    print("=" * 100)
    
    display_case_overview()
    print("\nDETAILED CASE USAGE")
    print("=" * 100)
    
    display_nominative_usage()
    display_accusative_usage()
    display_genitive_usage()
    display_dative_usage()
    display_prepositional_usage()
    display_preposition_notes()

def display_declension_menu():
    """Display menu for choosing which declension rules to view"""
    print("\n" + "=" * 50)
    print("  📖 DECLENSION RULES REFERENCE")
    print("=" * 50)
    print("\n1. Noun Declension Rules")
    print("2. Adjective Declension Rules")
    print("3. Personal Pronoun Declensions")
    print("4. Case Usage Guide")
    print("5. View All Rules")
    print("6. Return to Main Menu")
    print("=" * 50)