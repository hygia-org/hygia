import pandas as pd
from colorama import Fore, Style

from hygia.data_pipeline.feature_engineering.key_smash import KeySmash
from hygia.data_pipeline.feature_engineering.word_embedding import WordEmbedding
from hygia.data_pipeline.feature_engineering.regex import Regex

class FeatureEngineering:
    """
    A class for extracting key smashing and word embedding features from text data.
    This class combines the functionality of the KeySmash and WordEmbedding classes
    to extract key smashing and word embedding features from a given text column in a dataframe.

    Examples
    --------
    Use this class like this:

    .. code-block:: python

        feature_engineer = FeatureEngineering()
        df = feature_engineer.extract_features(df, "text_column")
        print(df)
    """

    def __init__(self, lang: str = 'es', dimensions: int = 25, model: str = 'bytepair'):
        """
        Initialize the FeatureEngineering class.
        
        :param lang: The language of the text to be processed. (default 'es')
        :type lang: str
        :param dimensions: The number of dimensions of the word embedding vectors. (default 25)
        :type dimensions: int
        :param model: The word embedding model to be used. (default 'bytepair')
        :type model: str
        """
        print(f'{Fore.YELLOW}running feature engineering with configs below...{Fore.WHITE}')
        
        print(f'{Style.BRIGHT}language -> {Style.NORMAL}{lang}')
        print(f'{Style.BRIGHT}dimensions -> {Style.NORMAL}{dimensions}')
        
        
        self.key_smash = KeySmash()
        self.word_embedding = WordEmbedding(lang=lang, dimensions=dimensions, model=model)
        self.regex = Regex()

    def extract_features(self, df: pd.DataFrame, text_column: str) -> pd.DataFrame:
        """
        Extract key smashing and word embedding features from a given dataframe and column.

        :param df: Dataframe to extract features from.
        :type df: pandas.DataFrame
        :param text_column: Name of the column in the dataframe that contains the text data to extract features from.
        :type text_column: str
        :param normalize: Indicates whether to normalize the feature columns. Default is True.
        :type normalize: bool, optional

        :return: The input dataframe with additional columns for key smashing and word embedding features.
        :rtype: pandas.DataFrame

        Examples
        --------
        Use this class like this:

        .. code-block:: python

            fe = FeatureEngineering()
            df = fe.extract_features(df, "text_column")
            print(df)
        """
        print(f'extract features from -> {text_column}')
        
        df = self.key_smash.extract_key_smash_features(df, text_column)
        df = self.word_embedding.extract_word_embedding_features(df, text_column)
        df = self.regex.extract_regex_features(df, text_column)
        return df
