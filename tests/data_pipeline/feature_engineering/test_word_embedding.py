import numpy as np

from src.data_pipeline.feature_engineering.word_embedding import WordEmbedding

class TestWordEmbedding:
    def setup_method(self):
        self.we = WordEmbedding()
        
    def test_get_embedding(self):
        text = "This is a text"
        expected = [0.06799883, 0.17547965, 0.47599664, 0.16108984, -0.1360625, -0.10632467,
                    -0.10654568, -0.09805, -0.33004168, -0.33528003, -0.23304085, 0.36661038,
                    -0.5797167, 0.53252834, 0.30276018, -0.01584417, 0.85087484, 0.14121284,
                    0.74862367, -0.33011952, 0.015432, 0.02694534, 0.10118082, -0.34017918,
                    -0.14560167]
        lang = "es"
        dimensions = 25
        result = self.we.get_embedding(text, lang, dimensions)
        assert np.allclose(result, expected)