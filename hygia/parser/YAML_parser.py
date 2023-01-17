import yaml

from hygia.parser.parser_base import ParserBase

class YAMLParser(ParserBase):

    def parse(self):
        return self._parse_yaml()

    def _parse_yaml(self):
        with open(self.filepath, 'r') as file:
            dag_config_dict = yaml.safe_load(file)

        dag = self._try_get(dag_config_dict, 'dag')
        data_config = self._try_get(dag, 'data_config')
        
        separator = self._get(data_config, 'separator', '¨')
        engine = self._get(data_config, 'engine', 'python')
        encoding = self._get(data_config, 'encoding', 'utf-8')
        nrows = self._get(data_config, 'nrows', 10000)

        initial_parser = {
            "nrows": nrows,
            "engine": engine,
            "encoding": encoding,
            "separator": separator,
            "dag_id": self._try_get(dag, 'id'),
            "model": self._try_get(dag, 'model'),
            "data_path": self._try_get(dag, 'data_path'),
            "description": self._try_get(dag, 'description'),
            "output_folder": self._try_get(dag, 'output_folder'),
            "pre_processing": self._try_get(dag, 'pre_processing'),
            "feature_engineering": self._try_get(dag, 'feature_engineering'),
        }

        return initial_parser
