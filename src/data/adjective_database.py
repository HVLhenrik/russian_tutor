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
                },
                "plural": {
                    "nominative": "новые",
                    "accusative": "новые",  # inanimate
                    "genitive": "новых",
                    "dative": "новым",
                    "prepositional": "новых"
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
                },
                "plural": {
                    "nominative": "красивые",
                    "accusative": "красивые",
                    "genitive": "красивых",
                    "dative": "красивым",
                    "prepositional": "красивых"
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
                },
                "plural": {
                    "nominative": "старые",
                    "accusative": "старые",
                    "genitive": "старых",
                    "dative": "старым",
                    "prepositional": "старых"
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
                },
                "plural": {
                    "nominative": "белые",
                    "accusative": "белые",
                    "genitive": "белых",
                    "dative": "белым",
                    "prepositional": "белых"
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
                },
                "plural": {
                    "nominative": "красные",
                    "accusative": "красные",
                    "genitive": "красивых",
                    "dative": "красным",
                    "prepositional": "красных"
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
                },
                "plural": {
                    "nominative": "большие",
                    "accusative": "большие",
                    "genitive": "больших",
                    "dative": "большим",
                    "prepositional": "больших"
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
                },
                "plural": {
                    "nominative": "молодые",
                    "accusative": "молодые",
                    "genitive": "молодых",
                    "dative": "молодым",
                    "prepositional": "молодых"
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
                },
                "plural": {
                    "nominative": "дорогие",
                    "accusative": "дорогие",
                    "genitive": "дорогих",
                    "dative": "дорогим",
                    "prepositional": "дорогих"
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
                },
                "plural": {
                    "nominative": "хорошие",
                    "accusative": "хорошие",
                    "genitive": "хороших",
                    "dative": "хорошим",
                    "prepositional": "хороших"
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
                },
                "plural": {
                    "nominative": "синие",
                    "accusative": "синие",
                    "genitive": "синих",
                    "dative": "синим",
                    "prepositional": "синих"
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
                },
                "plural": {
                    "nominative": "маленькие",
                    "accusative": "маленькие",
                    "genitive": "маленьких",
                    "dative": "маленьким",
                    "prepositional": "маленьких"
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
                },
                "plural": {
                    "nominative": "русские",
                    "accusative": "русские",
                    "genitive": "русских",
                    "dative": "русским",
                    "prepositional": "русских"
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
                },
                "plural": {
                    "nominative": "вкусные",
                    "accusative": "вкусные",
                    "genitive": "вкусных",
                    "dative": "вкусным",
                    "prepositional": "вкусных"
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
                },
                "plural": {
                    "nominative": "спортивные",
                    "accusative": "спортивные",
                    "genitive": "спортивных",
                    "dative": "спортивным",
                    "prepositional": "спортивных"
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
                },
                "plural": {
                    "nominative": "музыкальные",
                    "accusative": "музыкальные",
                    "genitive": "музыкальных",
                    "dative": "музыкальным",
                    "prepositional": "музыкальных"
                }
            }
        }
    
    def get_all_adjectives(self):
        """Return all adjectives with their declensions"""
        return self.adjectives
    
    def get_adjective(self, adjective):
        """Get a specific adjective's declensions"""
        return self.adjectives.get(adjective, None)