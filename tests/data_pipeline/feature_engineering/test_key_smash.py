import pytest
import pandas as pd
from hygia import KeySmash

class TestKeySmash:
    
    def setup_method(self):
        self.key_smash = KeySmash()

    @pytest.mark.parametrize("data, expected_output", [
        ("PUENTECILLA KM. 1.7", 1.121212121212121),
        ("ASDASD XXXX", 3.0)
    ])
    def test_average_of_char_count_squared(self, data, expected_output):
        assert self.key_smash.average_of_char_count_squared(data) == expected_output

    @pytest.mark.parametrize("data, opt, expected_output", [
        ("PUENTECILLA KM. 1.7", "vowels", 0.21052631578947367),
        ("ASDASD XXXX", "consonants", 2.1818181818181817)
    ])
    def test_count_sequence_squared(self, data, opt, expected_output):
        assert self.key_smash.count_sequence_squared(data, opt) == expected_output

    @pytest.mark.parametrize("data, expected_output", [
        ("ABC 123 !@#", 0.0),
        ("ABC123 !@#", 0.9)
    ])
    def test_ratio_of_numeric_digits_squared(self, data, expected_output):
        assert self.key_smash.ratio_of_numeric_digits_squared(data) == expected_output
    
    def test_extract_key_smash_features(self):
        df = pd.DataFrame({"text_column": ["abcdefgh", "ijklmnop", "qrstuvwxyz"]})
        result = self.key_smash.extract_key_smash_features(df, "text_column", normalize=False)

        assert 'feature_ks_count_sequence_squared_vowels_text_column' in result.columns
        assert 'feature_ks_count_sequence_squared_consonants_text_column' in result.columns
        assert 'feature_ks_count_sequence_squared_special_characters_text_column' in result.columns
        assert 'feature_ks_ratio_of_numeric_digits_squared_text_column' in result.columns
        assert 'feature_ks_average_of_char_count_squared_text_column' in result.columns
        assert result.shape[1] == 6 # Ensure no extra columns are added