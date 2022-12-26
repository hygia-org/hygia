import pytest

from parser.initial.parser import YAMLParser

class TestYamlParser:

    yamlParser = YAMLParser
    yaml = yamlParser('src/parser/initial/tests/mock/ymal_mock.yaml').parse()
    
    def test_yaml_has_path(self):
        assert 'data_path' in self.yaml
        assert 'src/parser/tests/mock/data_mock.csv' in self.yaml['data_path']
        
    def test_yaml_has_id(self):
        assert 'dag_id' in self.yaml
        assert self.yaml['dag_id'] == 'basic_example'
        
    def test_yaml_has_description(self):
        assert 'description' in self.yaml
        assert self.yaml['description'] == 'DAG de teste'
        
    def test_yaml_has_feature_settings(self):
        assert 'feature_engineering' in self.yaml
        assert 'keyboard_smash' in self.yaml['feature_engineering']
    

def test_try_get_fail():
    yamlParser = YAMLParser
    with pytest.raises(ValueError) as exc:
        yamlParser('src/parser/initial/tests/mock/ymal_mock_fail.yaml').parse()
        
    assert "Erro no arquivo ymal_mock_fail.yaml: O campo `description` é obrigatório." in str(exc.value)
    assert exc.type == ValueError