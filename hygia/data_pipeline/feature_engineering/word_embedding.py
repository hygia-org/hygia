from typing import List, Any
import numpy as np
from whatlies.language import BytePairLanguage
# from whatlies.language import FastText
# from whatlies.language import Word2Vec
# from whatlies.language import Glove
# from whatlies.language import BagOfWords
import pandas as pd
import re

class WordEmbedding:
    """
    A class for generating word embeddings from text data.
    Word embeddings are numerical representations of text data that capture the context and meaning of words within a sentence or document.

    Examples - 
    Use this class like this:

    \code{.py}

        word_embedding = WordEmbedding()
        df = word_embedding.extract_word_embedding_features(df, "text_column")
        print(df)
    \endcode
    """

    def __init__(self, lang: str = 'es', dimensions: int = 25, model: str = 'bytepair'):
        """
        Initialize the WordEmbedding class.

        \param lang (Type: str) The language of the text to be processed. (default 'es')
        \param dimensions (Type: int) The number of dimensions of the word embedding vectors. (default 25)
        \param model (Type: str) The word embedding model to be used. (default 'bytepair')
        """
        self.lang = lang
        self.dimensions = dimensions
        self.model = model
        self.word_embedding_model = self._load_model()

    def _load_model(self) -> Any:
        """
        Load the word embedding model.

        \return (Type: Any) The loaded word embedding model.
        """
        if self.model == 'bytepair':
            return BytePairLanguage(lang=self.lang, dim=self.dimensions)
        elif self.model == 'fasttext':
            raise NotImplementedError
        elif self.model == 'word2vec':
            raise NotImplementedError
        elif self.model == 'glove':
            raise NotImplementedError
        elif self.model == 'bagofwords':
            raise NotImplementedError
        else:
            raise ValueError
    
    def _pre_embedding(self, text: str) -> str:
        text = ' '.join(e for e in text.split() if e.isalpha() and len(e) >= 3 and not e.isspace())
        return text
        
    def get_embedding(self, text: str) -> np.ndarray:
        """
        Get the word embedding vector for a given text.
        
        Examples - 
        Use this function like this:
        
        \code{.py}
            word_embedding = WordEmbedding()
            embedding = word_embedding.get_embedding("This is a sample text.")
            print(embedding)
            # Output: [0.1, 0.2, ..., 0.3] (a list of float values representing the word embedding vector)

            embedding = word_embedding.get_embedding("Another sample text.")
            print(embedding)
            # Output: [0.5, 0.6, ..., 0.7] (a list of float values representing the word embedding vector)
        \endcode

        \param text (Type: str) The text to be processed.
        
        \return (type: array) A word embedding vector for the given text.
        """
        
        empty_vector = [0.0] * self.dimensions

        text = self._pre_embedding(text)
        
        # White space string
        if len(text.strip().split()) == 0:
            return empty_vector
        
        return self.word_embedding_model[text].vector
    
    def extract_word_embedding_features(self, df: pd.DataFrame, column_name: str, normalize: bool = False) -> pd.DataFrame:
        """
        Extract word embedding features from a given dataframe and column.

        Examples - 
        Use this class like this:

        \code{.py}

            word_embedding = WordEmbedding()
            df = pd.DataFrame({"text_column": ["abcdefgh", "ijklmnop", "qrstuvwxyz"]})
            df = word_embedding.extract_features(df, "text_column", normalize=False)
            print(df.head())
        \endcode

        \param df (Type: DataFrame) Dataframe to extract word embedding features from.
        \param column_name (Type: str) Name of the column in the dataframe that contains the text data to extract features from.
        \param normalize (Type: bool, optional) Indicates whether to normalize the word embedding feature columns. Default is True.

        \return (Type: DataFrame) The input dataframe with additional columns for word embedding features.
        """
        
        feature_we_tmp = df[column_name].fillna('').apply(lambda x: self.get_embedding(x))
        
        for i in range(self.dimensions):
            df[f'feature_we_{i}_{column_name}'] = feature_we_tmp.apply(lambda x: x[i])

        if normalize:
            for i in range(self.dimensions):
                df[f'feature_we_{i}_{column_name}'] = (df[f'feature_we_{i}_{column_name}'] - df[f'feature_we_{i}_{column_name}'].min()) / (df[f'feature_we_{i}_{column_name}'].max() - df[f'feature_we_{i}_{column_name}'].min())
        
        return df
        