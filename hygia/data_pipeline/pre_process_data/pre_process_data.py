import pandas as pd
import re
from colorama import Style
from hygia.paths.paths import root_path

class PreProcessData:
    """
    This class presents a series of functions that help in data pre-processing.
    As concatenate columns, replace abbreviation, and etc.


    Examples
    --------
    Use this class like this:

    .. code-block:: python
        pre_process_data = hg.PreProcessData()
        df = pre_process_data.pre_process_data(df, ['COLUMN_1', 'COLUMN_2'], concatened_column_name)
        print(df)
    """
    def __init__(self, country:str=None, abbreviations_file:str=None) -> None:
        """
        Initialize the PreProcessData class.
        
        :param country: Zipcode list of the region or country used.
        :type country: str
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
        
        :param df: Dataframe.
        :type df: pandas.DataFrame

        :param columns: List of columns
        :type columns: List

        :param concatenated_column_name: Name of the new column
        :type concatenated_column_name: str

        :return: Return the columns concatenated
        """

        print(f'aliases indified: {Style.BRIGHT}{concatenated_column_name} -> {Style.NORMAL}{columns}')
        
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def handle_nulls(self, df, column_name):
        """
        Handle null values
        
        :param df: Dataframe
        :type df: pandas.DataFrame

        :param column_name: Column name to check
        :type column_name: str
        """
        print(f'handle null values in the column {Style.BRIGHT}{column_name}{Style.NORMAL}')
        
        df[column_name].fillna('').astype(str)
        return df

    def handle_extra_spaces(self, df, column_name:str) -> str:
        df[column_name] = df[column_name].apply(lambda x: ' '.join(x.split()))
        return df
    
    def _replace_abbreviation(self, text:str) -> str:
        """
        Function that identifies abbreviations and according to the dictionary changes the names
        
        :param text: Text to be analyzed
        :type text: str
        """
        for abbreviation in self.abbreviations_dict:
            text = ' '.join([re.sub(rf'(\b|(?<=[^a-zA-Z])){abbreviation}(\.|\b|(?=[^a-zA-Z]))', self.abbreviations_dict[abbreviation], e, flags=re.IGNORECASE) for e in text.split()])
        return text
    
    def handle_abreviations(self, df, column_name):
        """
        Handles abbreviations in the dataframe
        
        :param df: Dataframe
        :type df: DataFrame

        :param column_name: Column name to check
        :type column_name: str
        """

        df[column_name] = df[column_name].apply(lambda x: self._replace_abbreviation(x))
        return df
    
    def pre_process_data(self, df, columns_to_concat=None, column_name=None):
        """
        Function that gathers all implemented preprocessing (column concatenation, handle with nulls and abbreviations)
        
        :param df: Dataframe
        :type df: DataFrame

        :param columns_to_concat: List of columns
        :type columns_to_concat: List

        :param column_name: Column name to check
        :type column_name: str

        :return: The input dataframe with additional columns
        :rtype: pandas.DataFrame
        """
        if columns_to_concat and column_name:
            df = self.concatenate_columns(df, columns_to_concat, column_name)
        
        if column_name and column_name in df.columns:
            df = self.handle_nulls(df, column_name)
            df = self.handle_extra_spaces(df, column_name)
            df = self.handle_abreviations(df, column_name)
        
        return df
