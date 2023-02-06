import pytest

from hygia.data_pipeline.pre_process_data.pre_process_data import PreProcessData
from hygia.paths.paths import root_path

@pytest.mark.parametrize("abbreviation, expected_replacement", [
    ('NO', "NUMBER"),
    ('no', "NUMBER"),
    ('no123', "NUMBER123"),
    ('no 123', "NUMBER 123"),
    ('123 no', "123 NUMBER"),
    ('not', "not"),
    ('NOT', "NOT"),
    ('ono', "ono")
])
class TestPreProcessData:
    def test_replace_abbreviation_coutry(self, abbreviation, expected_replacement):
        pre_process_data = PreProcessData(country='MEXICO')
        assert pre_process_data._replace_abbreviation(abbreviation) == expected_replacement
        
    def test_replace_abbreviation_abbreviations_file(self, abbreviation, expected_replacement):
        pre_process_data = PreProcessData(abbreviations_file=root_path + '/data/dicts/mexico_abbreviations.csv')
        assert pre_process_data._replace_abbreviation(abbreviation) == expected_replacement
