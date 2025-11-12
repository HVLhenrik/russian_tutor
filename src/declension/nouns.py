class Noun:
    def __init__(self, nominative, genitive, dative, accusative, instrumental, prepositional):
        self.nominative = nominative
        self.genitive = genitive
        self.dative = dative
        self.accusative = accusative
        self.instrumental = instrumental
        self.prepositional = prepositional

    def declension_cases(self):
        return {
            "Nominative": self.nominative,
            "Genitive": self.genitive,
            "Dative": self.dative,
            "Accusative": self.accusative,
            "Instrumental": self.instrumental,
            "Prepositional": self.prepositional,
        }

# List of Russian nouns with their declensions
nouns_list = [
    Noun("стол", "стола", "столу", "стол", "столом", "столе"),  # table
    Noun("книга", "книги", "книге", "книгу", "книгой", "книге"),  # book
    Noun("дом", "дома", "дому", "дом", "домом", "доме"),  # house
    Noun("машина", "машины", "машине", "машину", "машиной", "машине"),  # car
    Noun("человек", "человека", "человеку", "человека", "человеком", "человеке"),  # person
]

def get_noun_declension(noun):
    for n in nouns_list:
        if n.nominative == noun:
            return n.declension_cases()
    return None

def list_all_nouns():
    return [noun.nominative for noun in nouns_list]