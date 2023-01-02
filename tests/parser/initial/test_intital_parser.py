
from src.parser.initial.parser import YAMLParser

class TestYamlParser():

    def setup_method(self):
        yamlParser = YAMLParser
        self.yaml = yamlParser('tests/mock/success/yaml_mock.yaml').parse()
    
    def test_yaml_has_path(self):
        assert 'data_path' in self.yaml
        assert 'tests/mock/data_mock.csv' in self.yaml['data_path']
        
    def test_yaml_has_id(self):
        assert 'dag_id' in self.yaml
        assert self.yaml['dag_id'] == 'basic_example'
        
    def test_yaml_has_description(self):
        assert 'description' in self.yaml
        assert self.yaml['description'] == 'DAG de teste'
        
    def test_yaml_has_feature_settings(self):
        assert 'output_folder' in self.yaml
        assert self.yaml['output_folder'] == 'output'
        
    def test_yaml_has_feature_settings(self):
        assert 'feature_engineering' in self.yaml
        assert type(self.yaml['feature_engineering']) == list
        assert 'input' in self.yaml['feature_engineering'][0]
