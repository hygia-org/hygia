import yaml

class YAMLParser():

    def __init__(self, filepath: str):
        self.filepath = filepath

    def parse(self):
        return self._parse_yaml()

    def _parse_yaml(self):
        with open(self.filepath, 'r') as file:
            dag_config_dict = yaml.safe_load(file)

        dag = self._try_get(dag_config_dict, 'dag')

        initial_parser = {
            "dag_id": self._try_get(dag, 'id'),
            "data_path": self._try_get(dag, 'data_path'),
            "description": self._try_get(dag, 'description'),
            "feature_engineering": self._try_get(dag, 'feature_engineering'),
        }

        return initial_parser

    def _try_get(self, variable: dict, field, error_msg=None):
        try:
            return variable[field]
        except KeyError:
            if not error_msg:
                error_msg = f'O campo `{field}` é obrigatório.'
            file_name = self.filepath.split('/')[-1]
            error_msg = f'Erro no arquivo {file_name}: {error_msg}'
            raise ValueError(error_msg)
