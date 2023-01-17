import os
import pandas as pd

from hygia import PreProcessData
from hygia import FeatureEngineering
from hygia import RandomForestModel

from hygia.parser.model_parser import ModelParser
from hygia.parser.YAML_parser import YAMLParser
from hygia.parser.pre_processing_parser import PreProcessingParser
from hygia.parser.feature_engineering_parser import FeatureEngineeringParser
    
def run_with_config(yaml_path: str):
    initialParser = YAMLParser
    
    preProcessingParser = PreProcessingParser
    preProcessData = PreProcessData
    
    featureEngineeringParser = FeatureEngineeringParser
    featureEngineering = FeatureEngineering
    
    modelParser = ModelParser
    randomForestModel = RandomForestModel

    config = initialParser(yaml_path).parse()
    
    for data in config['data_path']:
        # Load csv
        separator = config['separator']
        encoding = config['encoding']
        engine = config['engine']
        nrows = config['nrows']
        df = pd.read_csv(data, sep=separator, engine=engine, encoding=encoding, nrows=nrows)
        
        results = pd.DataFrame()
            
        # Pre processing
        columns_name = list(df.columns)
        
        columns_set, columns_name = preProcessingParser(columns_name).parse(config['pre_processing'])
        for columns in columns_set:       
            for key, value in columns.items():
                df = preProcessData().pre_process_data(df, value, key)
        
        # Feature engineering
        features_configs, columns_alias = featureEngineeringParser(columns_name).parse(config['feature_engineering'])
        for feature_config in features_configs:
            feature_columns = feature_config['columns']
            
            for column in feature_columns:
                lang = feature_config['data_lang']
                dimensions = feature_config['dimensions'][column]
                df = featureEngineering(lang=lang, dimensions=dimensions).extract_features(df, column)
                
        # Model
        model_configs = modelParser(columns_alias).parse(config['model'])
        for model_config in model_configs:
            model_columns = model_config['columns']
            trained_model_file = model_config['trained_model_file']
            
            for column in model_columns:
                results[column] = df[column]
                featured_df = df.loc[:, df.columns.str.endswith(column)]
                results[f'prediction_{column}'] = randomForestModel(model_file=trained_model_file).predict(featured_df.iloc[:,-30:])
            
        del config['pre_processing']
        del config['feature_engineering']
        del config['model']
        
        return results