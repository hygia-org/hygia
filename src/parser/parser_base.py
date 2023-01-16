import os

class ParserBase():
    
    def __init__(self, filepath = 'src/yamls/config.yaml'):
        self.filepath = filepath
    
    def _try_get(self, variable: dict, field, error_msg=None):
        try:
            return variable[field]
        except KeyError:
            if not error_msg:
                error_msg = f'the field `{field}` is required.'
            file_name = self.filepath.split('/')[-1]
            error_msg = f'Error in file {file_name}: {error_msg}'
            raise ValueError(error_msg)
        
    def _has_column_on_df(self, df_columns_alias: list, column_alias: str):
        return column_alias in df_columns_alias
        
    def _get(self, variable: dict, field, default_value):
        try:
            return variable[field]
        except:
            return default_value