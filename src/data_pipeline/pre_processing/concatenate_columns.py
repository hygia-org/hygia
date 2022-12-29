from pandas import DataFrame

def get_concatenated_column(csv, columns):
    if(type(columns) == str):
        return DataFrame(csv[columns])
    
    value_name = ''
    for value in columns:
        if (value_name != ''): 
            csv[value_name + value] = csv[value_name].astype(str) + ' ' + csv[value].astype(str)
            if (value_name != last_value): del csv[value_name]
            
        last_value = value
        value_name = value_name + value        
        
    return DataFrame(csv[value_name])