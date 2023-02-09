import pandas as pd
from hygia import RandomForestModel

class TestRandomForestModel:
    def setup_method(self):
        self.random_forest = RandomForestModel()
    
    def test_random_forest(self):
        # TODO improve model tests
        assert self.random_forest