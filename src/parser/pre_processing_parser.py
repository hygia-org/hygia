from parser.parser_base import ParserBase

class PreProcessingParser(ParserBase):
    
    def __init__(self, columns_name):
        self.columns_name = columns_name
        
    def parse(self, data: list):
        return self._parse_pre_processing_configs(data)
        
    def _parse_pre_processing_configs(self, data: list):
        if(not data): return
        
        columns = self._try_get(data, 'columns')
        columns_alias = self._get_dataframe(columns)
        
        
        for alias in columns_alias:   
            if(not self._has_column_on_df(self.columns_name, alias)):
                self.columns_name.append(alias)
        
        return columns, self.columns_name
    
    def _get_dataframe(self, columns: dict):
        if(not columns): return 
        
        columns_alias = []
        
        for column in columns:
            for key in column.keys():
                columns_alias.append(key)
                
        return columns_alias

