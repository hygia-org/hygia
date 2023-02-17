import pytest
import pandas as pd
import numpy as np
from whatlies.language import BytePairLanguage

from hygia import WordEmbedding

class TestWordEmbedding:
    def setup_method(self):
        self.word_embedding = WordEmbedding()

    def test_load_model(self):
        assert isinstance(self.word_embedding.__load_model(), BytePairLanguage)
    
    def test_get_embedding(self):
        embedding = self.word_embedding.get_embedding("This is a sample text.")
        assert isinstance(embedding, np.ndarray)

    def test_pre_embedding(self):
        assert self.word_embedding.__pre_embedding("A test with ABC123 AVENUE") == "test with AVENUE"

    def test_extract_word_embedding_features(self):
        df = pd.DataFrame({"text_column": ["This is a sample text.", "Another sample text."]})
        result = self.word_embedding.extract_word_embedding_features(df, "text_column")
        assert isinstance(result, pd.DataFrame)
        assert any(col.startswith("feature_we_") for col in result.columns)