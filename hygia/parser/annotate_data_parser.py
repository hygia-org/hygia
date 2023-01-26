from hygia.parser.parser_base import ParserBase

class AnnotateDataParser(ParserBase):
    
    def __init__(self):
        self.default_thresholds = {
            'ksmash_sequence_vowels': 1.00,
            'ksmash_sequence_consonants': 1.999,
            'ksmash_sequence_special_characters': 2.2499,
            'ksmash_numbers': 2.9,
            'ksmash_char_frequence': 2.78
        }
    
    def parse(self, data: list):
        return self._parse_annotate_data_configs(data)
        
    def _parse_annotate_data_configs(self, data: list):
        if(not data): return
        
        configs = []
        
        for inputs in data:
            input = self._try_get(inputs, 'input')
            columns = self._try_get(input, 'columns')
            thresholds = self._try_get(input, 'thresholds')
            
            configs.append({
                        'columns': columns,
                        'thresholds': thresholds,
                    })
        
        return configs
    
    def get_thresholds(self, input, columns_alias):
        thresholds = self._try_get(input, 'thresholds')
        
        thresholds_default = self.get_default_thresholds(columns_alias)
        thresholds = self._get(thresholds, 'thresholds', thresholds_default)
            
        for key in thresholds.keys():
            if(not(key in columns_alias)):
                raise ValueError(f'`{key}` key not match with the available columns')
            
        for alias in columns_alias:
            if(not(alias in thresholds.keys())):
                thresholds[alias] = self.default_thresholds
                
        return thresholds
    
    def get_default_thresholds(self, columns_alias):
        default_config = []
        
        for alias in columns_alias:
            default_config.append({alias: self.default_thresholds})
            
        return default_config
        
