import os
import pandas as pd

from parser.YAML_parser import YAMLParser

from parser.pre_processing_parser import PreProcessingParser
from data_pipeline.pre_processing.concatenate_columns import concatenate_columns

from parser.feature_engineering_parser import FeatureEngineeringParser
from data_pipeline.feature_engineering.feature_engineering import FeatureEngineering

from parser.model_parser import ModelParser
from data_pipeline.model.random_forest import RandomForestModel

if __name__ != "__main__":
    exit()   
    
def get_config(yaml_path: str):
    initialParser = YAMLParser
    
    preProcessingParser = PreProcessingParser
    
    featureEngineringParser = FeatureEngineeringParser
    featureEngineering = FeatureEngineering
    
    modelParser = ModelParser
    randomForestModel = RandomForestModel

    config = initialParser(yaml_path).parse()
    
    for data in config['data_path']:
        separator = config['separator']
        engine = config['engine']
        encoding = config['encoding']
        df = pd.read_csv(data, sep=separator, engine=engine, encoding=encoding, nrows=10000)
        
        columns_name = list(df.columns)
        columns_set, columns_name = preProcessingParser(columns_name).parse(config['pre_processing'])
        df = concatenate_columns(df, columns_set)

        features_configs, columns_alias = featureEngineringParser(columns_name).parse(config['feature_engineering'])
        for feature_config in features_configs:
            feature_columns = feature_config['columns']
            
            for column in feature_columns:
                lang = feature_config['data_lang']
                dimensions = feature_config['dimensions'][column]
                df = featureEngineering(lang=lang, dimensions=dimensions).extract_features(df, column)
                
        model_configs = modelParser(columns_alias).parse(config['model'])
        for model_config in model_configs:
            model_columns = model_config['columns']
            
            for column in model_columns:
                featured_df = df.loc[:, df.columns.str.endswith(column)]
                df[f'prediction_{column}'] = randomForestModel(model_file='data/RandomForest_Ksmash_WordEmbedding.model').predict(featured_df.iloc[:,-30:])
            
        del config['pre_processing']
        del config['feature_engineering']
        del config['model']
        
        print(3*'\n')
        print(20*'-')
        print("Result")
        print(df.loc[:, df.columns.str.startswith('prediction_')])
        print(20*'-')
        print(3*'\n')
         
get_config('src/yamls/basic_example.yaml')
