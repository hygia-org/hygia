import os

from parser import YAMLParser

class Generator():

    dir = 'yamls'
    YAMLS_DIR = os.listdir(dir)
    parser = YAMLParser

    def generate_dags(self):

        for file in self.YAMLS_DIR:
            dag_specs = self.parser(
                filepath=os.path.join(self.dir, file)).parse()
            print(dag_specs)
            
Generator().generate_dags()

