import os
from pandas import read_csv

from parser.parser import YAMLParser
from parser.treatment.feature_engineering.parser import FeatureEngineering

class Generator():
    
    def __init__(self, dir):
        self.dir = dir
        self.yamls_dir = os.listdir(dir)
    

    def generate_dags(self):
        initialParser = YAMLParser
        featureEngineringParser = FeatureEngineering

        for file in self.yamls_dir:
            dag = initialParser(filepath=os.path.join(self.dir, file)).parse()
            
            for path in dag['data_path']:
                csv = read_csv(path)
                return featureEngineringParser(csv).parser(dag['feature_engineering'])
            

