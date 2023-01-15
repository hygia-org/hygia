import pandas as pd
import pytest
from typing import Any, List

from src.data_pipeline.feature_engineering.feature_engineering import FeatureEngineering

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
        assert 'feature_ks_count_sequence_squared_vowels' in df.columns
        assert 'feature_ks_count_sequence_squared_consonants' in df.columns
        assert 'feature_ks_count_sequence_squared_special_characters' in df.columns
        assert 'feature_ks_ratio_of_numeric_digits_squared' in df.columns
        assert 'feature_ks_average_of_char_count_squared' in df.columns
        assert 'feature_we_0' in df.columns

    def test_extract_features_with_normalization(self, feature_engineering, dataframe):
        df = feature_engineering.extract_features(dataframe, 'text_column')
        for i in range(25):
            assert df[f'feature_we_{i}'].min() == 0
            assert df[f'feature_we_{i}'].max() == 1
