import os
from pandas import read_csv

from parser import YAMLParser
from treatment.feature_engineering.parser import FeatureEngineering

class Generator():

    dir = 'src/yamls'
    YAMLS_DIR = os.listdir(dir)
    
    initialParser = YAMLParser
    featureEngineringParser = FeatureEngineering

    def generate_dags(self):

        for file in self.YAMLS_DIR:
            dag = self.initialParser(filepath=os.path.join(self.dir, file)).parse()
            
            for path in dag['data_path']:
                csv = read_csv(path)
                self.featureEngineringParser(csv).parser(dag['feature_engineering'])
            
Generator().generate_dags()

