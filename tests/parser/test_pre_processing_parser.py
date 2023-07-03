import pytest
from hygia.parser.pre_processing_parser import PreProcessingParser

class TestPreProcessingParser:
    
    def setup_method(self):
        self.columns_name = ['col1', 'col2']
        self.parser = PreProcessingParser(self.columns_name)
        
    def test_parse_pre_processing_configs_with_empty_data(self):
        data = []
        result = self.parser.parse(data)
        
        assert result is None
        
    def test_get_dataframe(self):
        aliases = [{'col3': 'new_col3'}, {'col4': 'new_col4'}]
        self.parser._get_dataframe(aliases)
        
        assert 'col3' in self.parser.columns_name
        assert 'col4' in self.parser.columns_name
        
    def test_get_dataframe_with_empty_aliases(self):
        aliases = []
        self.parser._get_dataframe(aliases)
        
        assert self.parser.columns_name == self.columns_name
        
    def test_get_dataframe_with_existing_columns(self):
        aliases = [{'new_col1': 'col1'}, {'new_col2': 'col2'}]
        self.parser._get_dataframe(aliases)
        
        assert self.parser.columns_name == self.columns_name
        
    def test_get_dataframe_with_empty_aliases_and_existing_columns(self):
        aliases = []
        self.parser._get_dataframe(aliases)
        
        assert self.parser.columns_name == self.columns_name
