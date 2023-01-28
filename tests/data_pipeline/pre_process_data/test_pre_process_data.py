from hygia.data_pipeline.pre_process_data.pre_process_data import PreProcessData

class TestPreProcessData:
    def setup_method(self):
        self.pre_process_data = PreProcessData()
    
    def test_replace_abbreviation(self):
        assert self.pre_process_data._replace_abbreviation("NO") == "NUMBER"
        assert self.pre_process_data._replace_abbreviation("no") == "NUMBER"
        assert self.pre_process_data._replace_abbreviation("no123") == "NUMBER123"
        assert self.pre_process_data._replace_abbreviation("no 123") == "NUMBER 123"
        assert self.pre_process_data._replace_abbreviation("123 no") == "123 NUMBER"
        assert self.pre_process_data._replace_abbreviation("not") == "not"
        assert self.pre_process_data._replace_abbreviation("NOT") == "NOT"
        assert self.pre_process_data._replace_abbreviation("ono") == "ono"