import os
import pandas as pd

from parser.YAML_parser import YAMLParser
from parser.pre_processing_parser import PreProcessingParser
# from parser.feature_engineering_parser import FeatureEngineeringParser
# from parser.model_parser import ModelParser
# from data_pipeline.model.random_forest import RandomForestAddress

if __name__ != "__main__":
    exit()   
    
def get_config():
    initialParser = YAMLParser
    preProcessingParser = PreProcessingParser
    # featureEngineringParser = FeatureEngineeringParser
    # modelParser = ModelParser
    
    for file in os.listdir('src/yamls'):
        filepath = os.path.join('src/yamls', file)
        config = initialParser(filepath).parse()
        
        for data in config['data_path']:
            df = pd.read_csv(data)
            columns_name = list(df.columns)
            
            columns_set, columns_name = preProcessingParser(columns_name).parse(config['pre_processing'])
    
            # features_configs, columns_set_alias = featureEngineringParser(filepath).parse(config['feature_engineering'])
            # del config['feature_engineering']
            
            # model_configs = modelParser(columns_set_alias).parse(config['model'])
            # del config['model']
            
            # for feature_config in features_configs:
        
        print("FEATURES")
        print(columns_set)
        print(3*'\n')
        print(20*'-')
        print(3*'\n')
        print(columns_name)
    
    # IF 
    # rfa = RandomForestAddress('data_paths', model_configs, features_configs)
    # rfa.run()
         
get_config()
