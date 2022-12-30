import pytest

from parser.generator import Generator

def test_generator():  
        generator = Generator('src/tests/mock/success').generate_dags()
        default_case = generator[0]
        
        assert 'dataframe' in default_case
        assert 'enabled_features' in default_case
        
        assert 'data_lang' in default_case
        assert default_case['data_lang'] == 'es'

        assert 'dimensions' in default_case
        assert type(default_case['dimensions']) == dict
        
def test_generator_off_case():
        generator = Generator('src/tests/mock/success').generate_dags()
        off_case = generator[1]
        
        assert 'dataframe' in off_case
        assert 'enabled_features' in off_case
        
        assert 'data_lang' in off_case
        assert off_case['data_lang'] == 'es'

        assert 'dimensions' in off_case
        assert off_case['dimensions'] == None
        
@pytest.mark.parametrize(
    'yaml_url, dag_colmuns_title',
    [('src/tests/mock/fail', 'Label tudo_jnto not match')]
)
def test_generator_fail(yaml_url, dag_colmuns_title):
    with pytest.raises(ValueError) as exc:
        Generator(yaml_url).generate_dags()
        
    assert dag_colmuns_title in str(exc.value)
    assert exc.type == ValueError
