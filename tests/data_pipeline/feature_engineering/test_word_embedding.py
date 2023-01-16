import pytest
import pandas as pd
import numpy as np
from whatlies.language import BytePairLanguage
from src.data_pipeline.feature_engineering.word_embedding import WordEmbedding

class TestWordEmbedding:

    @pytest.fixture
    def word_embedding(self):
        return WordEmbedding()

    def test_load_model(self, word_embedding):
        assert isinstance(word_embedding._load_model(), BytePairLanguage)

    def test_get_embedding(self, word_embedding):
        embedding = word_embedding.get_embedding("This is a sample text.")
        assert isinstance(embedding, np.ndarray)

    def test_extract_word_embedding_features(self, word_embedding):
        df = pd.DataFrame({"text_column": ["This is a sample text.", "Another sample text."]})
        result = word_embedding.extract_word_embedding_features(df, "text_column")
        assert isinstance(result, pd.DataFrame)
        assert any(col.startswith("feature_we_") for col in result.columns)