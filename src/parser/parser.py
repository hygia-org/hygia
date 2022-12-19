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
        dag_id = self._try_get(dag, 'id')
        description = self._try_get(dag, 'description')
        verify = self._try_get(dag, 'verify')

        location = verify.get('location', None)
        cellphone_number = verify.get('cellphone_number', None)
        address = verify.get('address', None)
        area_code = verify.get('area_code', None)

        return (
            dag_id,
            description,
            location,
            cellphone_number,
            address,
            area_code
            )

    def _try_get(self, variable: dict, field, error_msg=None):
        try:
            return variable[field]
        except KeyError:
            if not error_msg:
                error_msg = f'O campo `{field}` é obrigatório.'
            file_name = self.filepath.split('/')[-1]
            error_msg = f'Erro no arquivo {file_name}: {error_msg}'
            raise ValueError(error_msg)
