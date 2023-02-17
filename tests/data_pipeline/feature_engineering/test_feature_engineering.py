import pandas as pd
import pytest
from typing import Any, List

from hygia import FeatureEngineering

class TestFeatureEngineering:

    @pytest.fixture
    def dataframe(self):
        df = pd.DataFrame({'text_column': ['Hello World!', 'Hello again!', 'Goodbye for now']})
        return df

    @pytest.fixture
    def feature_engineering(self):
        return FeatureEngineering()

    def test_extract_features(self, feature_engineering, dataframe):
        df = feature_engineering.extract_features(dataframe, 'text_column')
        assert 'feature_ks_count_sequence_squared_vowels_text_column' in df.columns
        assert 'feature_ks_count_sequence_squared_consonants_text_column' in df.columns
        assert 'feature_ks_count_sequence_squared_special_characters_text_column' in df.columns
        assert 'feature_ks_average_of_char_count_squared_text_column' in df.columns
        assert 'feature_we_0_text_column' in df.columns
