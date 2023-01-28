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
            thresholds = self.get_thresholds(input)
            
            configs.append({
                        'columns': columns,
                        'thresholds': thresholds,
                    })
        
        return configs
    
    def get_thresholds(self, input=None):
        thresholds = self._get(input, 'thresholds', self.default_thresholds)
            
        for key, alias in self.default_thresholds.items():
            if(not(key in thresholds.keys())):
                thresholds[key] = alias
                
        return thresholds
