class WordPairDatabase:
    """Database of adjective-noun pairs for realistic Russian practice with full case agreement"""
    
    def __init__(self):
        # Use base form (masculine nominative) for adjective keys
        self.pairs = {
            # MASCULINE NOUNS - Common exam vocabulary
            "новый дом": {
                "adjective": "новый",  # Base form
                "noun": "дом",
                "gender": "masculine",
                "animacy": "inanimate",
                "translation": "new house",
                "category": "places"
            },
            "большой город": {
                "adjective": "большой",  # Base form
                "noun": "город",
                "gender": "masculine",
                "animacy": "inanimate",
                "translation": "big city",
                "category": "places"
            },
            "вкусный салат": {
                "adjective": "вкусный",  # Base form
                "noun": "салат",
                "gender": "masculine",
                "animacy": "inanimate",
                "translation": "tasty salad",
                "category": "food"
            },
            "хороший друг": {
                "adjective": "хороший",  # Base form
                "noun": "друг",
                "gender": "masculine",
                "animacy": "animate",
                "translation": "good friend",
                "category": "people"
            },
            "русский язык": {
                "adjective": "русский",  # Base form
                "noun": "язык",
                "gender": "masculine",
                "animacy": "inanimate",
                "translation": "Russian language",
                "category": "education"
            },
            "спортивный центр": {
                "adjective": "спортивный",  # Base form
                "noun": "центр",
                "gender": "masculine",
                "animacy": "inanimate",
                "translation": "sports center",
                "category": "places"
            },
            "маленький мальчик": {
                "adjective": "маленький",  # Base form
                "noun": "мальчик",
                "gender": "masculine",
                "animacy": "animate",
                "translation": "little boy",
                "category": "people"
            },
            
            # FEMININE NOUNS - Use base form of adjective
            "большая тарелка": {
                "adjective": "большой",  # Base form (not большая)
                "noun": "тарелка",
                "gender": "feminine",
                "animacy": "inanimate",
                "translation": "big plate",
                "category": "objects"
            },
            "красивая книга": {
                "adjective": "красивый",  # Base form (not красивая)
                "noun": "книга",
                "gender": "feminine",
                "animacy": "inanimate",
                "translation": "beautiful book",
                "category": "objects"
            },
            "новая машина": {
                "adjective": "новый",  # Base form (not новая)
                "noun": "машина",
                "gender": "feminine",
                "animacy": "inanimate",
                "translation": "new car",
                "category": "transport"
            },
            "музыкальная школа": {
                "adjective": "музыкальный",  # Base form (not музыкальная)
                "noun": "школа",
                "gender": "feminine",
                "animacy": "inanimate",
                "translation": "music school",
                "category": "education"
            },
            "вкусная еда": {
                "adjective": "вкусный",  # Base form (not вкусная)
                "noun": "еда",
                "gender": "feminine",
                "animacy": "inanimate",
                "translation": "tasty food",
                "category": "food"
            },
            "хорошая соседка": {
                "adjective": "хороший",  # Base form (not хорошая)
                "noun": "соседка",
                "gender": "feminine",
                "animacy": "animate",
                "translation": "good neighbor (female)",
                "category": "people"
            },
            "маленькая девочка": {
                "adjective": "маленький",  # Base form (not маленькая)
                "noun": "девочка",
                "gender": "feminine",
                "animacy": "animate",
                "translation": "little girl",
                "category": "people"
            },
            "молодая пенсионерка": {
                "adjective": "молодой",  # Base form (not молодая)
                "noun": "пенсионерка",
                "gender": "feminine",
                "animacy": "animate",
                "translation": "young retiree (female)",
                "category": "people"
            },
            
            # NEUTER NOUNS - Use base form of adjective
            "красное мясо": {
                "adjective": "красный",  # Base form (not красное)
                "noun": "мясо",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "red meat",
                "category": "food"
            },
            "белое вино": {
                "adjective": "белый",  # Base form (not белое)
                "noun": "вино",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "white wine",
                "category": "food"
            },
            "старое окно": {
                "adjective": "старый",  # Base form (not старое)
                "noun": "окно",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "old window",
                "category": "objects"
            },
            "новое слово": {
                "adjective": "новый",  # Base form (not новое)
                "noun": "слово",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "new word",
                "category": "language"
            },
            "синее море": {
                "adjective": "синий",  # Base form (not синее)
                "noun": "море",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "blue sea",
                "category": "nature"
            },
            "маленькое окно": {
                "adjective": "маленький",  # Base form (not маленькое)
                "noun": "окно",
                "gender": "neuter",
                "animacy": "inanimate",
                "translation": "little window",
                "category": "objects"
            }
        }
    
    def get_all_pairs(self):
        """Return all word pairs"""
        return self.pairs
    
    def get_pair(self, pair_name):
        """Get a specific word pair"""
        return self.pairs.get(pair_name, None)
    
    def get_pairs_by_gender(self, gender):
        """Get all pairs of a specific gender"""
        return {k: v for k, v in self.pairs.items() if v['gender'] == gender}
    
    def get_pairs_by_animacy(self, animacy):
        """Get all pairs by animacy (for testing animate/inanimate rules)"""
        return {k: v for k, v in self.pairs.items() if v['animacy'] == animacy}
    
    def add_pair(self, pair_name, adjective, noun, gender, animacy, translation):
        """Add a new word pair"""
        self.pairs[pair_name] = {
            "adjective": adjective,
            "noun": noun,
            "gender": gender,
            "animacy": animacy,
            "translation": translation
        }
    
    def generate_declension_example(self, pair_name, case, adj_db, noun_db):
        """
        Generate a complete declension example showing agreement between adjective and noun
        Returns: (declined_adjective, declined_noun, explanation)
        """
        if pair_name not in self.pairs:
            return None, None, None
        
        pair_info = self.pairs[pair_name]
        adjective = pair_info['adjective']
        noun = pair_info['noun']
        gender = pair_info['gender']
        
        # Get the declined forms
        if adjective in adj_db and noun in noun_db:
            adj_forms = adj_db[adjective]
            noun_forms = noun_db[noun]
            
            if gender in adj_forms and case in adj_forms[gender]:
                declined_adj = adj_forms[gender][case]
            else:
                return None, None, None
            
            if case in noun_forms:
                declined_noun = noun_forms[case]
            else:
                return None, None, None
            
            # Create explanation based on case
            case_explanations = {
                "nominative": f"Subject or predicative: The {pair_info['translation']} is/are...",
                "accusative": f"Direct object: I see the {pair_info['translation']}",
                "genitive": f"Possession/absence: of the {pair_info['translation']}, without the {pair_info['translation']}",
                "dative": f"Indirect object: to/for the {pair_info['translation']}",
                "prepositional": f"Location/topic: in/at/about the {pair_info['translation']}"
            }
            
            explanation = case_explanations.get(case, "")
            
            return declined_adj, declined_noun, explanation
        
        return None, None, None
    
    def get_pairs_by_category(self, category):
        """Get all pairs of a specific category"""
        return {k: v for k, v in self.pairs.items() if v.get('category') == category}