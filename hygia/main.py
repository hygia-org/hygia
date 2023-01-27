import pandas as pd
from colorama import Fore, Back

from hygia import PreProcessData
from hygia import FeatureEngineering
from hygia import RandomForestModel
from hygia import AnnotateData

from hygia.parser.model_parser import ModelParser
from hygia.parser.YAML_parser import YAMLParser
from hygia.parser.pre_processing_parser import PreProcessingParser
from hygia.parser.feature_engineering_parser import FeatureEngineeringParser
from hygia.parser.annotate_data_parser import AnnotateDataParser
    
def run_with_config(yaml_path: str):
    initialParser = YAMLParser
    
    preProcessingParser = PreProcessingParser
    preProcessData = PreProcessData()
    
    featureEngineeringParser = FeatureEngineeringParser
    featureEngineering = FeatureEngineering
    
    annotateDataParser = AnnotateDataParser
    annotateData = AnnotateData
    
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
        print(f'{Fore.MAGENTA}------ HYGIA ------{Fore.WHITE}')
            
        # Pre processing        
        print(30*'-')
        print(f'{Back.WHITE }{Fore.BLACK}Running PRE PROCESSING...{Back.BLACK }{Fore.WHITE}')
        
        columns_name = list(df.columns)
        
        columns_set, columns_name = preProcessingParser(columns_name).parse(config['pre_processing'])
        for columns in columns_set:       
            for key, value in columns.items():
                df = preProcessData.pre_process_data(df, value, key)
        
        # Feature engineering
        print(30*'-')
        print(f'{Back.WHITE }{Fore.BLACK}Running FEATURE ENGINEERING...{Back.BLACK }{Fore.WHITE}')
        
        features_configs, columns_alias = featureEngineeringParser(columns_name).parse(config['feature_engineering'])
        
        for feature_config in features_configs:
            feature_columns = feature_config['columns']
            lang = feature_config['data_lang']
            
            for column in feature_columns:
                dimensions = feature_config['dimensions'][column]
                df = preProcessData.handle_nulls(df, column)
                df = featureEngineering(lang=lang, dimensions=dimensions).extract_features(df, column)
        
        # Annotate Data
        print(30*'-')
        print(f'{Back.WHITE }{Fore.BLACK}Running ANNOTATE DATA...{Back.BLACK }{Fore.WHITE}')

        annotate_data_configs = annotateDataParser().parse(config['annotate_data'])
        
        for annotate_data_config in annotate_data_configs:
            columns = annotate_data_config['columns']
            for column in columns:       
                thresholds = annotate_data_config['thresholds']
                df = annotateData().annotate_data(df, column, thresholds)  
            
        # Model
        print(30*'-')
        print(f'{Back.WHITE }{Fore.BLACK}Running MODEL (KEYBOARD-SMASH)...{Back.BLACK }{Fore.WHITE}')
        
        model_configs = modelParser(columns_alias).parse(config['model'])
        for model_config in model_configs:
            model_columns = model_config['columns']
            trained_model_file = model_config['trained_model_file']
            
            for column in model_columns:
                features_columns = [col for col in df if (col.startswith('feature_ks') or col.startswith('feature_we') or col.startswith('feature_re')) and col.endswith(column)]
                
                randomForest = randomForestModel(trained_model_file)
                # randomForest.train_and_get_scores(df, column, features_columns)
                
                results[column] = df[column]
                results[f'prediction_{column}'] = randomForest.predict(df[features_columns].values)
                
                if(config['output_folder']):
                    output_folder = config['output_folder']
                    results[results[f'prediction_{column}'] == 1] \
                        .loc[:, results.columns.str.endswith(column)] \
                        .to_csv(f'{output_folder}prediction_{column}.csv')
                    print(30*'-')
                    print(f'{Fore.GREEN}exporting to {output_folder}prediction_{column}.csv{Fore.WHITE}')
        
        del config['pre_processing']
        del config['feature_engineering']
        del config['annotate_data']
        del config['model']
        
        return results