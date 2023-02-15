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

    Examples - 
    Use this class like this:

    \code{.py}

        feature_engineer = FeatureEngineering()
        df = feature_engineer.extract_features(df, "text_column")
        print(df)
    \endcode
    """

    def __init__(self, lang:str='es',
                 dimensions:int=25,
                 model:str='bytepair',
                 country:str=None,
                 context_words_file:str=None,
                 ignore_word_embedding:bool=False,
                 ignore_ratio_of_numeric_digits_squared:bool=True,
                 ignore_shannon_entropy:bool=True) -> None:
        """
        Initialize the FeatureEngineering class.
        
        \param lang (Type: str) The language of the text to be processed. (default 'es')
        \param dimensions (Type: int) The number of dimensions of the word embedding vectors. (default 25)
        \param model (Type: str) The word embedding model to be used. (default 'bytepair')
        """
        print(f'{Fore.YELLOW}running feature engineering with configs below...{Fore.WHITE}')
        print(f'{Style.BRIGHT}language -> {Style.NORMAL}{lang}')
        print(f'{Style.BRIGHT}dimensions -> {Style.NORMAL}{dimensions}')
        
        self.ignore_word_embedding = ignore_word_embedding
        self.key_smash = KeySmash(ignore_ratio_of_numeric_digits_squared, ignore_shannon_entropy)
        self.word_embedding = WordEmbedding(lang=lang, dimensions=dimensions, model=model)
        self.regex = Regex(country=country, context_words_file=context_words_file)

    def extract_features(self, df: pd.DataFrame, text_column: str) -> pd.DataFrame:
        """
        Extract key smashing and word embedding features from a given dataframe and column.

        \param df (Type: DataFrame) Dataframe to extract features from.
        \param text_column (Type: str) Name of the column in the dataframe that contains the text data to extract features from.
        \param normalize (Type: bool, optional) Indicates whether to normalize the feature columns. Default is True.

        \return (Type: DataFrame) The input dataframe with additional columns for key smashing and word embedding features.

        Examples - 
        Use this class like this:

        \code{.py}

            fe = FeatureEngineering()
            df = fe.extract_features(df, "text_column")
            print(df)
        \endcode
        """
        print(f'extract features from -> {text_column}')
        
        df = self.key_smash.extract_key_smash_features(df, text_column)
        if not self.ignore_word_embedding:
            df = self.word_embedding.extract_word_embedding_features(df, text_column)
        df = self.regex.extract_regex_features(df, text_column)
        return df
