import os
import pandas as pd

from parser.YAML_parser import YAMLParser

from parser.pre_processing_parser import PreProcessingParser
from data_pipeline.pre_processing.concatenate_columns import concatenate_columns

from parser.feature_engineering_parser import FeatureEngineeringParser
from data_pipeline.feature_engineering.key_smash import KeySmash

# from parser.model_parser import ModelParser

# from data_pipeline.model.random_forest import RandomForestAddress

if __name__ != "__main__":
    exit()   
    
def get_config():
    initialParser = YAMLParser
    
    preProcessingParser = PreProcessingParser
    
    featureEngineringParser = FeatureEngineeringParser
    keySmash = KeySmash
    
    # modelParser = ModelParser
    
    for file in os.listdir('src/yamls'):
        filepath = os.path.join('src/yamls', file)
        config = initialParser(filepath).parse()
        
        for data in config['data_path']:
            df = pd.read_csv(data)
            columns_name = list(df.columns)
            
            columns_set, columns_name = preProcessingParser(columns_name).parse(config['pre_processing'])
            df = concatenate_columns(df, columns_set)
    
            features_configs = featureEngineringParser(columns_name).parse(config['feature_engineering'])
            for config in features_configs:
                for column in config['columns']:
                    df = keySmash().extract_key_smash_features(df, column)
            
            # model_configs = modelParser(columns_set_alias).parse(config['model'])
            # del config['model']
            
            # for feature_config in features_configs:
            
        del config['pre_processing']
        del config['feature_engineering']
        
        print("FEATURES")
        print(features_configs)
        print(3*'\n')
        print(20*'-')
        print(3*'\n')
        print(columns_name)
    
    # IF 
    # rfa = RandomForestAddress('data_paths', model_configs, features_configs)
    # rfa.run()
         
get_config()
