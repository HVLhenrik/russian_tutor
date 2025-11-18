import csv
import os
from typing import List, Dict

class RussianNorwegianExtractor:
    """Extract vocabulary words from Russian-Norwegian CSV data"""
    
    def __init__(self, csv_file: str = "russisk_norsk.csv"):
        self.csv_file = os.path.join(os.path.dirname(__file__), csv_file)
    
    def check_csv_file(self) -> bool:
        """Check if CSV file exists and is readable"""
        if not os.path.exists(self.csv_file):
            print(f"\n❌ CSV file not found: {self.csv_file}")
            return False
        
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f, delimiter=';')
                # Try to read first row
                next(reader)
            print(f"✅ CSV file found and readable: {self.csv_file}")
            return True
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return False
    
    def _extract_verb_info(self, russian: str, norwegian: str) -> Dict:
        """Extract verb aspect and base form from Norwegian translation"""
        aspect = 'unknown'
        is_verb = False
        
        # Handle None values
        if not norwegian:
            return {'is_verb': False, 'aspect': 'unknown'}
        
        # Check if it's a verb (starts with 'å')
        if norwegian.startswith('å '):
            is_verb = True
            
            # Check for aspect markers in parentheses
            norwegian_lower = norwegian.lower()
            if '(perfektiv)' in norwegian_lower:
                aspect = 'perfective'
            elif '(imperfektiv)' in norwegian_lower:
                aspect = 'imperfective'
        
        return {
            'is_verb': is_verb,
            'aspect': aspect
        }
    
    def extract_unique_words(self) -> List[Dict]:
        """
        Extract Russian words with Norwegian translations
        Returns list of dicts: {russian: str, norwegian: str, pos: str, aspect: str (for verbs)}
        """
        words_list = []
        
        if not os.path.exists(self.csv_file):
            print(f"\n❌ Error: Could not find CSV file at: {self.csv_file}")
            return []
        
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as f:
                # Use semicolon as delimiter
                reader = csv.DictReader(f, delimiter=';')
                
                rows_processed = 0
                rows_added = 0
                skipped_rows = 0
                
                for row in reader:
                    rows_processed += 1
                    
                    # Safely get values with default empty string
                    russian = (row.get('russisk') or '').strip()
                    norwegian = (row.get('norsk') or '').strip()
                    
                    # Skip empty entries
                    if not russian or not norwegian:
                        skipped_rows += 1
                        continue
                    
                    # Extract verb information
                    verb_info = self._extract_verb_info(russian, norwegian)
                    
                    word_data = {
                        'russian': russian,
                        'norwegian': norwegian,
                        'pos': 'V' if verb_info['is_verb'] else 'N/A',
                        'level': 'N/A'
                    }
                    
                    # Add aspect information for verbs
                    if verb_info['is_verb']:
                        word_data['aspect'] = verb_info['aspect']
                    
                    words_list.append(word_data)
                    rows_added += 1
                
                print(f"\n📊 CSV Processing Summary:")
                print(f"   Total rows processed: {rows_processed}")
                print(f"   Words extracted: {rows_added}")
                if skipped_rows > 0:
                    print(f"   Skipped rows (empty/incomplete): {skipped_rows}")
                
        except Exception as e:
            print(f"\n❌ Error reading CSV file: {e}")
            import traceback
            traceback.print_exc()
            return []
        
        return words_list
    
    def get_words_by_pos(self, pos: str) -> List[Dict]:
        """Get words filtered by part of speech (V for verbs, N/A for others)"""
        all_words = self.extract_unique_words()
        if pos == 'V':
            return [w for w in all_words if w['pos'] == 'V']
        else:
            return [w for w in all_words if w['pos'] != 'V']
    
    def get_verbs(self) -> List[Dict]:
        """Get all verbs with aspect information"""
        return self.get_words_by_pos('V')
    
    def get_verbs_by_aspect(self, aspect: str) -> List[Dict]:
        """Get verbs filtered by aspect (perfective/imperfective)"""
        verbs = self.get_verbs()
        return [v for v in verbs if v.get('aspect', '').lower() == aspect.lower()]