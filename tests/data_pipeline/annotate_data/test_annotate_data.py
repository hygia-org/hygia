import pandas as pd
from hygia import AnnotateData

class TestAnnotateData:
    def setup_method(self):
        self.annotate_data = AnnotateData()
        
    def test_annotate_data(self):
        df = pd.DataFrame({
            'concat_address': ['test', 'asdasd', 'DELL', 'PENDIENTE 123!@#'],
            'feature_ks_count_sequence_squared_vowels': [0.05, 0.15, 0.25, 0.35],
            'feature_ks_count_sequence_squared_consonants': [0.05, 0.15, 0.9, 0.35],
            'feature_ks_count_sequence_squared_special_characters': [0.05, 0.15, 0.25, 0.35],
            'feature_ks_ratio_of_numeric_digits_squared': [0.05, 0.15, 0.25, 0.9],
            'feature_ks_average_of_char_count_squared': [0.05, 0.15, 0.25, 0.35],
        })
        
        key_smash_thresholds = {
            'count_sequence_squared_vowels': 0.9,
            'count_sequence_squared_consonants': 0.9,
            'count_sequence_squared_special_characters': 0.9,
            'ratio_of_numeric_digits_squared': 0.9,
            'average_of_char_count_squared': 0.9,
        }
        
        result = self.annotate_data.annotate_data(df, concatened_column_name='concat_address', ks_thresholds=key_smash_thresholds)
        
        assert 'target' in result.columns