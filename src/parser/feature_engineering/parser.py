from data_pipeline.pre_processing.concatenate_columns import get_concatenated_column

class FeatureEngineering():
    
    def __init__(self, csv):
        self.csv = csv

    def parse(self, feature: dict):
        return self._parser_feature_engineering(feature)
        
    def _parser_feature_engineering(self, feature: dict):
        if(not feature): return

        return self._keyboard_smash_parser(feature.get('keyboard_smash', None))

    def _keyboard_smash_parser(self, keyboard_smash: dict):
        if(not keyboard_smash): return
        
        columns = keyboard_smash.get('columns', None)
        dags = []
        for column in columns:
            dags.append(get_concatenated_column(self.csv, column))
            
        return dags
        
