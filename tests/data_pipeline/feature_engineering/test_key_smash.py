import pytest
import pandas as pd
from hygia import KeySmash

class TestKeySmash:
    
    def setup_method(self):
        self.key_smash = KeySmash(ignore_shannon_entropy=False)

    @pytest.mark.parametrize("data, expected_output", [
        ("PUENTECILLA KM. 1.7", 1.121212121212121),
        ("ASDASD XXXX", 3.0)
    ])
    def test_average_of_char_count_squared(self, data, expected_output):
        assert self.key_smash.average_of_char_count_squared(data) == expected_output

    @pytest.mark.parametrize("data, opt, expected_output", [
        ("PUENTECILLA KM. 1.7", "vowels", 0.0),
        ("ASDASD XXXX", "consonants", 2.272727272727273),
        ("ABC123 !@#$%", "special_characters", 2.0833333333333335)
    ])
    def test_count_sequence_squared(self, data, opt, expected_output):
        assert self.key_smash.count_sequence_squared(data, opt) == expected_output

    @pytest.mark.parametrize("data, expected_output", [
        ("ABC 123 !@#", 0.0),
        ("123456", 0.0),
        ("ABC123 !@#", 0.9)
    ])
    def test_ratio_of_numeric_digits_squared(self, data, expected_output):
        assert self.key_smash.ratio_of_numeric_digits_squared(data) == expected_output
    
    @pytest.mark.parametrize("data, expected_output", [
        ("PUENTECILLA KM. 1.7",3.7345216647797517),
        ("ASDASD XXXX",1.9219280948873623),
        ("AS AA",0.8112781244591328),
        ("XX XX",-0.0)
    ])
    def test_shannon_entropy(self, data, expected_output):
        assert self.key_smash.shannon_entropy(data) == expected_output
    
    @pytest.mark.parametrize("data, expected_output", [
        ("PUENTECILLA KM. 1.7",1.0),
        ("ASDASD XXXX",1.3636363636363638),
        ("AAAAAA AAAA",1.6363636363636362),
        ("XX XX",1.2)
    ])
    def test_repeated_bigram_ratio(self, data, expected_output):
        assert self.key_smash.repeated_bigram_ratio(data) == expected_output
    
    @pytest.mark.parametrize("data, expected_output", [
        ("PUENTECILLA KM. 1.7",1.7894736842105263),
        ("ASDASD XXXX",1.4545454545454546),
        ("AAAAAA AAAA",1.1818181818181819),
        ("XX XX",1.4)
    ])
    def test_unique_char_ratio(self, data, expected_output):
        assert self.key_smash.unique_char_ratio(data) == expected_output
    
    def test_extract_key_smash_features(self):
        df = pd.DataFrame({"text_column": ["abcdefgh", "ijklmnop", "qrstuvwxyz"]})
        result = self.key_smash.extract_key_smash_features(df, "text_column")

        assert 'feature_ks_count_sequence_squared_vowels_text_column' in result.columns
        assert 'feature_ks_count_sequence_squared_consonants_text_column' in result.columns
        assert 'feature_ks_count_sequence_squared_special_characters_text_column' in result.columns
        assert 'feature_ks_average_of_char_count_squared_text_column' in result.columns
        assert 'feature_ks_shannon_entropy_text_column' in result.columns
        assert result.shape[1] == 6 # Ensure no extra columns are added