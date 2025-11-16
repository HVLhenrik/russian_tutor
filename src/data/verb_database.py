"""
Russian Verb Database
Contains full conjugation patterns for verbs from SMARTool_data_A1.csv
"""
import os

class VerbDatabase:
    """Database for Russian verb conjugations with aspect information"""
    
    def __init__(self):
        # Load irregular verbs from file
        self.irregular_verbs = self._load_irregular_verbs()
        
        # Full verb conjugation database
        self.verbs = self._initialize_verbs()
    
    def _load_irregular_verbs(self) -> set:
        """Load list of irregular verbs from file"""
        irregular_file = os.path.join(
            os.path.dirname(__file__), 
            '..', 
            '..', 
            'irregular_verbs.txt'
        )
        
        irregular = set()
        try:
            with open(irregular_file, 'r', encoding='utf-8') as f:
                for line in f:
                    verb = line.strip()
                    if verb and not verb.startswith('#'):
                        irregular.add(verb)
        except FileNotFoundError:
            print(f"⚠️  Warning: irregular_verbs.txt not found")
        
        return irregular
    
    def _initialize_verbs(self) -> dict:
        """Initialize verb database with A1 verbs from SMARTool data"""
        return {
            # ============ IRREGULAR VERBS (11 exceptions) ============
            'гнать': {
                'translation': 'drive, chase',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'гоню',
                    'ты': 'гонишь',
                    'он': 'гонит',
                    'мы': 'гоним',
                    'вы': 'гоните',
                    'они': 'гонят'
                },
                'past': {
                    'masculine': 'гнал',
                    'feminine': 'гнала',
                    'neuter': 'гнало',
                    'plural': 'гнали'
                }
            },
            'держать': {
                'translation': 'hold, keep',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'держу',
                    'ты': 'держишь',
                    'он': 'держит',
                    'мы': 'держим',
                    'вы': 'держите',
                    'они': 'держат'
                },
                'past': {
                    'masculine': 'держал',
                    'feminine': 'держала',
                    'neuter': 'держало',
                    'plural': 'держали'
                }
            },
            'дышать': {
                'translation': 'breathe',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'дышу',
                    'ты': 'дышишь',
                    'он': 'дышит',
                    'мы': 'дышим',
                    'вы': 'дышите',
                    'они': 'дышат'
                },
                'past': {
                    'masculine': 'дышал',
                    'feminine': 'дышала',
                    'neuter': 'дышало',
                    'plural': 'дышали'
                }
            },
            'слышать': {
                'translation': 'hear',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'слышу',
                    'ты': 'слышишь',
                    'он': 'слышит',
                    'мы': 'слышим',
                    'вы': 'слышите',
                    'они': 'слышат'
                },
                'past': {
                    'masculine': 'слышал',
                    'feminine': 'слышала',
                    'neuter': 'слышало',
                    'plural': 'слышали'
                }
            },
            'смотреть': {
                'translation': 'watch, look',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'смотрю',
                    'ты': 'смотришь',
                    'он': 'смотрит',
                    'мы': 'смотрим',
                    'вы': 'смотрите',
                    'они': 'смотрят'
                },
                'past': {
                    'masculine': 'смотрел',
                    'feminine': 'смотрела',
                    'neuter': 'смотрело',
                    'plural': 'смотрели'
                }
            },
            'видеть': {
                'translation': 'see',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'вижу',
                    'ты': 'видишь',
                    'он': 'видит',
                    'мы': 'видим',
                    'вы': 'видите',
                    'они': 'видят'
                },
                'past': {
                    'masculine': 'видел',
                    'feminine': 'видела',
                    'neuter': 'видело',
                    'plural': 'видели'
                }
            },
            'ненавидеть': {
                'translation': 'hate',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'ненавижу',
                    'ты': 'ненавидишь',
                    'он': 'ненавидит',
                    'мы': 'ненавидим',
                    'вы': 'ненавидите',
                    'они': 'ненавидят'
                },
                'past': {
                    'masculine': 'ненавидел',
                    'feminine': 'ненавидела',
                    'neuter': 'ненавидело',
                    'plural': 'ненавидели'
                }
            },
            'зависеть': {
                'translation': 'depend',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'завишу',
                    'ты': 'зависишь',
                    'он': 'зависит',
                    'мы': 'зависим',
                    'вы': 'зависите',
                    'они': 'зависят'
                },
                'past': {
                    'masculine': 'зависел',
                    'feminine': 'зависела',
                    'neuter': 'зависело',
                    'plural': 'зависели'
                }
            },
            'вертеть': {
                'translation': 'turn, spin',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'верчу',
                    'ты': 'вертишь',
                    'он': 'вертит',
                    'мы': 'вертим',
                    'вы': 'вертите',
                    'они': 'вертят'
                },
                'past': {
                    'masculine': 'вертел',
                    'feminine': 'вертела',
                    'neuter': 'вертело',
                    'plural': 'вертели'
                }
            },
            'обидеть': {
                'translation': 'offend, hurt',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': True,
                'future': {
                    'я': 'обижу',
                    'ты': 'обидишь',
                    'он': 'обидит',
                    'мы': 'обидим',
                    'вы': 'обидите',
                    'они': 'обидят'
                },
                'past': {
                    'masculine': 'обидел',
                    'feminine': 'обидела',
                    'neuter': 'обидело',
                    'plural': 'обидели'
                }
            },
            'терпеть': {
                'translation': 'endure, tolerate',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': True,
                'present': {
                    'я': 'терплю',
                    'ты': 'терпишь',
                    'он': 'терпит',
                    'мы': 'терпим',
                    'вы': 'терпите',
                    'они': 'терпят'
                },
                'past': {
                    'masculine': 'терпел',
                    'feminine': 'терпела',
                    'neuter': 'терпело',
                    'plural': 'терпели'
                }
            },
            
            # ============ COMMON A1 VERBS ============
            'работать': {
                'translation': 'work',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'работаю',
                    'ты': 'работаешь',
                    'он': 'работает',
                    'мы': 'работаем',
                    'вы': 'работаете',
                    'они': 'работают'
                },
                'past': {
                    'masculine': 'работал',
                    'feminine': 'работала',
                    'neuter': 'работало',
                    'plural': 'работали'
                }
            },
            'понравиться': {
                'translation': 'please, be liked',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'понравлюсь',
                    'ты': 'понравишься',
                    'он': 'понравится',
                    'мы': 'понравимся',
                    'вы': 'понравитесь',
                    'они': 'понравятся'
                },
                'past': {
                    'masculine': 'понравился',
                    'feminine': 'понравилась',
                    'neuter': 'понравилось',
                    'plural': 'понравились'
                }
            },
            'пообедать': {
                'translation': 'have lunch',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'пообедаю',
                    'ты': 'пообедаешь',
                    'он': 'пообедает',
                    'мы': 'пообедаем',
                    'вы': 'пообедаете',
                    'они': 'пообедают'
                },
                'past': {
                    'masculine': 'пообедал',
                    'feminine': 'пообедала',
                    'neuter': 'пообедало',
                    'plural': 'пообедали'
                }
            },
            'хотеть': {
                'translation': 'want',
                'aspect': 'imperfective',
                'conjugation': 'mixed',
                'irregular': True,
                'present': {
                    'я': 'хочу',
                    'ты': 'хочешь',
                    'он': 'хочет',
                    'мы': 'хотим',
                    'вы': 'хотите',
                    'они': 'хотят'
                },
                'past': {
                    'masculine': 'хотел',
                    'feminine': 'хотела',
                    'neuter': 'хотело',
                    'plural': 'хотели'
                }
            },
            'посмотреть': {
                'translation': 'watch, look',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'посмотрю',
                    'ты': 'посмотришь',
                    'он': 'посмотрит',
                    'мы': 'посмотрим',
                    'вы': 'посмотрите',
                    'они': 'посмотрят'
                },
                'past': {
                    'masculine': 'посмотрел',
                    'feminine': 'посмотрела',
                    'neuter': 'посмотрело',
                    'plural': 'посмотрели'
                }
            },
            'попросить': {
                'translation': 'ask for',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'попрошу',
                    'ты': 'попросишь',
                    'он': 'попросит',
                    'мы': 'попросим',
                    'вы': 'попросите',
                    'они': 'попросят'
                },
                'past': {
                    'masculine': 'попросил',
                    'feminine': 'попросила',
                    'neuter': 'попросило',
                    'plural': 'попросили'
                }
            },
            'встречать': {
                'translation': 'meet',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'встречаю',
                    'ты': 'встречаешь',
                    'он': 'встречает',
                    'мы': 'встречаем',
                    'вы': 'встречаете',
                    'они': 'встречают'
                },
                'past': {
                    'masculine': 'встречал',
                    'feminine': 'встречала',
                    'neuter': 'встречало',
                    'plural': 'встречали'
                }
            },
            'брать': {
                'translation': 'take',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'беру',
                    'ты': 'берёшь',
                    'он': 'берёт',
                    'мы': 'берём',
                    'вы': 'берёте',
                    'они': 'берут'
                },
                'past': {
                    'masculine': 'брал',
                    'feminine': 'брала',
                    'neuter': 'брало',
                    'plural': 'брали'
                }
            },
            'взять': {
                'translation': 'take',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'возьму',
                    'ты': 'возьмёшь',
                    'он': 'возьмёт',
                    'мы': 'возьмём',
                    'вы': 'возьмёте',
                    'они': 'возьмут'
                },
                'past': {
                    'masculine': 'взял',
                    'feminine': 'взяла',
                    'neuter': 'взяло',
                    'plural': 'взяли'
                }
            },
            'говорить': {
                'translation': 'speak, talk',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'говорю',
                    'ты': 'говоришь',
                    'он': 'говорит',
                    'мы': 'говорим',
                    'вы': 'говорите',
                    'они': 'говорят'
                },
                'past': {
                    'masculine': 'говорил',
                    'feminine': 'говорила',
                    'neuter': 'говорило',
                    'plural': 'говорили'
                }
            },
            'гулять': {
                'translation': 'walk, stroll',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'гуляю',
                    'ты': 'гуляешь',
                    'он': 'гуляет',
                    'мы': 'гуляем',
                    'вы': 'гуляете',
                    'они': 'гуляют'
                },
                'past': {
                    'masculine': 'гулял',
                    'feminine': 'гуляла',
                    'neuter': 'гуляло',
                    'plural': 'гуляли'
                }
            },
            'давать': {
                'translation': 'give',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'даю',
                    'ты': 'даёшь',
                    'он': 'даёт',
                    'мы': 'даём',
                    'вы': 'даёте',
                    'они': 'дают'
                },
                'past': {
                    'masculine': 'давал',
                    'feminine': 'давала',
                    'neuter': 'давало',
                    'plural': 'давали'
                }
            },
            'дарить': {
                'translation': 'give (a gift)',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'дарю',
                    'ты': 'даришь',
                    'он': 'дарит',
                    'мы': 'дарим',
                    'вы': 'дарите',
                    'они': 'дарят'
                },
                'past': {
                    'masculine': 'дарил',
                    'feminine': 'дарила',
                    'neuter': 'дарило',
                    'plural': 'дарили'
                }
            },
            'делать': {
                'translation': 'do, make',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'делаю',
                    'ты': 'делаешь',
                    'он': 'делает',
                    'мы': 'делаем',
                    'вы': 'делаете',
                    'они': 'делают'
                },
                'past': {
                    'masculine': 'делал',
                    'feminine': 'делала',
                    'neuter': 'делало',
                    'plural': 'делали'
                }
            },
            'думать': {
                'translation': 'think',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'думаю',
                    'ты': 'думаешь',
                    'он': 'думает',
                    'мы': 'думаем',
                    'вы': 'думаете',
                    'они': 'думают'
                },
                'past': {
                    'masculine': 'думал',
                    'feminine': 'думала',
                    'neuter': 'думало',
                    'plural': 'думали'
                }
            },
            'ездить': {
                'translation': 'go (by vehicle), travel',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'езжу',
                    'ты': 'ездишь',
                    'он': 'ездит',
                    'мы': 'ездим',
                    'вы': 'ездите',
                    'они': 'ездят'
                },
                'past': {
                    'masculine': 'ездил',
                    'feminine': 'ездила',
                    'neuter': 'ездило',
                    'plural': 'ездили'
                }
            },
            'ехать': {
                'translation': 'go (by vehicle)',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'еду',
                    'ты': 'едешь',
                    'он': 'едет',
                    'мы': 'едем',
                    'вы': 'едете',
                    'они': 'едут'
                },
                'past': {
                    'masculine': 'ехал',
                    'feminine': 'ехала',
                    'neuter': 'ехало',
                    'plural': 'ехали'
                }
            },
            'ждать': {
                'translation': 'wait',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'жду',
                    'ты': 'ждёшь',
                    'он': 'ждёт',
                    'мы': 'ждём',
                    'вы': 'ждёте',
                    'они': 'ждут'
                },
                'past': {
                    'masculine': 'ждал',
                    'feminine': 'ждала',
                    'neuter': 'ждало',
                    'plural': 'ждали'
                }
            },
            'жить': {
                'translation': 'live',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'живу',
                    'ты': 'живёшь',
                    'он': 'живёт',
                    'мы': 'живём',
                    'вы': 'живёте',
                    'они': 'живут'
                },
                'past': {
                    'masculine': 'жил',
                    'feminine': 'жила',
                    'neuter': 'жило',
                    'plural': 'жили'
                }
            },
            'завтракать': {
                'translation': 'have breakfast',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'завтракаю',
                    'ты': 'завтракаешь',
                    'он': 'завтракает',
                    'мы': 'завтракаем',
                    'вы': 'завтракаете',
                    'они': 'завтракают'
                },
                'past': {
                    'masculine': 'завтракал',
                    'feminine': 'завтракала',
                    'neuter': 'завтракало',
                    'plural': 'завтракали'
                }
            },
            'звонить': {
                'translation': 'call, ring',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'звоню',
                    'ты': 'звонишь',
                    'он': 'звонит',
                    'мы': 'звоним',
                    'вы': 'звоните',
                    'они': 'звонят'
                },
                'past': {
                    'masculine': 'звонил',
                    'feminine': 'звонила',
                    'neuter': 'звонило',
                    'plural': 'звонили'
                }
            },
            'знать': {
                'translation': 'know',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'знаю',
                    'ты': 'знаешь',
                    'он': 'знает',
                    'мы': 'знаем',
                    'вы': 'знаете',
                    'они': 'знают'
                },
                'past': {
                    'masculine': 'знал',
                    'feminine': 'знала',
                    'neuter': 'знало',
                    'plural': 'знали'
                }
            },
            'играть': {
                'translation': 'play',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'играю',
                    'ты': 'играешь',
                    'он': 'играет',
                    'мы': 'играем',
                    'вы': 'играете',
                    'они': 'играют'
                },
                'past': {
                    'masculine': 'играл',
                    'feminine': 'играла',
                    'neuter': 'играло',
                    'plural': 'играли'
                }
            },
            'идти': {
                'translation': 'go (on foot)',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': True,
                'present': {
                    'я': 'иду',
                    'ты': 'идёшь',
                    'он': 'идёт',
                    'мы': 'идём',
                    'вы': 'идёте',
                    'они': 'идут'
                },
                'past': {
                    'masculine': 'шёл',
                    'feminine': 'шла',
                    'neuter': 'шло',
                    'plural': 'шли'
                }
            },
            'купить': {
                'translation': 'buy',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'куплю',
                    'ты': 'купишь',
                    'он': 'купит',
                    'мы': 'купим',
                    'вы': 'купите',
                    'они': 'купят'
                },
                'past': {
                    'masculine': 'купил',
                    'feminine': 'купила',
                    'neuter': 'купило',
                    'plural': 'купили'
                }
            },
            'курить': {
                'translation': 'smoke',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'курю',
                    'ты': 'куришь',
                    'он': 'курит',
                    'мы': 'курим',
                    'вы': 'курите',
                    'они': 'курят'
                },
                'past': {
                    'masculine': 'курил',
                    'feminine': 'курила',
                    'neuter': 'курило',
                    'plural': 'курили'
                }
            },
            'лежать': {
                'translation': 'lie (down)',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'лежу',
                    'ты': 'лежишь',
                    'он': 'лежит',
                    'мы': 'лежим',
                    'вы': 'лежите',
                    'они': 'лежат'
                },
                'past': {
                    'masculine': 'лежал',
                    'feminine': 'лежала',
                    'neuter': 'лежало',
                    'plural': 'лежали'
                }
            },
            'любить': {
                'translation': 'love',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'люблю',
                    'ты': 'любишь',
                    'он': 'любит',
                    'мы': 'любим',
                    'вы': 'любите',
                    'они': 'любят'
                },
                'past': {
                    'masculine': 'любил',
                    'feminine': 'любила',
                    'neuter': 'любило',
                    'plural': 'любили'
                }
            },
            'мочь': {
                'translation': 'be able, can',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': True,
                'present': {
                    'я': 'могу',
                    'ты': 'можешь',
                    'он': 'может',
                    'мы': 'можем',
                    'вы': 'можете',
                    'они': 'могут'
                },
                'past': {
                    'masculine': 'мог',
                    'feminine': 'могла',
                    'neuter': 'могло',
                    'plural': 'могли'
                }
            },
            'написать': {
                'translation': 'write',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'напишу',
                    'ты': 'напишешь',
                    'он': 'напишет',
                    'мы': 'напишем',
                    'вы': 'напишете',
                    'они': 'напишут'
                },
                'past': {
                    'masculine': 'написал',
                    'feminine': 'написала',
                    'neuter': 'написало',
                    'plural': 'написали'
                }
            },
            'находиться': {
                'translation': 'be located',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'нахожусь',
                    'ты': 'находишься',
                    'он': 'находится',
                    'мы': 'находимся',
                    'вы': 'находитесь',
                    'они': 'находятся'
                },
                'past': {
                    'masculine': 'находился',
                    'feminine': 'находилась',
                    'neuter': 'находилось',
                    'plural': 'находились'
                }
            },
            'нравиться': {
                'translation': 'be pleasing, like',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'нравлюсь',
                    'ты': 'нравишься',
                    'он': 'нравится',
                    'мы': 'нравимся',
                    'вы': 'нравитесь',
                    'они': 'нравятся'
                },
                'past': {
                    'masculine': 'нравился',
                    'feminine': 'нравилась',
                    'neuter': 'нравилось',
                    'plural': 'нравились'
                }
            },
            'обедать': {
                'translation': 'have lunch',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'обедаю',
                    'ты': 'обедаешь',
                    'он': 'обедает',
                    'мы': 'обедаем',
                    'вы': 'обедаете',
                    'они': 'обедают'
                },
                'past': {
                    'masculine': 'обедал',
                    'feminine': 'обедала',
                    'neuter': 'обедало',
                    'plural': 'обедали'
                }
            },
            'опаздывать': {
                'translation': 'be late',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'опаздываю',
                    'ты': 'опаздываешь',
                    'он': 'опаздывает',
                    'мы': 'опаздываем',
                    'вы': 'опаздываете',
                    'они': 'опаздывают'
                },
                'past': {
                    'masculine': 'опаздывал',
                    'feminine': 'опаздывала',
                    'neuter': 'опаздывало',
                    'plural': 'опаздывали'
                }
            },
            'отдыхать': {
                'translation': 'rest, relax',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'отдыхаю',
                    'ты': 'отдыхаешь',
                    'он': 'отдыхает',
                    'мы': 'отдыхаем',
                    'вы': 'отдыхаете',
                    'они': 'отдыхают'
                },
                'past': {
                    'masculine': 'отдыхал',
                    'feminine': 'отдыхала',
                    'neuter': 'отдыхало',
                    'plural': 'отдыхали'
                }
            },
            'петь': {
                'translation': 'sing',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'пою',
                    'ты': 'поёшь',
                    'он': 'поёт',
                    'мы': 'поём',
                    'вы': 'поёте',
                    'они': 'поют'
                },
                'past': {
                    'masculine': 'пел',
                    'feminine': 'пела',
                    'neuter': 'пело',
                    'plural': 'пели'
                }
            },
            'писать': {
                'translation': 'write',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'пишу',
                    'ты': 'пишешь',
                    'он': 'пишет',
                    'мы': 'пишем',
                    'вы': 'пишете',
                    'они': 'пишут'
                },
                'past': {
                    'masculine': 'писал',
                    'feminine': 'писала',
                    'neuter': 'писало',
                    'plural': 'писали'
                }
            },
            'пить': {
                'translation': 'drink',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'пью',
                    'ты': 'пьёшь',
                    'он': 'пьёт',
                    'мы': 'пьём',
                    'вы': 'пьёте',
                    'они': 'пьют'
                },
                'past': {
                    'masculine': 'пил',
                    'feminine': 'пила',
                    'neuter': 'пило',
                    'plural': 'пили'
                }
            },
            'подарить': {
                'translation': 'give (a gift)',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'подарю',
                    'ты': 'подаришь',
                    'он': 'подарит',
                    'мы': 'подарим',
                    'вы': 'подарите',
                    'они': 'подарят'
                },
                'past': {
                    'masculine': 'подарил',
                    'feminine': 'подарила',
                    'neuter': 'подарило',
                    'plural': 'подарили'
                }
            },
            'подумать': {
                'translation': 'think',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'подумаю',
                    'ты': 'подумаешь',
                    'он': 'подумает',
                    'мы': 'подумаем',
                    'вы': 'подумаете',
                    'они': 'подумают'
                },
                'past': {
                    'masculine': 'подумал',
                    'feminine': 'подумала',
                    'neuter': 'подумало',
                    'plural': 'подумали'
                }
            },
            'поехать': {
                'translation': 'go (by vehicle)',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'поеду',
                    'ты': 'поедешь',
                    'он': 'поедет',
                    'мы': 'поедем',
                    'вы': 'поедете',
                    'они': 'поедут'
                },
                'past': {
                    'masculine': 'поехал',
                    'feminine': 'поехала',
                    'neuter': 'поехало',
                    'plural': 'поехали'
                }
            },
            'позвонить': {
                'translation': 'call, phone',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'позвоню',
                    'ты': 'позвонишь',
                    'он': 'позвонит',
                    'мы': 'позвоним',
                    'вы': 'позвоните',
                    'они': 'позвонят'
                },
                'past': {
                    'masculine': 'позвонил',
                    'feminine': 'позвонила',
                    'neuter': 'позвонило',
                    'plural': 'позвонили'
                }
            },
            'пойти': {
                'translation': 'go (on foot)',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': True,
                'future': {
                    'я': 'пойду',
                    'ты': 'пойдёшь',
                    'он': 'пойдёт',
                    'мы': 'пойдём',
                    'вы': 'пойдёте',
                    'они': 'пойдут'
                },
                'past': {
                    'masculine': 'пошёл',
                    'feminine': 'пошла',
                    'neuter': 'пошло',
                    'plural': 'пошли'
                }
            },
            'покупать': {
                'translation': 'buy',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'покупаю',
                    'ты': 'покупаешь',
                    'он': 'покупает',
                    'мы': 'покупаем',
                    'вы': 'покупаете',
                    'они': 'покупают'
                },
                'past': {
                    'masculine': 'покупал',
                    'feminine': 'покупала',
                    'neuter': 'покупало',
                    'plural': 'покупали'
                }
            },
            'помнить': {
                'translation': 'remember',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'помню',
                    'ты': 'помнишь',
                    'он': 'помнит',
                    'мы': 'помним',
                    'вы': 'помните',
                    'они': 'помнят'
                },
                'past': {
                    'masculine': 'помнил',
                    'feminine': 'помнила',
                    'neuter': 'помнило',
                    'plural': 'помнили'
                }
            },
            'поступать': {
                'translation': 'apply for entrance',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'поступаю',
                    'ты': 'поступаешь',
                    'он': 'поступает',
                    'мы': 'поступаем',
                    'вы': 'поступаете',
                    'они': 'поступают'
                },
                'past': {
                    'masculine': 'поступал',
                    'feminine': 'поступала',
                    'neuter': 'поступало',
                    'plural': 'поступали'
                }
            },
            'поужинать': {
                'translation': 'have dinner',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'поужинаю',
                    'ты': 'поужинаешь',
                    'он': 'поужинает',
                    'мы': 'поужинаем',
                    'вы': 'поужинаете',
                    'они': 'поужинают'
                },
                'past': {
                    'masculine': 'поужинал',
                    'feminine': 'поужинала',
                    'neuter': 'поужинало',
                    'plural': 'поужинали'
                }
            },
            'повторять': {
                'translation': 'repeat',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'повторяю',
                    'ты': 'повторяешь',
                    'он': 'повторяет',
                    'мы': 'повторяем',
                    'вы': 'повторяете',
                    'они': 'повторяют'
                },
                'past': {
                    'masculine': 'повторял',
                    'feminine': 'повторяла',
                    'neuter': 'повторяло',
                    'plural': 'повторяли'
                }
            },
            'посылать': {
                'translation': 'send',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'посылаю',
                    'ты': 'посылаешь',
                    'он': 'посылает',
                    'мы': 'посылаем',
                    'вы': 'посылаете',
                    'они': 'посылают'
                },
                'past': {
                    'masculine': 'посылал',
                    'feminine': 'посылала',
                    'neuter': 'посылало',
                    'plural': 'посылали'
                }
            },
            'приезжать': {
                'translation': 'arrive',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'приезжаю',
                    'ты': 'приезжаешь',
                    'он': 'приезжает',
                    'мы': 'приезжаем',
                    'вы': 'приезжаете',
                    'они': 'приезжают'
                },
                'past': {
                    'masculine': 'приезжал',
                    'feminine': 'приезжала',
                    'neuter': 'приезжало',
                    'plural': 'приезжали'
                }
            },
            'продолжать': {
                'translation': 'continue',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'продолжаю',
                    'ты': 'продолжаешь',
                    'он': 'продолжает',
                    'мы': 'продолжаем',
                    'вы': 'продолжаете',
                    'они': 'продолжают'
                },
                'past': {
                    'masculine': 'продолжал',
                    'feminine': 'продолжала',
                    'neuter': 'продолжало',
                    'plural': 'продолжали'
                }
            },
            'просить': {
                'translation': 'ask',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'прошу',
                    'ты': 'просишь',
                    'он': 'просит',
                    'мы': 'просим',
                    'вы': 'просите',
                    'они': 'просят'
                },
                'past': {
                    'masculine': 'просил',
                    'feminine': 'просила',
                    'neuter': 'просило',
                    'plural': 'просили'
                }
            },
            'разговаривать': {
                'translation': 'talk, converse',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'разговариваю',
                    'ты': 'разговариваешь',
                    'он': 'разговаривает',
                    'мы': 'разговариваем',
                    'вы': 'разговариваете',
                    'они': 'разговаривают'
                },
                'past': {
                    'masculine': 'разговаривал',
                    'feminine': 'разговаривала',
                    'neuter': 'разговаривало',
                    'plural': 'разговаривали'
                }
            },
            'сделать': {
                'translation': 'do, make',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'сделаю',
                    'ты': 'сделаешь',
                    'он': 'сделает',
                    'мы': 'сделаем',
                    'вы': 'сделаете',
                    'они': 'сделают'
                },
                'past': {
                    'masculine': 'сделал',
                    'feminine': 'сделала',
                    'neuter': 'сделало',
                    'plural': 'сделали'
                }
            },
            'сидеть': {
                'translation': 'sit',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'сижу',
                    'ты': 'сидишь',
                    'он': 'сидит',
                    'мы': 'сидим',
                    'вы': 'сидите',
                    'они': 'сидят'
                },
                'past': {
                    'masculine': 'сидел',
                    'feminine': 'сидела',
                    'neuter': 'сидело',
                    'plural': 'сидели'
                }
            },
            'сказать': {
                'translation': 'say, tell',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': False,
                'future': {
                    'я': 'скажу',
                    'ты': 'скажешь',
                    'он': 'скажет',
                    'мы': 'скажем',
                    'вы': 'скажете',
                    'они': 'скажут'
                },
                'past': {
                    'masculine': 'сказал',
                    'feminine': 'сказала',
                    'neuter': 'сказало',
                    'plural': 'сказали'
                }
            },
            'смочь': {
                'translation': 'be able, can (perfective)',
                'aspect': 'perfective',
                'conjugation': 'I',
                'irregular': True,
                'future': {
                    'я': 'смогу',
                    'ты': 'сможешь',
                    'он': 'сможет',
                    'мы': 'сможем',
                    'вы': 'сможете',
                    'они': 'смогут'
                },
                'past': {
                    'masculine': 'смог',
                    'feminine': 'смогла',
                    'neuter': 'смогло',
                    'plural': 'смогли'
                }
            },
            'спать': {
                'translation': 'sleep',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'сплю',
                    'ты': 'спишь',
                    'он': 'спит',
                    'мы': 'спим',
                    'вы': 'спите',
                    'они': 'спят'
                },
                'past': {
                    'masculine': 'спал',
                    'feminine': 'спала',
                    'neuter': 'спало',
                    'plural': 'спали'
                }
            },
            'спрашивать': {
                'translation': 'ask',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'спрашиваю',
                    'ты': 'спрашиваешь',
                    'он': 'спрашивает',
                    'мы': 'спрашиваем',
                    'вы': 'спрашиваете',
                    'они': 'спрашивают'
                },
                'past': {
                    'masculine': 'спрашивал',
                    'feminine': 'спрашивала',
                    'neuter': 'спрашивало',
                    'plural': 'спрашивали'
                }
            },
            'становиться': {
                'translation': 'become',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'становлюсь',
                    'ты': 'становишься',
                    'он': 'становится',
                    'мы': 'становимся',
                    'вы': 'становитесь',
                    'они': 'становятся'
                },
                'past': {
                    'masculine': 'становился',
                    'feminine': 'становилась',
                    'neuter': 'становилось',
                    'plural': 'становились'
                }
            },
            'стоить': {
                'translation': 'cost',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'стою',
                    'ты': 'стоишь',
                    'он': 'стоит',
                    'мы': 'стоим',
                    'вы': 'стоите',
                    'они': 'стоят'
                },
                'past': {
                    'masculine': 'стоил',
                    'feminine': 'стоила',
                    'neuter': 'стоило',
                    'plural': 'стоили'
                }
            },
            'стоять': {
                'translation': 'stand',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'стою',
                    'ты': 'стоишь',
                    'он': 'стоит',
                    'мы': 'стоим',
                    'вы': 'стоите',
                    'они': 'стоят'
                },
                'past': {
                    'masculine': 'стоял',
                    'feminine': 'стояла',
                    'neuter': 'стояло',
                    'plural': 'стояли'
                }
            },
            'строить': {
                'translation': 'build',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'строю',
                    'ты': 'строишь',
                    'он': 'строит',
                    'мы': 'строим',
                    'вы': 'строите',
                    'они': 'строят'
                },
                'past': {
                    'masculine': 'строил',
                    'feminine': 'строила',
                    'neuter': 'строило',
                    'plural': 'строили'
                }
            },
            'танцевать': {
                'translation': 'dance',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'танцую',
                    'ты': 'танцуешь',
                    'он': 'танцует',
                    'мы': 'танцуем',
                    'вы': 'танцуете',
                    'они': 'танцуют'
                },
                'past': {
                    'masculine': 'танцевал',
                    'feminine': 'танцевала',
                    'neuter': 'танцевало',
                    'plural': 'танцевали'
                }
            },
            'увидеть': {
                'translation': 'see (perfective)',
                'aspect': 'perfective',
                'conjugation': 'II',
                'irregular': False,
                'future': {
                    'я': 'увижу',
                    'ты': 'увидишь',
                    'он': 'увидит',
                    'мы': 'увидим',
                    'вы': 'увидите',
                    'они': 'увидят'
                },
                'past': {
                    'masculine': 'увидел',
                    'feminine': 'увидела',
                    'neuter': 'увидело',
                    'plural': 'увидели'
                }
            },
            'ужинать': {
                'translation': 'have dinner',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'ужинаю',
                    'ты': 'ужинаешь',
                    'он': 'ужинает',
                    'мы': 'ужинаем',
                    'вы': 'ужинаете',
                    'они': 'ужинают'
                },
                'past': {
                    'masculine': 'ужинал',
                    'feminine': 'ужинала',
                    'neuter': 'ужинало',
                    'plural': 'ужинали'
                }
            },
            'умирать': {
                'translation': 'die',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'умираю',
                    'ты': 'умираешь',
                    'он': 'умирает',
                    'мы': 'умираем',
                    'вы': 'умираете',
                    'они': 'умирают'
                },
                'past': {
                    'masculine': 'умирал',
                    'feminine': 'умирала',
                    'neuter': 'умирало',
                    'plural': 'умирали'
                }
            },
            'уставать': {
                'translation': 'get tired',
                'aspect': 'imperfective',
                'conjugation': 'I',
                'irregular': False,
                'present': {
                    'я': 'устаю',
                    'ты': 'устаёшь',
                    'он': 'устаёт',
                    'мы': 'устаём',
                    'вы': 'устаёте',
                    'они': 'устают'
                },
                'past': {
                    'masculine': 'уставал',
                    'feminine': 'уставала',
                    'neuter': 'уставало',
                    'plural': 'уставали'
                }
            },
            'учить': {
                'translation': 'teach, study',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'учу',
                    'ты': 'учишь',
                    'он': 'учит',
                    'мы': 'учим',
                    'вы': 'учите',
                    'они': 'учат'
                },
                'past': {
                    'masculine': 'учил',
                    'feminine': 'учила',
                    'neuter': 'учило',
                    'plural': 'учили'
                }
            },
            'учиться': {
                'translation': 'study, learn',
                'aspect': 'imperfective',
                'conjugation': 'II',
                'irregular': False,
                'present': {
                    'я': 'учуся',
                    'ты': 'учишься',
                    'он': 'учится',
                    'мы': 'учимся',
                    'вы': 'учитесь',
                    'они': 'учатся'
                },
                'past': {
                    'masculine': 'учился',
                    'feminine': 'училась',
                    'neuter': 'училось',
                    'plural': 'учились'
                }
            }
        }
    
    def get_verb(self, infinitive: str) -> dict:
        """Get verb information"""
        return self.verbs.get(infinitive, {})
    
    def is_irregular(self, infinitive: str) -> bool:
        """Check if verb is irregular"""
        return infinitive in self.irregular_verbs
    
    def get_aspect(self, infinitive: str) -> str:
        """Get verb aspect (perfective/imperfective)"""
        verb_data = self.verbs.get(infinitive, {})
        return verb_data.get('aspect', 'unknown')
    
    def get_all_verbs(self) -> dict:
        """Get all verbs"""
        return self.verbs
    
    def get_irregular_verbs(self) -> list:
        """Get list of irregular verb infinitives"""
        return [v for v in self.verbs.keys() if self.verbs[v].get('irregular', False)]