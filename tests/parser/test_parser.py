import pytest

from src.parser.parser import Parser

class TestParser():
    
    def setup_method(self):
        self.object_mock = {'data': 23}
        self.parser = Parser

    def test_try_get_fail(self):
        with pytest.raises(ValueError) as exc:
            self.parser('tests/mock/success/ymal_mock.yaml')._try_get(self.object_mock, 'feature')
            
        assert "Error in file ymal_mock.yaml: the field `feature` is required." in str(exc.value)
        assert exc.type == ValueError
        
    def test_get_fallback(self):
        response = self.parser('tests/mock/success/ymal_mock.yaml')._get(self.object_mock, 'feature', 20)
        
        assert response == 20
        
    def test_get_good_flow(self):
        response = self.parser('tests/mock/success/ymal_mock.yaml')._get(self.object_mock, 'data', 20)
        
        assert response == 23