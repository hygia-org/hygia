import pandas as pd
import pytest
from hygia.data_pipeline.augment_data.augment_data import AugmentData

@pytest.mark.parametrize("zipcode, expected", [
    ('20000', True),
    ('20997', True),
    ('01000', True),
    ('16900', True),
    ('1000', False),
    ('999999', False),
    ('00000', False),
    ('00001', False)
])
class TestAugmentData:
    def setup_method(self):
        self.augment_data = AugmentData()
    
    def test_validate_zipcode(self, zipcode, expected):
        assert self.augment_data.validate_zipcode(zipcode) == expected

    def test_validate_zipcodes(self, zipcode, expected):
        df = pd.DataFrame({'zipcode': [zipcode]})
        result = self.augment_data.validate_zipcodes(df, 'zipcode')
        assert result.equals(pd.DataFrame({'zipcode_is_valid': [expected]}))

    def test_augment_data(self, zipcode, expected):
        df = pd.DataFrame({'zipcode': [zipcode]})
        result = self.augment_data.augment_data(df, 'zipcode')
        expected_result = pd.DataFrame({'zipcode': [zipcode], 'zipcode_is_valid': [expected]})
        assert result.equals(expected_result)