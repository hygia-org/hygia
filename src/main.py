import os
from pandas import read_csv

from parser.initial.parser import YAMLParser
from parser.feature_engineering.parser import FeatureEngineering

if __name__ != "__main__":
    exit()   

def get_config():
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineering

    for file in os.listdir('src/yamls'):
        config = initialParser(filepath=os.path.join('src/yamls', file)).parse()
        
        for path in config['data_path']:
            csv = read_csv(path)
            print(featureEngineringParser(csv).parse(config['feature_engineering']))
            
        del config['feature_engineering']
         
get_config()
