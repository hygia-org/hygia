from hygia.parser.YAML_parser import YAMLParser

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
    
    def test_yaml_has_model(self):
        assert 'model' in self.yaml
        assert self.yaml['model'] == 'model'

    def test_yaml_has_nrows(self):
        assert 'nrows' in self.yaml
    
    def test_yaml_has_engine(self):
        assert 'engine' in self.yaml

    def test_yaml_has_encoding(self):
        assert 'encoding' in self.yaml

    def test_yaml_has_separator(self):
        assert 'separator' in self.yaml

    def test_yaml_has_model(self):
        assert 'model' in self.yaml
        assert self.yaml['model'] == 'model'

    def test_yaml_has_annotate_data(self):
        assert 'annotate_data' in self.yaml
        assert self.yaml['annotate_data'] == 'annotate_data'

    def test_yaml_has_preprocessing(self):
        assert 'pre_processing' in self.yaml
        assert self.yaml['pre_processing'] == 'pre_processing'
