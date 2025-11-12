class PronounDatabase:
    def __init__(self):
        self.pronouns = {
            "я": {
                "nominative": "я",
                "accusative": "меня́",
                "genitive": "меня́",
                "dative": "мне",
                "instrumental": "мной",
                "prepositional": "мне"
            },
            "ты": {
                "nominative": "ты́",
                "accusative": "тебя́",
                "genitive": "тебя́",
                "dative": "тебе́",
                "instrumental": "тобой",
                "prepositional": "тебе́"
            },
            "он": {
                "nominative": "он",
                "accusative": "(н)его́",
                "genitive": "(н)его́",
                "dative": "(н)ему́",
                "instrumental": "н(им)",
                "prepositional": "нём"
            },
            "она": {
                "nominative": "она́",
                "accusative": "(н)её",
                "genitive": "(н)её",
                "dative": "(н)ей",
                "instrumental": "(н)ей",
                "prepositional": "ней"
            },
            "мы": {
                "nominative": "мы",
                "accusative": "нас",
                "genitive": "нас",
                "dative": "нам",
                "instrumental": "на́ми",
                "prepositional": "нас"
            },
            "вы": {
                "nominative": "вы",
                "accusative": "вас",
                "genitive": "вас",
                "dative": "вам",
                "instrumental": "ва́ми",
                "prepositional": "вас"
            },
            "они": {
                "nominative": "они́",
                "accusative": "(н)их",
                "genitive": "(н)их",
                "dative": "(н)им",
                "instrumental": "(н)и́ми",
                "prepositional": "них"
            }
        }
    
    def get_all_pronouns(self):
        """Return all pronouns in the database"""
        return self.pronouns
    
    def get_pronoun(self, word):
        """Get declensions for a specific pronoun"""
        return self.pronouns.get(word, None)
    
    def add_pronoun(self, word, declensions):
        """Add a new pronoun to the database"""
        self.pronouns[word] = declensions