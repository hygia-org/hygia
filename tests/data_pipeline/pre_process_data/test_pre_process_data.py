import pytest
import pandas as pd
from hygia.data_pipeline.pre_process_data.pre_process_data import PreProcessData

class TestPreProcessData:
    def setup_method(self):
        self.pre_processor = PreProcessData(country='MEXICO')

    def test_concatenate_columns(self):
        data = {'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']}
        df = pd.DataFrame(data)
        expected_output = ['a d', 'b e', 'c f']
        output = self.pre_processor.concatenate_columns(df, ['A', 'B'], 'C')
        assert list(output['C']) == expected_output

    def test_handle_nulls(self):
        data = {'A': ['a', 'b', None]}
        df = pd.DataFrame(data)
        expected_output = ['a', 'b', '']
        output = self.pre_processor.handle_nulls(df, 'A')
        assert list(output['A']) == expected_output

    def test_handle_extra_spaces(self):
        data = {'A': ['  a  ', ' b  ', ' c']}
        df = pd.DataFrame(data)
        expected_output = ['a', 'b', 'c']
        output = self.pre_processor.handle_extra_spaces(df, 'A')
        assert list(output['A']) == expected_output

    def test_handle_abreviations(self):
        data = {'A': ['CDMX', 'MZ', 'BCN']}
        df = pd.DataFrame(data)
        expected_output = ['Ciudad de México', 'MANZANA', 'Baja California']
        output = self.pre_processor.handle_abreviations(df, 'A')
        assert list(output['A']) == expected_output

    def test_pre_process_data(self):
        data = {'A': ['  a  ', ' b  ', ' c'], 'B': ['d', 'e', 'f'], 'C': ['NLE', 'CANCUN', 'NLE Monterrey']}
        df = pd.DataFrame(data)
        expected_output = ['a d', 'b e', 'c f']
        output = self.pre_processor.pre_process_data(df, ['A', 'B'], 'D')
        assert 'D' in output.columns
        assert list(output['D']) == expected_output
