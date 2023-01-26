import pandas as pd
from colorama import Style

class PreProcessData:
    def concatenate_columns(self, df, columns, concatenated_column_name):
        print(f'aliases indified: {Style.BRIGHT}{concatenated_column_name} -> {Style.NORMAL}{columns}')
        
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def handle_nulls(self, df, column_name):
        print(f'handle null values in the column {Style.BRIGHT}{column_name}{Style.NORMAL}')
        
        df[column_name].fillna('').astype(str)
        return df
    
    def pre_process_data(self, df, columns_to_concat=None, column_name=None):
        
        if columns_to_concat and column_name:
            df = self.concatenate_columns(df, columns_to_concat, column_name)
        
        if column_name and column_name in df.columns:
            df = self.handle_nulls(df, column_name)
        
        return df
