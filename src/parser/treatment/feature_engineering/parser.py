from pandas import DataFrame

class FeatureEngineering():
    
    def __init__(self, csv):
        self.csv = csv

    def parser(self, feature: dict):
        return self._parser_feature_engineering(feature)
        
    def _parser_feature_engineering(self, feature: dict):
        if(not feature): return

        return self._keyboard_smash_parser(feature.get('keyboard_smash', None))

    def _keyboard_smash_parser(self, keyboard_smash: dict):
        if(not keyboard_smash): return
        
        columns = keyboard_smash.get('columns', None)
        dags = []
        for column in columns:
            dags.append(self._get_concatenated_column(column))
            
        return dags
        
    def _get_concatenated_column(self, column):
        if(type(column) == str):
            return DataFrame(self.csv[column])
        
        value_name = ''
        for value in column:
            if (value_name != ''): 
                self.csv[value_name + value] = self.csv[value_name].astype(str) + ' ' + self.csv[value].astype(str)
                if (value_name != last_value): del self.csv[value_name]
                
            last_value = value
            value_name = value_name + value        
            
        return DataFrame(self.csv[value_name])