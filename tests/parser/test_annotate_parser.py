import pytest

from hygia.parser.annotate_data_parser import AnnotateDataParser

class TestAnnotateParser():
    
    def setup_method(self):
        self.model_data = [{'input': {'columns': ['street', 'phone'], 'thresholds': {'ksmash_sequence_vowels': 1.0, 'ksmash_sequence_consonants': 1.999, 'ksmash_sequence_special_characters': 2.2499, 'ksmash_numbers': 2.9, 'ksmash_char_frequence': 2.78}}}]
        self.parser = AnnotateDataParser()
        
    def test_parser_annotate_data(self):
        configs = self.parser.parse(self.model_data)
        default_case = configs[0]
        
        assert 'columns' in default_case
        assert default_case['columns'] == ['street', 'phone']
        
        assert 'thresholds' in default_case
        thresholds = default_case['thresholds']
        
        assert 'ksmash_char_frequence' in thresholds
        assert thresholds['ksmash_char_frequence'] == 2.78
        
        assert 'ksmash_numbers' in thresholds
        assert thresholds['ksmash_numbers'] == 2.9
        
        assert 'ksmash_sequence_consonants' in thresholds
        assert thresholds['ksmash_sequence_consonants'] == 1.999
        
        assert 'ksmash_sequence_special_characters' in thresholds
        assert thresholds['ksmash_sequence_special_characters'] == 2.2499
        
        assert 'ksmash_sequence_vowels' in thresholds
        assert thresholds['ksmash_sequence_vowels'] == 1.0
        
    def test_get_thresholds(self):
        thresholds = self.parser.get_thresholds(self.model_data[0]['input'])
    
        assert 'ksmash_char_frequence' in thresholds
        assert thresholds['ksmash_char_frequence'] == 2.78
        
        assert 'ksmash_numbers' in thresholds
        assert thresholds['ksmash_numbers'] == 2.9
        
        assert 'ksmash_sequence_consonants' in thresholds
        assert thresholds['ksmash_sequence_consonants'] == 1.999
        
        assert 'ksmash_sequence_special_characters' in thresholds
        assert thresholds['ksmash_sequence_special_characters'] == 2.2499
        
        assert 'ksmash_sequence_vowels' in thresholds
        assert thresholds['ksmash_sequence_vowels'] == 1.0
        
    def test_get_keyboard_smash_default_config(self):
        thresholds = self.parser.get_thresholds({'thresholds': {'ksmash_sequence_vowels': 1.1}})
        
        assert 'ksmash_char_frequence' in thresholds
        assert thresholds['ksmash_char_frequence'] == 2.78
        
        assert 'ksmash_numbers' in thresholds
        assert thresholds['ksmash_numbers'] == 2.9
        
        assert 'ksmash_sequence_consonants' in thresholds
        assert thresholds['ksmash_sequence_consonants'] == 1.999
        
        assert 'ksmash_sequence_special_characters' in thresholds
        assert thresholds['ksmash_sequence_special_characters'] == 2.2499
        
        assert 'ksmash_sequence_vowels' in thresholds
        assert thresholds['ksmash_sequence_vowels'] == 1.1
        
    def test_get_keyboard_smash_default_config(self):
        thresholds = self.parser.get_thresholds()
        
        assert 'ksmash_char_frequence' in thresholds
        assert thresholds['ksmash_char_frequence'] == 2.78
        
        assert 'ksmash_numbers' in thresholds
        assert thresholds['ksmash_numbers'] == 2.9
        
        assert 'ksmash_sequence_consonants' in thresholds
        assert thresholds['ksmash_sequence_consonants'] == 1.999
        
        assert 'ksmash_sequence_special_characters' in thresholds
        assert thresholds['ksmash_sequence_special_characters'] == 2.2499
        
        assert 'ksmash_sequence_vowels' in thresholds
        assert thresholds['ksmash_sequence_vowels'] == 1.0
