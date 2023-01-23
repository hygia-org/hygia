import pandas as pd

class PreProcessData:
    def concatenate_columns(self, df, columns, concatenated_column_name):
        df[concatenated_column_name] = df[columns].astype(str).agg(' '.join, axis=1)
        return df
    
    def pre_process_data(self, df, columns_to_concat, concatenated_column_name):
        df = self.concatenate_columns(df, columns_to_concat, concatenated_column_name)
        return df

