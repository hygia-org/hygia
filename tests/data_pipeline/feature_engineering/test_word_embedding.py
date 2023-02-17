import pytest
import pandas as pd
import numpy as np

from hygia import WordEmbedding

class TestWordEmbedding:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.word_embedding = WordEmbedding()

    def test_pre_embedding(self):
        text = 'A test with ABC123 AVENUE'
        pre_embedding = self.word_embedding._WordEmbedding__pre_embedding(text)
        assert pre_embedding == 'test with AVENUE'

    def test_get_embedding(self):
        embedding = self.word_embedding.get_embedding("This is a sample text.")
        assert isinstance(embedding, np.ndarray)

    def test_extract_word_embedding_features(self):
        df = pd.DataFrame({"text_column": ["This is a sample text.", "Another sample text."]})
        result = self.word_embedding.extract_word_embedding_features(df, "text_column")
        assert isinstance(result, pd.DataFrame)
        assert any(col.startswith("feature_we_") for col in result.columns)
