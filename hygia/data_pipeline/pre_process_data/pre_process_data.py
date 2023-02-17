import pandas as pd
import re
from colorama import Style
from hygia.paths.paths import root_path

class PreProcessData:
    """
    This class presents a series of functions that help in data pre-processing.
    As concatenate columns, replace abbreviation, and etc.
    
    Some abbreviations were taken from this website: https://en.wikipedia.org/wiki/Template:Mexico_State-Abbreviation_Codes

    Examples - 
    Use this class like this:

    \code{.py}
        pre_process_data = hg.PreProcessData()
        df = pre_process_data.pre_process_data(df, ['COLUMN_1', 'COLUMN_2'], concatened_column_name)
        print(df)
    \endcode
    """
    def __init__(self, country:str=None, abbreviations_file:str=None) -> None:
        """
        Initialize the PreProcessData class.
        
        \param country (Type: str) Zipcode list of the region or country used.
        """
        self.abbreviations_dict = {}
        if not country and not abbreviations_file:
            return
        country_mappings = {
            'MEXICO': {'code': 'MX', 'abbrevitations_file': root_path + '/data/dicts/mexico_abbreviations.csv'},
        }
        if country:
            abbreviations_file_path = country_mappings[country]['abbrevitations_file']
        if abbreviations_file:
            abbreviations_file_path = abbreviations_file
        with open(abbreviations_file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split(',')
                self.abbreviations_dict.update({key: value})
    
    def concatenate_columns(self, df, columns, concatenated_column_name):
        """
        Function that concatenates two columns and saves in a new one, whose name is informed by the user.
        
        \param df (Type: DataFrame) Dataframe.

        \param columns (Type: List) List of columns

        \param concatenated_column_name (Type: str) Name of the new column

        \return  Return the columns concatenated
        """

        print(f'aliases indified: {Style.BRIGHT}{concatenated_column_name} -> {Style.NORMAL}{columns}')
        
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def handle_nulls(self, df, column_name):
        """
        Handle null values
        
        \param df (Type: Dataframe) Dataframe

        \param column_name (Type: str) Column name to check
        """
        print(f'handle null values in the column {Style.BRIGHT}{column_name}{Style.NORMAL}')
        
        df[column_name] = df[column_name].fillna('').astype(str)
        return df

    def handle_extra_spaces(self, df, column_name:str) -> str:
        df[column_name] = df[column_name].apply(lambda x: ' '.join(x.split()))
        return df
    
    def __replace_abbreviation(self, text:str) -> str:
        """
        Function that identifies abbreviations and according to the dictionary changes the names
        
        \param text (Type: str) Text to be analyzed
        """
        for abbreviation in self.abbreviations_dict:
            text = ' '.join([re.sub(rf'(\b|(?<=[^a-zA-Z])){abbreviation}(\.|\b|(?=[^a-zA-Z]))', self.abbreviations_dict[abbreviation], e, flags=re.IGNORECASE) for e in text.split()])
        return text
    
    def handle_abreviations(self, df, column_name):
        """
        Handles abbreviations in the dataframe
        
        \param df (Type: DataFrame) Dataframe

        \param column_name (Type: str) Column name to check
        """

        df[column_name] = df[column_name].apply(lambda x: self.__replace_abbreviation(x))
        return df
    
    def pre_process_data(self, df, columns_to_concat=None, column_name=None):
        """
        Function that gathers all implemented preprocessing (column concatenation, handle with nulls and abbreviations)
        
        \param df (Type: DataFrame) Dataframe
        \param columns_to_concat (Type: List) List of columns
        \param column_name (Type: str) Column name to check

        \return (Type: DataFrame) The input dataframe with additional columns
        """
        if columns_to_concat and column_name:
            df = self.concatenate_columns(df, columns_to_concat, column_name)
        
        if column_name and column_name in df.columns:
            df = self.handle_nulls(df, column_name)
            df = self.handle_extra_spaces(df, column_name)
            df = self.handle_abreviations(df, column_name)
        
        return df
