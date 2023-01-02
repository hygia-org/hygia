import os

from parser.initial.parser import YAMLParser
from parser.feature_engineering.parser import FeatureEngineeringParser
from parser.model.parser import ModelParser

if __name__ != "__main__":
    exit()   

def get_config():
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineeringParser
    modelParser = ModelParser

    for file in os.listdir('src/yamls'):
        filepath = os.path.join('src/yamls', file)
        config = initialParser(filepath).parse()
    
        features, columns_set_alias = featureEngineringParser(filepath).parse(config['feature_engineering'])
        del config['feature_engineering']
        
        print("FEATURES")
        print(features)
        print(5*'\n')
        print(20*'-')
        print(5*'\n')
        
        print(modelParser(columns_set_alias).parse(config['model']))
        del config['model']
         
get_config()
