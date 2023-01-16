from hygia.parser.parser_base import ParserBase

class PreProcessingParser(ParserBase):
    
    def __init__(self, columns_name):
        self.columns_name = columns_name
        
    def parse(self, data: list):
        return self._parse_pre_processing_configs(data)
        
    def _parse_pre_processing_configs(self, data: list):
        if(not data): return
        
        aliases = self._try_get(data, 'aliases')
        self._get_dataframe(aliases)
        
        return aliases, self.columns_name
    
    def _get_dataframe(self, aliases: dict):
        if(not aliases): return 
        
        for alias in aliases:
            for key in alias.keys():
                if(not self._has_column_on_df(self.columns_name, alias)):
                    self.columns_name.append(key)
                
