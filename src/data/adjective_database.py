class AdjectiveDatabase:
    def __init__(self):
        self.adjectives = {
            # HARD STEM -ый adjectives
            "новый": {
                "masculine": {
                    "nominative": "новый",
                    "accusative": "новый",  # inanimate
                    "genitive": "нового",
                    "dative": "новому",
                    "prepositional": "новом"
                },
                "feminine": {
                    "nominative": "новая",
                    "accusative": "новую",
                    "genitive": "новой",
                    "dative": "новой",
                    "prepositional": "новой"
                },
                "neuter": {
                    "nominative": "новое",
                    "accusative": "новое",
                    "genitive": "нового",
                    "dative": "новому",
                    "prepositional": "новом"
                }
            },
            "красивый": {
                "masculine": {
                    "nominative": "красивый",
                    "accusative": "красивый",
                    "genitive": "красивого",
                    "dative": "красивому",
                    "prepositional": "красивом"
                },
                "feminine": {
                    "nominative": "красивая",
                    "accusative": "красивую",
                    "genitive": "красивой",
                    "dative": "красивой",
                    "prepositional": "красивой"
                },
                "neuter": {
                    "nominative": "красивое",
                    "accusative": "красивое",
                    "genitive": "красивого",
                    "dative": "красивому",
                    "prepositional": "красивом"
                }
            },
            "старый": {
                "masculine": {
                    "nominative": "старый",
                    "accusative": "старый",
                    "genitive": "старого",
                    "dative": "старому",
                    "prepositional": "старом"
                },
                "feminine": {
                    "nominative": "старая",
                    "accusative": "старую",
                    "genitive": "старой",
                    "dative": "старой",
                    "prepositional": "старой"
                },
                "neuter": {
                    "nominative": "старое",
                    "accusative": "старое",
                    "genitive": "старого",
                    "dative": "старому",
                    "prepositional": "старом"
                }
            },
            "белый": {
                "masculine": {
                    "nominative": "белый",
                    "accusative": "белый",
                    "genitive": "белого",
                    "dative": "белому",
                    "prepositional": "белом"
                },
                "feminine": {
                    "nominative": "белая",
                    "accusative": "белую",
                    "genitive": "белой",
                    "dative": "белой",
                    "prepositional": "белой"
                },
                "neuter": {
                    "nominative": "белое",
                    "accusative": "белое",
                    "genitive": "белого",
                    "dative": "белому",
                    "prepositional": "белом"
                }
            },
            "красный": {
                "masculine": {
                    "nominative": "красный",
                    "accusative": "красный",
                    "genitive": "красного",
                    "dative": "красному",
                    "prepositional": "красном"
                },
                "feminine": {
                    "nominative": "красная",
                    "accusative": "красную",
                    "genitive": "красной",
                    "dative": "красной",
                    "prepositional": "красной"
                },
                "neuter": {
                    "nominative": "красное",
                    "accusative": "красное",
                    "genitive": "красного",
                    "dative": "красному",
                    "prepositional": "красном"
                }
            },
            
            # STRESSED -ой adjectives
            "большой": {
                "masculine": {
                    "nominative": "большой",
                    "accusative": "большой",
                    "genitive": "большого",
                    "dative": "большому",
                    "prepositional": "большом"
                },
                "feminine": {
                    "nominative": "большая",
                    "accusative": "большую",
                    "genitive": "большой",
                    "dative": "большой",
                    "prepositional": "большой"
                },
                "neuter": {
                    "nominative": "большое",
                    "accusative": "большое",
                    "genitive": "большого",
                    "dative": "большому",
                    "prepositional": "большом"
                }
            },
            "молодой": {
                "masculine": {
                    "nominative": "молодой",
                    "accusative": "молодой",
                    "genitive": "молодого",
                    "dative": "молодому",
                    "prepositional": "молодом"
                },
                "feminine": {
                    "nominative": "молодая",
                    "accusative": "молодую",
                    "genitive": "молодой",
                    "dative": "молодой",
                    "prepositional": "молодой"
                },
                "neuter": {
                    "nominative": "молодое",
                    "accusative": "молодое",
                    "genitive": "молодого",
                    "dative": "молодому",
                    "prepositional": "молодом"
                }
            },
            "дорогой": {
                "masculine": {
                    "nominative": "дорогой",
                    "accusative": "дорогой",
                    "genitive": "дорогого",
                    "dative": "дорогому",
                    "prepositional": "дорогом"
                },
                "feminine": {
                    "nominative": "дорогая",
                    "accusative": "дорогую",
                    "genitive": "дорогой",
                    "dative": "дорогой",
                    "prepositional": "дорогой"
                },
                "neuter": {
                    "nominative": "дорогое",
                    "accusative": "дорогое",
                    "genitive": "дорогого",
                    "dative": "дорогому",
                    "prepositional": "дорогом"
                }
            },
            
            # SOFT STEM -ий adjectives
            "хороший": {
                "masculine": {
                    "nominative": "хороший",
                    "accusative": "хороший",
                    "genitive": "хорошего",
                    "dative": "хорошему",
                    "prepositional": "хорошем"
                },
                "feminine": {
                    "nominative": "хорошая",
                    "accusative": "хорошую",
                    "genitive": "хорошей",
                    "dative": "хорошей",
                    "prepositional": "хорошей"
                },
                "neuter": {
                    "nominative": "хорошее",
                    "accusative": "хорошее",
                    "genitive": "хорошего",
                    "dative": "хорошему",
                    "prepositional": "хорошем"
                }
            },
            "синий": {
                "masculine": {
                    "nominative": "синий",
                    "accusative": "синий",
                    "genitive": "синего",
                    "dative": "синему",
                    "prepositional": "синем"
                },
                "feminine": {
                    "nominative": "синяя",
                    "accusative": "синюю",
                    "genitive": "синей",
                    "dative": "синей",
                    "prepositional": "синей"
                },
                "neuter": {
                    "nominative": "синее",
                    "accusative": "синее",
                    "genitive": "синего",
                    "dative": "синему",
                    "prepositional": "синем"
                }
            },
            "маленький": {
                "masculine": {
                    "nominative": "маленький",
                    "accusative": "маленький",
                    "genitive": "маленького",
                    "dative": "маленькому",
                    "prepositional": "маленьком"
                },
                "feminine": {
                    "nominative": "маленькая",
                    "accusative": "маленькую",
                    "genitive": "маленькой",
                    "dative": "маленькой",
                    "prepositional": "маленькой"
                },
                "neuter": {
                    "nominative": "маленькое",
                    "accusative": "маленькое",
                    "genitive": "маленького",
                    "dative": "маленькому",
                    "prepositional": "маленьком"
                }
            },
            "русский": {
                "masculine": {
                    "nominative": "русский",
                    "accusative": "русский",
                    "genitive": "русского",
                    "dative": "русскому",
                    "prepositional": "русском"
                },
                "feminine": {
                    "nominative": "русская",
                    "accusative": "русскую",
                    "genitive": "русской",
                    "dative": "русской",
                    "prepositional": "русской"
                },
                "neuter": {
                    "nominative": "русское",
                    "accusative": "русское",
                    "genitive": "русского",
                    "dative": "русскому",
                    "prepositional": "русском"
                }
            },
            "вкусный": {
                "masculine": {
                    "nominative": "вкусный",
                    "accusative": "вкусный",
                    "genitive": "вкусного",
                    "dative": "вкусному",
                    "prepositional": "вкусном"
                },
                "feminine": {
                    "nominative": "вкусная",
                    "accusative": "вкусную",
                    "genitive": "вкусной",
                    "dative": "вкусной",
                    "prepositional": "вкусной"
                },
                "neuter": {
                    "nominative": "вкусное",
                    "accusative": "вкусное",
                    "genitive": "вкусного",
                    "dative": "вкусному",
                    "prepositional": "вкусном"
                }
            },
            "спортивный": {
                "masculine": {
                    "nominative": "спортивный",
                    "accusative": "спортивный",
                    "genitive": "спортивного",
                    "dative": "спортивному",
                    "prepositional": "спортивном"
                },
                "feminine": {
                    "nominative": "спортивная",
                    "accusative": "спортивную",
                    "genitive": "спортивной",
                    "dative": "спортивной",
                    "prepositional": "спортивной"
                },
                "neuter": {
                    "nominative": "спортивное",
                    "accusative": "спортивное",
                    "genitive": "спортивного",
                    "dative": "спортивному",
                    "prepositional": "спортивном"
                }
            },
            "музыкальный": {
                "masculine": {
                    "nominative": "музыкальный",
                    "accusative": "музыкальный",
                    "genitive": "музыкального",
                    "dative": "музыкальному",
                    "prepositional": "музыкальном"
                },
                "feminine": {
                    "nominative": "музыкальная",
                    "accusative": "музыкальную",
                    "genitive": "музыкальной",
                    "dative": "музыкальной",
                    "prepositional": "музыкальной"
                },
                "neuter": {
                    "nominative": "музыкальное",
                    "accusative": "музыкальное",
                    "genitive": "музыкального",
                    "dative": "музыкальному",
                    "prepositional": "музыкальном"
                }
            }
        }
    
    def get_all_adjectives(self):
        """Return all adjectives with their declensions"""
        return self.adjectives
    
    def get_adjective(self, adjective):
        """Get a specific adjective's declensions"""
        return self.adjectives.get(adjective, None)