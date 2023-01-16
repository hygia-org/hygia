import pytest

from hygia.parser.model_parser import ModelParser

class TestParser():
    
    def setup_method(self):
        self.model_data = {'random_forest': [{'input': {'trained_model_file': '../mock/RandomForest_Ksmash_WordEmbedding.model', 'type': 'address', 'columns': ['foo_1'], 'thresholds': {'test_size': 0.3, 'n_estimators': 100, 'keyboard_smash': {'foo_1': {'ksmash_sequence_vowels': 1.0, 'ksmash_sequence_consonants': 1.999, 'ksmash_sequence_special_characters': 2.2499, 'ksmash_numbers': 2.9, 'ksmash_char_frequence': 2.78}}}}}]}
        self.parser = ModelParser(['NUMBER', 'ADDRESS', 'ZIPCODE', 'foo_1', 'foo_2'])
        
    def test_parser_model(self):
        configs = self.parser.parse(self.model_data)
        default_case = configs[0]
        
        assert 'model' in default_case
        assert default_case['model'] == 'keyboard_smash'
        
        assert 'type' in default_case
        assert default_case['type'] == 'address'
        
        assert 'columns' in default_case
        assert 'foo_1' in default_case['columns']
        
        assert 'n_estimators' in default_case
        assert default_case['n_estimators'] == 100
        
        assert 'test_size' in default_case
        assert default_case['test_size'] == 0.3
        
        assert 'keyboard_smash' in default_case
      
    def test_get_random_forest_config(self):
        configs = self.parser.get_random_forest_address_config(self.model_data['random_forest'])
        test_case = configs[0]
        
        assert 'model' in test_case
        assert test_case['model'] == 'keyboard_smash'
        
        assert 'type' in test_case
        assert test_case['type'] == 'address'
        
        assert 'columns' in test_case
        assert 'foo_1' in test_case['columns']
        
        assert 'n_estimators' in test_case
        assert test_case['n_estimators'] == 100
        
        assert 'test_size' in test_case
        assert test_case['test_size'] == 0.3
        
        assert 'keyboard_smash' in test_case
    
    def test_get_columns(self):
        columns = self.parser.get_columns({'columns': ['foo_1']})
        
        assert columns == ['foo_1']
    
    def test_get_columns_fallback(self):
        with pytest.raises(ValueError) as exc:
            self.parser.get_columns({'columns': ['tudo_unto']})
            
        assert "`tudo_unto` column not match with the available columns" in str(exc.value)
        assert exc.type == ValueError
    
    def test_get_thresholds(self):
        keyboard_smash, n_estimators, test_size = self.parser.get_thresholds({'thresholds': {'test_size': 0.3, 'n_estimators': 100, 'keyboard_smash': {'foo_1': {'ksmash_sequence_vowels': 1.0, 'ksmash_sequence_consonants': 1.999, 'ksmash_sequence_special_characters': 2.2499, 'ksmash_numbers': 2.9, 'ksmash_char_frequence': 2.78}}}}, ['foo_1'])

        assert n_estimators == 100
        assert test_size == 0.3
        
        assert 'foo_1' in keyboard_smash
        
        foo_1_thresholds = keyboard_smash['foo_1']
        assert 'ksmash_char_frequence' in foo_1_thresholds
        assert foo_1_thresholds['ksmash_char_frequence'] == 2.78
        
        assert 'ksmash_numbers' in foo_1_thresholds
        assert foo_1_thresholds['ksmash_numbers'] == 2.9
        
        assert 'ksmash_sequence_consonants' in foo_1_thresholds
        assert foo_1_thresholds['ksmash_sequence_consonants'] == 1.999
        
        assert 'ksmash_sequence_special_characters' in foo_1_thresholds
        assert foo_1_thresholds['ksmash_sequence_special_characters'] == 2.2499
        
        assert 'ksmash_sequence_vowels' in foo_1_thresholds
        assert foo_1_thresholds['ksmash_sequence_vowels'] == 1.0
        
    def test_get_thresholds_fallback(self):
        with pytest.raises(ValueError) as exc:
            self.parser.get_thresholds({'thresholds': {'test_size': 0.3, 'n_estimators': 100, 'keyboard_smash': {'tudo_unto': {'ksmash_sequence_vowels': 1.0, 'ksmash_sequence_consonants': 1.999, 'ksmash_sequence_special_characters': 2.2499, 'ksmash_numbers': 2.9, 'ksmash_char_frequence': 2.78}}}}, ['foo_1'])
        
        assert "`tudo_unto` key not match with the available columns" in str(exc.value)
        assert exc.type == ValueError
        
    def test_get_keyboard_smash_default_config(self):
        configs = self.parser.get_keyboard_smash_default_thresholds(['foo_1'])
        
        thresholds = configs[0]['foo_1']
        
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
        