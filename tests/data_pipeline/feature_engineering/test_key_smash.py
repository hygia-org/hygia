import pytest
from src.data_pipeline.feature_engineering.key_smash import KeySmash

key_smash = KeySmash()

@pytest.mark.parametrize("data, expected_output", [
    ("PUENTECILLA KM. 1.7", 1.121212121212121),
    ("ASDASD XXXX", 3.0)
])
def test_char_frequency_metric(data, expected_output):
    assert key_smash.calculate_char_frequency_metric(data) == expected_output

@pytest.mark.parametrize("data, opt, expected_output", [
    ("PUENTECILLA KM. 1.7", "vowels", 0.21052631578947367),
    ("ASDASD XXXX", "consonants", 2.1818181818181817)
])
def test_irregular_sequence_metric(data, opt, expected_output):
    assert key_smash.calculate_irregular_sequence_metric(data, opt) == expected_output

@pytest.mark.parametrize("data, expected_output", [
    ("ABC 123 !@#", 0.0),
    ("ABC123 !@#", 0.9)
])
def test_number_count_metric(data, expected_output):
    assert key_smash.calculate_number_count_metric(data) == expected_output