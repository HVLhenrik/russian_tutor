"""
Display verb conjugation rules and patterns
"""

def display_verb_conjugation_menu():
    """Display verb conjugation reference menu"""
    print("\n" + "=" * 60)
    print("  📖 RUSSIAN VERB CONJUGATION REFERENCE")
    print("=" * 60)
    print("\n1. Conjugation Patterns (I & II)")
    print("2. Irregular Verbs (11 exceptions)")
    print("3. Verb Aspects (Perfective vs Imperfective)")
    print("4. Past Tense Formation")
    print("5. Return to Main Menu")
    
    return input("\nSelect an option (1-5): ").strip()

def display_conjugation_patterns():
    """Display conjugation I and II patterns"""
    print("\n" + "=" * 60)
    print("  VERB CONJUGATION PATTERNS")
    print("=" * 60)
    
    print("\n📌 FIRST CONJUGATION (-ать, -ять, -еть verbs)")
    print("-" * 60)
    print("Example: работать (to work)")
    print("\nPresent/Future:")
    print("  я работа-ю       мы работа-ем")
    print("  ты работа-ешь    вы работа-ете")
    print("  он работа-ет     они работа-ют")
    
    print("\n📌 SECOND CONJUGATION (-ить verbs)")
    print("-" * 60)
    print("Example: говорить (to speak)")
    print("\nPresent/Future:")
    print("  я говор-ю        мы говор-им")
    print("  ты говор-ишь     вы говор-ите")
    print("  он говор-ит      они говор-ят")
    
    print("\n💡 Key Differences:")
    print("  • Conjugation I: -ю, -ешь, -ет, -ем, -ете, -ют")
    print("  • Conjugation II: -ю/-у, -ишь, -ит, -им, -ите, -ят/-ат")

def display_irregular_verbs():
    """Display the 11 irregular verbs"""
    print("\n" + "=" * 60)
    print("  ⚠️  11 IRREGULAR VERBS (Conjugation II exceptions)")
    print("=" * 60)
    print("\nThese verbs end in -ать/-еть but conjugate like II:")
    print("-" * 60)
    
    irregular = [
        ("гнать", "гоню, гонишь, гонят", "drive, chase"),
        ("держать", "держу, держишь, держат", "hold"),
        ("дышать", "дышу, дышишь, дышат", "breathe"),
        ("слышать", "слышу, слышишь, слышат", "hear"),
        ("смотреть", "смотрю, смотришь, смотрят", "watch"),
        ("видеть", "вижу, видишь, видят", "see"),
        ("ненавидеть", "ненавижу, ненавидишь, ненавидят", "hate"),
        ("зависеть", "завишу, зависишь, зависят", "depend"),
        ("вертеть", "верчу, вертишь, вертят", "turn"),
        ("обидеть", "обижу, обидишь, обидят", "offend"),
        ("терпеть", "терплю, терпишь, терпят", "endure")
    ]
    
    for infinitive, conjugation, english in irregular:
        print(f"\n  {infinitive} ({english})")
        print(f"    {conjugation}")
    
    print("\n💡 Memory tip: All end in -ать or -еть but use -ишь, -ит, -ят!")

def display_verb_aspects():
    """Display information about verb aspects"""
    print("\n" + "=" * 60)
    print("  VERB ASPECTS: Perfective vs Imperfective")
    print("=" * 60)
    
    print("\n📌 IMPERFECTIVE ASPECT")
    print("-" * 60)
    print("  • Describes ongoing, repeated, or habitual actions")
    print("  • Has present tense forms")
    print("  • Example: читать (to read/be reading)")
    print("    Я читаю книгу (I am reading a book)")
    
    print("\n📌 PERFECTIVE ASPECT")
    print("-" * 60)
    print("  • Describes completed actions or results")
    print("  • No present tense (uses future forms)")
    print("  • Example: прочитать (to finish reading)")
    print("    Я прочитаю книгу (I will finish reading the book)")
    
    print("\n💡 Aspectual Pairs:")
    print("  читать (impf) → прочитать (pf)")
    print("  делать (impf) → сделать (pf)")
    print("  писать (impf) → написать (pf)")
    
    print("\n📝 Usage:")
    print("  • Past: Both aspects available")
    print("  • Present: Only imperfective")
    print("  • Future: Both (different meanings)")

def display_past_tense():
    """Display past tense formation rules"""
    print("\n" + "=" * 60)
    print("  PAST TENSE FORMATION")
    print("=" * 60)
    
    print("\n📌 REGULAR FORMATION")
    print("-" * 60)
    print("  Remove -ть, add gender/number endings:")
    print("    Masculine: -л    (он работал)")
    print("    Feminine:  -ла   (она работала)")
    print("    Neuter:    -ло   (оно работало)")
    print("    Plural:    -ли   (они работали)")
    
    print("\n📌 EXAMPLES")
    print("-" * 60)
    print("  читать → читал, читала, читало, читали")
    print("  говорить → говорил, говорила, говорило, говорили")
    print("  видеть → видел, видела, видело, видели")
    
    print("\n⚠️  IRREGULAR PAST TENSE")
    print("-" * 60)
    print("  Some verbs drop consonants:")
    print("    идти → шёл, шла, шло, шли")
    print("    мочь → мог, могла, могло, могли")