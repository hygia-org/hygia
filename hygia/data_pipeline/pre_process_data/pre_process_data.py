import pandas as pd
from colorama import Style

class PreProcessData:
    def concatenate_columns(self, df, columns, concatenated_column_name):
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def handle_nulls(df, column_name):
        return df[column_name].fillna('').astype(str)
    
    def pre_process_data(self, df, columns_to_concat=None, column_name=None):
        print(f'aliases indified: {Style.BRIGHT}{column_name} -> {Style.NORMAL}{columns_to_concat}')
        
        if column_name:
            df = self.handle_nulls(df, column_name)
        if columns_to_concat and column_name:
            df = self.concatenate_columns(df, columns_to_concat, column_name)
        return df
