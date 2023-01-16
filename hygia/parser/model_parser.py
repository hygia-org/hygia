from hygia.parser.parser_base import ParserBase
from hygia.parser.const import model_type

class ModelParser(ParserBase):
    
    def __init__(self, columns_alias):
        self.columns_alias = columns_alias
        self.default_keyboard_smash_values = {
            'ksmash_sequence_vowels': 1.00,
            'ksmash_sequence_consonants': 1.999,
            'ksmash_sequence_special_characters': 2.2499,
            'ksmash_numbers': 2.9,
            'ksmash_char_frequence': 2.78
        }

    def parse(self, data: list):
        return self._parse_modal_configs(data)
        
    def _parse_modal_configs(self, data: list):
        if(not data): return
        
        random_forest = data.get('random_forest')
        
        if(random_forest):
            return self.get_random_forest_address_config(random_forest)
                
    def get_random_forest_address_config(self, model: list):
        configs = []

        for inputs in model:
            input = self._try_get(inputs, 'input', 'The inputs should be specified')
            type = self._try_get(input, 'type')
            trained_model_file = self._try_get(input, 'trained_model_file', 'Trained model should be provided')
        
            if (type == model_type['ADDRESS']):
                columns = self.get_columns(input)
                keyboard_smash, n_estimators, test_size = self.get_thresholds(input, columns)
                
                configs.append({
                    'model': 'keyboard_smash',
                    'trained_model_file': trained_model_file,
                    'type': model_type['ADDRESS'],
                    'columns': columns,
                    'keyboard_smash': keyboard_smash,
                    'n_estimators': n_estimators,
                    'test_size': test_size
                })
                
        return configs
            
    def get_columns(self, input):
        columns_set = self._try_get(input, 'columns')

        for alias in columns_set:
            if(not(alias in self.columns_alias)):
                raise ValueError(f'`{alias}` column not match with the available columns')
        
        return columns_set
        
    def get_thresholds(self, input, columns_alias):
        thresholds = self._try_get(input, 'thresholds')
        
        test_size = self._get(thresholds, 'test_size', 0.3)
        n_estimators = self._get(thresholds, 'n_estimators', 100)
        
        keyboard_smash_default = self.get_keyboard_smash_default_thresholds(columns_alias)
        keyboard_smash = self._get(thresholds, 'keyboard_smash', keyboard_smash_default)
            
        for key in keyboard_smash.keys():
            if(not(key in columns_alias)):
                raise ValueError(f'`{key}` key not match with the available columns')
            
        for alias in columns_alias:
            if(not(alias in keyboard_smash.keys())):
                keyboard_smash[alias] = self.default_keyboard_smash_values
                
        return keyboard_smash, n_estimators, test_size
    
    def get_keyboard_smash_default_thresholds(self, columns_alias):
        default_config = []
        
        for alias in columns_alias:
            default_config.append({alias: self.default_keyboard_smash_values})
            
        return default_config
    