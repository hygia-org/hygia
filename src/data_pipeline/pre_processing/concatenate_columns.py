import pandas as pd

def concatenate_columns(df: pd.DataFrame, columns_set: list):
    for columns in columns_set:
        for key, values in columns.items():
            for value in values:
                if(not key in df):
                    print(value)
                    print(key)
                    print(df)
                    df[key] = df[value].astype(str)
                    continue
                
                df[key] = df[key] + ' ' + df[value].astype(str)
    return df
