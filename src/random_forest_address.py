
import pandas as pd

from data_pipeline.model.random_forest import RandomForestModel
from data_pipeline.feature_engineering.key_smash import KeySmash
from data_pipeline.feature_engineering.word_embedding import WordEmbedding

class RandomForestAddress():
    
    def __init__(self, data_paths, model_configs, features_configs):
        self.data_paths = data_paths
        self.model_configs = model_configs
        self.features_configs = features_configs
    
    def __normalize_column(self, df, column):
        return df[column]  / df[column].abs().max() if df[column].abs().max() != 0.0 else 0.0
    
    def run(self):
        df = pd.read_csv('data/data_example.csv')
        key_smash = KeySmash()
        word_embedding = WordEmbedding(lang="es", dimensions=25)

        # Columns concatenation = output: alias_concat
        df = df[['ADDRESS']]
        df['alias_concat'] = df['ADDRESS']

        # Key Smash new columns for each key smash calculation
        df['irregular_sequence_vowels'] = df['alias_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'vowels'))
        df['irregular_sequence_consonants'] = df['alias_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'consonants'))
        df['irregular_sequence_special_characters'] = df['alias_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'special_characters'))
        df['number_count_metric'] = df['alias_concat'].fillna('').apply(lambda x: key_smash.calculate_number_count_metric(x))
        df['char_frequency_metric'] = df['alias_concat'].fillna('').apply(lambda x: key_smash.calculate_char_frequency_metric(x))

        # Value Normalizations for keysmash columns
        key_smash_columns = ['irregular_sequence_vowels',
                        'irregular_sequence_consonants',
                        'irregular_sequence_special_characters',
                        'number_count_metric',
                        'char_frequency_metric']
        for column in key_smash_columns:
            df[column] = self.__normalize_column(df, column)
            
        # Adding a column in df for each dimension in the word embedding vetor
        DIMESIONS = 25
        for i in range(DIMESIONS):
            df[i] = df['alias_concat'].fillna('').apply(lambda x: word_embedding.get_embedding(x)[i])

        # Cleaning other columns and running models over only key_smash and word embedding columns
        df = df.drop(['alias_concat', 'ADDRESS'], axis=1)
        rf_model = RandomForestModel(model_file='data/RandomForest_Ksmash_WordEmbedding.model')
        y_pred = rf_model.predict(df)

        # Saving prediction to the output file
        df_pred = pd.DataFrame({'prediction': y_pred})
        df_pred.to_csv('predictions.csv', index=False)



