import pandas as pd
import re
from colorama import Style
class PreProcessData:
    def __init__(self, country:str=None, abbreviations_file:str=None) -> None:
        self.abbreviations_dict = {}
        if not country and not abbreviations_file:
            return
        country_mappings = {
            'MEXICO': {'code': 'MX', 'abbrevitations_file': '../data/dicts/mexico_abbreviations.csv'},
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
        print(f'aliases indified: {Style.BRIGHT}{concatenated_column_name} -> {Style.NORMAL}{columns}')
        
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def handle_nulls(self, df, column_name):
        print(f'handle null values in the column {Style.BRIGHT}{column_name}{Style.NORMAL}')
        
        df[column_name].fillna('').astype(str)
        return df
    
    def _replace_abbreviation(self, text:str) -> str:
        for abbreviation in self.abbreviations_dict:
            text = ' '.join([re.sub(rf'(\b|(?<=[^a-zA-Z])){abbreviation}(\b|(?=[^a-zA-Z]))', self.abbreviations_dict[abbreviation], e, flags=re.IGNORECASE) for e in text.split()])
        return text
    
    def handle_abreviations(self, df, column_name):
        df[column_name] = df[column_name].apply(lambda x: self._replace_abbreviation(x))
        return df
    
    def pre_process_data(self, df, columns_to_concat=None, column_name=None):
        
        if columns_to_concat and column_name:
            df = self.concatenate_columns(df, columns_to_concat, column_name)
        
        if column_name and column_name in df.columns:
            df = self.handle_nulls(df, column_name)
            df = self.handle_abreviations(df, column_name)
        
        return df
