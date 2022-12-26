import pytest

from parser.generator import Generator

@pytest.mark.parametrize(
    'yaml_url, dag_colmuns_title',
    [('src/parser/tests/mock/first_case', 'NUMBER'),
     ('src/parser/tests/mock/second_case', 'NUMBERADDRESS'),
     ('src/parser/tests/mock/third_case', 'NUMBERADDRESS'),
     ('src/parser/tests/mock/third_case', 'ZIPCODE')]
)
def test_generator(yaml_url, dag_colmuns_title):
        features_mock = []
        generator = Generator(yaml_url).generate_dags()

        for feature in generator: features_mock.append(dag_colmuns_title in feature)
        assert any(features_mock)