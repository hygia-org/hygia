from pandas import DataFrame

class FeatureEngineering():
    
    def __init__(self, csv):
        self.csv = csv

    def parser(self, feature: dict):
        if(not feature): return

        self.keyboardSmashParser(feature.get('keyboard_smash', None))

    def keyboardSmashParser(self, keyboard_smash: dict):
        if(not keyboard_smash): return
        
        columns = keyboard_smash.get('columns', None)
        for column in columns:
            print(self.getConcatenatedColumn(column))
        
    def getConcatenatedColumn(self, column):
        if(type(column) == str):
            return DataFrame(self.csv[column])
        
        value_name = ''
        for value in column:
            if (value_name != ''): 
                self.csv[value_name + value] = self.csv[value_name].astype(str) + ' ' + self.csv[value].astype(str)
                if (value_name != last_value): del self.csv[value_name]
                
            last_value = value
            value_name = value_name + value        
            
        return DataFrame(self.csv[value_name])