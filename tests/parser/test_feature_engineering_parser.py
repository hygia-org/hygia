import pytest

from parser.feature_engineering_parser import FeatureEngineeringParser

class TestFeatureEngineeringParser():
    
    def setup_method(self):
        self.feature_engineering_data = [{'input': {'columns': [{'foo_1': ['NUMBER', 'ADDRESS', 'ZIPCODE']}, {'foo_2': 'NUMBER'}], 'features': {'word_embedding': {'data_lang': 'es', 'foo_1': {'dimensions': 23}}}}}]
        self.parser = FeatureEngineeringParser()

    def test_parser_feature_engineering(self):
        features_config, columns_set_alias = self.parser.parse(self.feature_engineering_data)
        default_case = features_config[0]
        
        assert ['foo_1', 'foo_2'] == columns_set_alias
        
        assert 'columns_alias' in default_case
        assert 'columns_set' in default_case
        assert 'enabled_features' in default_case
        
        assert 'data_lang' in default_case
        assert default_case['data_lang'] == 'es'

        assert 'dimensions' in default_case
        assert type(default_case['dimensions']) == dict
        
    def test_get_dataframe(self):
        data = self.feature_engineering_data[0]
        columns_set, columns_set_alias = self.parser._get_dataframe(data['input']['columns'])
        
        assert 'foo_1' in columns_set[0].keys()
        assert 'foo_2' in columns_set_alias
        
    def test_get_features_details(self):
        data = self.feature_engineering_data[0]
        word_embedding, keyboard_smash = self.parser._get_features_details(data['input']['features'])
        
        assert 'data_lang' in word_embedding
        assert 'foo_1' in word_embedding
        
        assert 'ksmash_sequence_vowels' in keyboard_smash
                
    @pytest.mark.parametrize(
        'word_embedding, response',[
            ({'data_lang': 'pt', 'foo_1': {'dimensions': 23}}, {'data_lang': 'pt','dimensions': 23}),
            ({'data_lang': 'pt'}, {'data_lang': 'pt', 'dimensions': 25})
        ]
    )
    def test_get_word_embedding_config(self, word_embedding, response):
        data_lang, dimensions = self.parser._get_word_embedding_config(word_embedding, ['foo_1'])
        
        assert data_lang == response['data_lang']
        assert dimensions['foo_1'] == response['dimensions']
                
    def test_get_keyboard_smash_config(self):
        data = self.feature_engineering_data[0]
        keyboard_smash_default_value = self.parser._get_keyboard_smash_config(data['input']['features'])
        
        assert 'ksmash_sequence_vowels' in keyboard_smash_default_value
        assert 'ksmash_sequence_consonants' in keyboard_smash_default_value
        assert 'ksmash_sequence_special_characters' in keyboard_smash_default_value
        assert 'ksmash_numbers' in keyboard_smash_default_value
        assert 'ksmash_char_frequence' in keyboard_smash_default_value
        