import csv
import os
from typing import List, Dict

class VocabularyExtractor:
    """Extract unique vocabulary words from SMARTool CSV data"""
    
    def __init__(self, csv_file: str = "SMARTool_data_A1.csv"):
        self.csv_file = os.path.join(os.path.dirname(__file__), csv_file)
    
    def check_csv_file(self) -> bool:
        """Check if CSV file exists and is readable"""
        if not os.path.exists(self.csv_file):
            print(f"\n❌ CSV file not found: {self.csv_file}")
            return False
        
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Try to read first row
                next(reader)
            print(f"✅ CSV file found and readable: {self.csv_file}")
            return True
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return False
    
    def _extract_aspect_from_analysis(self, analysis: str) -> str:
        """Extract aspect (Perf/Imperf) from the Analysis column"""
        if not analysis:
            return 'unknown'
        
        analysis_lower = analysis.lower()
        if 'perf' in analysis_lower and 'imperf' not in analysis_lower:
            return 'perfective'
        elif 'imperf' in analysis_lower:
            return 'imperfective'
        return 'unknown'
    
    def extract_unique_words(self) -> List[Dict]:
        """
        Extract unique Russian words with their English translations
        Returns list of dicts: {russian: str, english: str, pos: str, level: str, aspect: str (for verbs)}
        """
        unique_words = {}
        
        if not os.path.exists(self.csv_file):
            print(f"\n❌ Error: Could not find CSV file at: {self.csv_file}")
            print(f"   Expected location: {os.path.dirname(__file__)}")
            print(f"   Looking for: SMARTool_data_A1.csv")
            return []
        
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                rows_processed = 0
                rows_added = 0
                
                for row in reader:
                    rows_processed += 1
                    
                    lemma = row.get('Target language lemma', '').strip()
                    # First try 'English gloss', then fall back to 'User language gloss'
                    english = row.get('English gloss', '').strip()
                    if not english:
                        english = row.get('User language gloss', '').strip()
                    pos = row.get('POS', '').strip()
                    level = row.get('Level', '').strip()
                    analysis = row.get('Analysis', '').strip()
                    
                    # Skip empty entries
                    if not lemma or not english:
                        continue
                    
                    # Skip entries marked as deleted
                    if lemma.lower() == 'deleted' or english.lower() == 'deleted':
                        continue
                    
                    # Use lemma as key to ensure uniqueness
                    if lemma not in unique_words:
                        word_data = {
                            'russian': lemma,
                            'english': english,
                            'pos': pos,
                            'level': level
                        }
                        
                        # Add aspect information for verbs
                        if pos and pos.startswith('V'):
                            word_data['aspect'] = self._extract_aspect_from_analysis(analysis)
                        
                        unique_words[lemma] = word_data
                        rows_added += 1
                
                print(f"\n📊 CSV Processing Summary:")
                print(f"   Total rows processed: {rows_processed}")
                print(f"   Unique words extracted: {rows_added}")
                
        except Exception as e:
            print(f"\n❌ Error reading CSV file: {e}")
            return []
        
        return list(unique_words.values())
    
    def get_words_by_pos(self, pos: str) -> List[Dict]:
        """Get words filtered by part of speech (N, V, A, etc.)"""
        all_words = self.extract_unique_words()
        return [w for w in all_words if w['pos'].startswith(pos)]
    
    def get_words_by_level(self, level: str = 'A1') -> List[Dict]:
        """Get words filtered by CEFR level"""
        all_words = self.extract_unique_words()
        return [w for w in all_words if w['level'] == level]
    
    def get_verbs(self) -> List[Dict]:
        """Get all verbs with aspect information"""
        return self.get_words_by_pos('V')
    
    def get_verbs_by_aspect(self, aspect: str) -> List[Dict]:
        """Get verbs filtered by aspect (perfective/imperfective)"""
        verbs = self.get_verbs()
        return [v for v in verbs if v.get('aspect', '').lower() == aspect.lower()]