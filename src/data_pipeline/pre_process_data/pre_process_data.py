import pandas as pd

class PreProcessData:
    def concatenate_columns(self, df, columns):
        df[f"concat_{'_'.join(columns)}"] = df[columns].astype(str).agg(' '.join, axis=1)
        df[f"concat_{'_'.join(columns)}"] = df[f"concat_{'_'.join(columns)}"].str.replace(r'  +', 'EMPTY', regex=True).astype('str')
        return df
    
    def pre_process_data(self, df, columns_to_concat):
        df = self.concatenate_columns(df, columns_to_concat)
        return df

