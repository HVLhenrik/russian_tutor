class NounDatabase:
    def __init__(self):
        self.nouns = {
            # FIRST DECLENSION - Masculine (ending in consonant or -й)
            "дом": {
                "nominative": "дом",
                "accusative": "дом",
                "genitive": "дома",
                "dative": "дому",
                "prepositional": "доме",
                "nominative_plural": "дома",
                "accusative_plural": "дома",
                "genitive_plural": "домов",
                "dative_plural": "домам",
                "prepositional_plural": "домах",
                "declension": "first",
                "gender": "masculine"
            },
            "город": {
                "nominative": "город",
                "accusative": "город",
                "genitive": "города",
                "dative": "городу",
                "prepositional": "городе",
                "nominative_plural": "города",
                "accusative_plural": "города",
                "genitive_plural": "городов",
                "dative_plural": "городам",
                "prepositional_plural": "городах",
                "declension": "first",
                "gender": "masculine"
            },
            "стол": {
                "nominative": "стол",
                "accusative": "стол",
                "genitive": "стола",
                "dative": "столу",
                "prepositional": "столе",
                "nominative_plural": "столы",
                "accusative_plural": "столы",
                "genitive_plural": "столов",
                "dative_plural": "столам",
                "prepositional_plural": "столах",
                "declension": "first",
                "gender": "masculine"
            },
            "друг": {
                "nominative": "друг",
                "accusative": "друга",
                "genitive": "друга",
                "dative": "другу",
                "prepositional": "друге",
                "nominative_plural": "друзья",
                "accusative_plural": "друзей",
                "genitive_plural": "друзей",
                "dative_plural": "друзьям",
                "prepositional_plural": "друзьях",
                "declension": "first",
                "gender": "masculine",
                "animacy": "animate"
            },
            "человек": {
                "nominative": "человек",
                "accusative": "человека",
                "genitive": "человека",
                "dative": "человеку",
                "prepositional": "человеке",
                "nominative_plural": "люди",
                "accusative_plural": "людей",
                "genitive_plural": "людей",
                "dative_plural": "людям",
                "prepositional_plural": "людях",
                "declension": "first",
                "gender": "masculine",
                "animacy": "animate"
            },
            "язык": {
                "nominative": "язык",
                "accusative": "язык",
                "genitive": "языка",
                "dative": "языку",
                "prepositional": "языке",
                "nominative_plural": "языки",
                "accusative_plural": "языки",
                "genitive_plural": "языков",
                "dative_plural": "языкам",
                "prepositional_plural": "языках",
                "declension": "first",
                "gender": "masculine"
            },
            "салат": {
                "nominative": "салат",
                "accusative": "салат",
                "genitive": "салата",
                "dative": "салату",
                "prepositional": "салате",
                "nominative_plural": "салаты",
                "accusative_plural": "салаты",
                "genitive_plural": "салатов",
                "dative_plural": "салатам",
                "prepositional_plural": "салатах",
                "declension": "first",
                "gender": "masculine"
            },
            "центр": {
                "nominative": "центр",
                "accusative": "центр",
                "genitive": "центра",
                "dative": "центру",
                "prepositional": "центре",
                "nominative_plural": "центры",
                "accusative_plural": "центры",
                "genitive_plural": "центров",
                "dative_plural": "центрам",
                "prepositional_plural": "центрах",
                "declension": "first",
                "gender": "masculine"
            },
            "карандаш": {
                "nominative": "карандаш",
                "accusative": "карандаш",
                "genitive": "карандаша",
                "dative": "карандашу",
                "prepositional": "карандаше",
                "nominative_plural": "карандаши",
                "accusative_plural": "карандаши",
                "genitive_plural": "карандашей",
                "dative_plural": "карандашам",
                "prepositional_plural": "карандашах",
                "declension": "first",
                "gender": "masculine"
            },
            "мальчик": {
                "nominative": "мальчик",
                "accusative": "мальчика",
                "genitive": "мальчика",
                "dative": "мальчику",
                "prepositional": "мальчике",
                "nominative_plural": "мальчики",
                "accusative_plural": "мальчиков",
                "genitive_plural": "мальчиков",
                "dative_plural": "мальчикам",
                "prepositional_plural": "мальчиках",
                "declension": "first",
                "gender": "masculine",
                "animacy": "animate"
            },
            "трамвай": {
                "nominative": "трамвай",
                "accusative": "трамвай",
                "genitive": "трамвая",
                "dative": "трамваю",
                "prepositional": "трамвае",
                "nominative_plural": "трамваи",
                "accusative_plural": "трамваи",
                "genitive_plural": "трамваев",
                "dative_plural": "трамваям",
                "prepositional_plural": "трамваях",
                "declension": "first",
                "gender": "masculine"
            },
            "килограмм": {
                "nominative": "килограмм",
                "accusative": "килограмм",
                "genitive": "килограмма",
                "dative": "килограмму",
                "prepositional": "килограмме",
                "nominative_plural": "килограммы",
                "accusative_plural": "килограммы",
                "genitive_plural": "килограммов",
                "dative_plural": "килограммам",
                "prepositional_plural": "килограммах",
                "declension": "first",
                "gender": "masculine"
            },
            
            # FIRST DECLENSION - Neuter (ending in -о/-е)
            "окно": {
                "nominative": "окно",
                "accusative": "окно",
                "genitive": "окна",
                "dative": "окну",
                "prepositional": "окне",
                "nominative_plural": "окна",
                "accusative_plural": "окна",
                "genitive_plural": "окон",
                "dative_plural": "окнам",
                "prepositional_plural": "окнах",
                "declension": "first",
                "gender": "neuter"
            },
            "слово": {
                "nominative": "слово",
                "accusative": "слово",
                "genitive": "слова",
                "dative": "слову",
                "prepositional": "слове",
                "nominative_plural": "слова",
                "accusative_plural": "слова",
                "genitive_plural": "слов",
                "dative_plural": "словам",
                "prepositional_plural": "словах",
                "declension": "first",
                "gender": "neuter"
            },
            "море": {
                "nominative": "море",
                "accusative": "море",
                "genitive": "моря",
                "dative": "морю",
                "prepositional": "море",
                "nominative_plural": "моря",
                "accusative_plural": "моря",
                "genitive_plural": "морей",
                "dative_plural": "морям",
                "prepositional_plural": "морях",
                "declension": "first",
                "gender": "neuter"
            },
            "место": {
                "nominative": "место",
                "accusative": "место",
                "genitive": "места",
                "dative": "месту",
                "prepositional": "месте",
                "nominative_plural": "места",
                "accusative_plural": "места",
                "genitive_plural": "мест",
                "dative_plural": "местам",
                "prepositional_plural": "местах",
                "declension": "first",
                "gender": "neuter"
            },
            "вино": {
                "nominative": "вино",
                "accusative": "вино",
                "genitive": "вина",
                "dative": "вину",
                "prepositional": "вине",
                "nominative_plural": "вина",
                "accusative_plural": "вина",
                "genitive_plural": "вин",
                "dative_plural": "винам",
                "prepositional_plural": "винах",
                "declension": "first",
                "gender": "neuter"
            },
            "мясо": {
                "nominative": "мясо",
                "accusative": "мясо",
                "genitive": "мяса",
                "dative": "мясу",
                "prepositional": "мясе",
                "nominative_plural": "мяса",
                "accusative_plural": "мяса",
                "genitive_plural": "мяс",
                "dative_plural": "мясам",
                "prepositional_plural": "мясах",
                "declension": "first",
                "gender": "neuter"
            },
            "яйцо": {
                "nominative": "яйцо",
                "accusative": "яйцо",
                "genitive": "яйца",
                "dative": "яйцу",
                "prepositional": "яйце",
                "nominative_plural": "яйца",
                "accusative_plural": "яйца",
                "genitive_plural": "яиц",
                "dative_plural": "яйцам",
                "prepositional_plural": "яйцах",
                "declension": "first",
                "gender": "neuter"
            },
            
            # SECOND DECLENSION - Feminine (ending in -а)
            "книга": {
                "nominative": "книга",
                "accusative": "книгу",
                "genitive": "книги",
                "dative": "книге",
                "prepositional": "книге",
                "nominative_plural": "книги",
                "accusative_plural": "книги",
                "genitive_plural": "куниг",
                "dative_plural": "книгам",
                "prepositional_plural": "книгах",
                "declension": "second",
                "gender": "feminine"
            },
            "машина": {
                "nominative": "машина",
                "accusative": "машину",
                "genitive": "машины",
                "dative": "машине",
                "prepositional": "машине",
                "nominative_plural": "машины",
                "accusative_plural": "машины",
                "genitive_plural": "машин",
                "dative_plural": "машинам",
                "prepositional_plural": "машинах",
                "declension": "second",
                "gender": "feminine"
            },
            "комната": {
                "nominative": "комната",
                "accusative": "комнату",
                "genitive": "комнаты",
                "dative": "комнате",
                "prepositional": "комнате",
                "nominative_plural": "комнаты",
                "accusative_plural": "комнаты",
                "genitive_plural": "комнат",
                "dative_plural": "комнатам",
                "prepositional_plural": "комнатах",
                "declension": "second",
                "gender": "feminine"
            },
            "женщина": {
                "nominative": "женщина",
                "accusative": "женщину",
                "genitive": "женщины",
                "dative": "женщине",
                "prepositional": "женщине",
                "nominative_plural": "женщины",
                "accusative_plural": "женщин",
                "genitive_plural": "женщин",
                "dative_plural": "женщинам",
                "prepositional_plural": "женщинах",
                "declension": "second",
                "gender": "feminine",
                "animacy": "animate"
            },
            "девочка": {
                "nominative": "девочка",
                "accusative": "девочку",
                "genitive": "девочки",
                "dative": "девочке",
                "prepositional": "девочке",
                "nominative_plural": "девочки",
                "accusative_plural": "девочек",
                "genitive_plural": "девочек",
                "dative_plural": "девочкам",
                "prepositional_plural": "девочках",
                "declension": "second",
                "gender": "feminine",
                "animacy": "animate"
            },
            "ручка": {
                "nominative": "ручка",
                "accusative": "ручку",
                "genitive": "ручки",
                "dative": "ручке",
                "prepositional": "ручке",
                "nominative_plural": "ручки",
                "accusative_plural": "ручки",
                "genitive_plural": "ручек",
                "dative_plural": "ручкам",
                "prepositional_plural": "ручках",
                "declension": "second",
                "gender": "feminine"
            },
            "тарелка": {
                "nominative": "тарелка",
                "accusative": "тарелку",
                "genitive": "тарелки",
                "dative": "тарелке",
                "prepositional": "тарелке",
                "nominative_plural": "тарелки",
                "accusative_plural": "тарелки",
                "genitive_plural": "тарелок",
                "dative_plural": "тарелкам",
                "prepositional_plural": "тарелках",
                "declension": "second",
                "gender": "feminine"
            },
            "школа": {
                "nominative": "школа",
                "accusative": "школу",
                "genitive": "школы",
                "dative": "школе",
                "prepositional": "школе",
                "nominative_plural": "школы",
                "accusative_plural": "школы",
                "genitive_plural": "школ",
                "dative_plural": "школам",
                "prepositional_plural": "школах",
                "declension": "second",
                "gender": "feminine"
            },
            "еда": {
                "nominative": "еда",
                "accusative": "еду",
                "genitive": "еды",
                "dative": "еде",
                "prepositional": "еде",
                "nominative_plural": "еды",
                "accusative_plural": "еды",
                "genitive_plural": "ед",
                "dative_plural": "едам",
                "prepositional_plural": "едах",
                "declension": "second",
                "gender": "feminine"
            },
            "соседка": {
                "nominative": "соседка",
                "accusative": "соседку",
                "genitive": "соседки",
                "dative": "соседке",
                "prepositional": "соседке",
                "nominative_plural": "соседки",
                "accusative_plural": "соседок",
                "genitive_plural": "соседок",
                "dative_plural": "соседкам",
                "prepositional_plural": "соседках",
                "declension": "second",
                "gender": "feminine",
                "animacy": "animate"
            },
            "пенсионерка": {
                "nominative": "пенсионерка",
                "accusative": "пенсионерку",
                "genitive": "пенсионерки",
                "dative": "пенсионерке",
                "prepositional": "пенсионерке",
                "nominative_plural": "пенсионерки",
                "accusative_plural": "пенсионерок",
                "genitive_plural": "пенсионерок",
                "dative_plural": "пенсионеркам",
                "prepositional_plural": "пенсионерках",
                "declension": "second",
                "gender": "feminine",
                "animacy": "animate"
            },
            
            # SECOND DECLENSION - Feminine (ending in -я)
            "неделя": {
                "nominative": "неделя",
                "accusative": "неделю",
                "genitive": "недели",
                "dative": "неделе",
                "prepositional": "неделе",
                "nominative_plural": "недели",
                "accusative_plural": "недели",
                "genitive_plural": "недель",
                "dative_plural": "неделям",
                "prepositional_plural": "неделях",
                "declension": "second",
                "gender": "feminine"
            },
            "семья": {
                "nominative": "семья",
                "accusative": "семью",
                "genitive": "семьи",
                "dative": "семье",
                "prepositional": "семье",
                "nominative_plural": "семьи",
                "accusative_plural": "семьи",
                "genitive_plural": "семей",
                "dative_plural": "семьям",
                "prepositional_plural": "семьях",
                "declension": "second",
                "gender": "feminine"
            },
            "кухня": {
                "nominative": "кухня",
                "accusative": "кухню",
                "genitive": "кухни",
                "dative": "кухне",
                "prepositional": "кухне",
                "nominative_plural": "кухни",
                "accusative_plural": "кухни",
                "genitive_plural": "кухонь",
                "dative_plural": "кухням",
                "prepositional_plural": "кухнях",
                "declension": "second",
                "gender": "feminine"
            },
            "песня": {
                "nominative": "песня",
                "accusative": "песню",
                "genitive": "песни",
                "dative": "песне",
                "prepositional": "песне",
                "nominative_plural": "песни",
                "accusative_plural": "песни",
                "genitive_plural": "песен",
                "dative_plural": "песням",
                "prepositional_plural": "песнях",
                "declension": "second",
                "gender": "feminine"
            },
            "деревня": {
                "nominative": "деревня",
                "accusative": "деревню",
                "genitive": "деревни",
                "dative": "деревне",
                "prepositional": "деревне",
                "nominative_plural": "деревни",
                "accusative_plural": "деревни",
                "genitive_plural": "деревень",
                "dative_plural": "деревням",
                "prepositional_plural": "деревнях",
                "declension": "second",
                "gender": "feminine"
            },
            "станция": {
                "nominative": "станция",
                "accusative": "станцию",
                "genitive": "станции",
                "dative": "станции",
                "prepositional": "станции",
                "nominative_plural": "станции",
                "accusative_plural": "станции",
                "genitive_plural": "станций",
                "dative_plural": "станциям",
                "prepositional_plural": "станциях",
                "declension": "second",
                "gender": "feminine"
            },
            "лекция": {
                "nominative": "лекция",
                "accusative": "лекцию",
                "genitive": "лекции",
                "dative": "лекции",
                "prepositional": "лекции",
                "nominative_plural": "лекции",
                "accusative_plural": "лекции",
                "genitive_plural": "лекций",
                "dative_plural": "лекциям",
                "prepositional_plural": "лекциях",
                "declension": "second",
                "gender": "feminine"
            },
            
            # THIRD DECLENSION - Feminine (ending in -ь)
            "дверь": {
                "nominative": "дверь",
                "accusative": "дверь",
                "genitive": "двери",
                "dative": "двери",
                "prepositional": "двери",
                "nominative_plural": "двери",
                "accusative_plural": "двери",
                "genitive_plural": "дверей",
                "dative_plural": "дверям",
                "prepositional_plural": "дверях",
                "declension": "third",
                "gender": "feminine"
            },
            "любовь": {
                "nominative": "любовь",
                "accusative": "любовь",
                "genitive": "любви",
                "dative": "любви",
                "prepositional": "любви",
                "nominative_plural": "любови",
                "accusative_plural": "любови",
                "genitive_plural": "любовей",
                "dative_plural": "любовям",
                "prepositional_plural": "любовях",
                "declension": "third",
                "gender": "feminine"
            },
            "ночь": {
                "nominative": "ночь",
                "accusative": "ночь",
                "genitive": "ночи",
                "dative": "ночи",
                "prepositional": "ночи",
                "nominative_plural": "ночи",
                "accusative_plural": "ночи",
                "genitive_plural": "ночей",
                "dative_plural": "ночам",
                "prepositional_plural": "ночах",
                "declension": "third",
                "gender": "feminine"
            },
            "тетрадь": {
                "nominative": "тетрадь",
                "accusative": "тетрадь",
                "genitive": "тетради",
                "dative": "тетради",
                "prepositional": "тетради",
                "nominative_plural": "тетради",
                "accusative_plural": "тетради",
                "genitive_plural": "тетрадей",
                "dative_plural": "тетрадям",
                "prepositional_plural": "тетрадях",
                "declension": "third",
                "gender": "feminine"
            },
            "обувь": {
                "nominative": "обувь",
                "accusative": "обувь",
                "genitive": "обуви",
                "dative": "обуви",
                "prepositional": "обуви",
                "declension": "third",
                "gender": "feminine"
            },
            "соль": {
                "nominative": "соль",
                "accusative": "соль",
                "genitive": "соли",
                "dative": "соли",
                "prepositional": "соли",
                "nominative_plural": "соли",
                "accusative_plural": "соли",
                "genitive_plural": "солей",
                "dative_plural": "солям",
                "prepositional_plural": "солях",
                "declension": "third",
                "gender": "feminine"
            },
            "смерть": {
                "nominative": "смерть",
                "accusative": "смерть",
                "genitive": "смерти",
                "dative": "смерти",
                "prepositional": "смерти",
                "declension": "third",
                "gender": "feminine"
            }
        }
    
    def get_all_nouns(self):
        """Return all nouns with their declensions"""
        return self.nouns
    
    def get_noun(self, noun):
        """Get a specific noun's declensions"""
        return self.nouns.get(noun, None)
    
    def get_nouns_by_declension(self, declension_type):
        """Get nouns filtered by declension type (first, second, third)"""
        return {k: v for k, v in self.nouns.items() if v.get('declension') == declension_type}
    
    def get_nouns_by_gender(self, gender):
        """Get nouns filtered by gender"""
        return {k: v for k, v in self.nouns.items() if v.get('gender') == gender}
    
    def get_nouns_with_plurals(self):
        """Get only nouns that have plural forms defined"""
        return {k: v for k, v in self.nouns.items() if 'nominative_plural' in v}
    
    def get_declension_info(self):
        """Return information about Russian declension patterns"""
        return {
            "first": {
                "description": "1. deklinasjon",
                "types": [
                    "Masculine nouns: ending in consonant or -й (дом, трамвай)",
                    "Neuter nouns: ending in -о/-е (окно, море)"
                ],
                "endings": {
                    "nominative": "-/consonant (masc), -о/-е (neut)",
                    "accusative": "= Nominative (inanimate), -а/-я (animate)",
                    "genitive": "-а/-я",
                    "dative": "-у/-ю",
                    "prepositional": "-е"
                },
                "plural_endings": {
                    "nominative": "-ы/-и (masc), -а/-я (neut)",
                    "accusative": "= Nominative (inanimate), = Genitive (animate)",
                    "genitive": "-ов/-ев/-ей",
                    "dative": "-ам/-ям",
                    "prepositional": "-ах/-ях"
                },
                "example_masculine": "дом → дома (gen.sing), дома (nom.pl)",
                "example_neuter": "окно → окна (gen.sing), окна (nom.pl)"
            },
            "second": {
                "description": "2. deklinasjon",
                "types": [
                    "Feminine nouns: ending in -а/-я (книга, неделя)"
                ],
                "endings": {
                    "nominative": "-а/-я",
                    "accusative": "-у/-ю",
                    "genitive": "-ы/-и",
                    "dative": "-е (-и)",
                    "prepositional": "-е (-и)"
                },
                "plural_endings": {
                    "nominative": "-ы/-и",
                    "accusative": "= Nominative (inanimate), = Genitive (animate)",
                    "genitive": "- (zero ending) / -ь / -ей",
                    "dative": "-ам/-ям",
                    "prepositional": "-ах/-ях"
                },
                "example": "книга → книги (gen.sing), книги (nom.pl), книг (gen.pl)"
            },
            "third": {
                "description": "3. deklinasjon",
                "types": [
                    "Feminine nouns: ending in -ь (дверь, ночь, любовь)"
                ],
                "endings": {
                    "nominative": "-ь",
                    "accusative": "= Nominative",
                    "genitive": "-и",
                    "dative": "-и",
                    "prepositional": "-и"
                },
                "plural_endings": {
                    "nominative": "-и",
                    "accusative": "= Nominative",
                    "genitive": "-ей",
                    "dative": "-ям",
                    "prepositional": "-ях"
                },
                "example": "дверь → двери (gen.sing), двери (nom.pl), дверей (gen.pl)"
            }
        }