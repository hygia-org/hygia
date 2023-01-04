
import pandas as pd

from data_pipeline.model.random_forest import RandomForestModel
from data_pipeline.feature_engineering.key_smash import KeySmash
from data_pipeline.feature_engineering.word_embedding import WordEmbedding

df = pd.read_csv('../data/data_example.csv')
key_smash = KeySmash()
word_embedding = WordEmbedding()

df = df[['ADDRESS']]
df['street_address_concat'] = df['ADDRESS']
df['street_address_sequence_vowels_concat'] = df['street_address_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'vowels'))
df['street_address_sequence_consonants_concat'] = df['street_address_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'consonants'))
df['street_address_sequence_special_characters_concat'] = df['street_address_concat'].fillna('').apply(lambda x: key_smash.calculate_irregular_sequence_metric(x, 'special_characters'))
df['ksmash_number_address_concat'] = df['street_address_concat'].fillna('').apply(lambda x: key_smash.calculate_number_count_metric(x))
df['char_counter_street_address_concat'] = df['street_address_concat'].fillna('').apply(lambda x: key_smash.calculate_char_frequency_metric(x))

columns = df.drop(['street_address_concat', 'ADDRESS'], axis=1).columns
columns
for column in columns:
    df[column] = df[column]  / df[column].abs().max() if df[column].abs().max() != 0.0 else 0.0
VECTOR_SIZE = 25
for i in range(VECTOR_SIZE):
    df[i] = df['street_address_concat'].fillna('').apply(lambda x: word_embedding.get_embedding(x)[i])

df = df.drop(['street_address_concat', 'ADDRESS'], axis=1)
rf_model = RandomForestModel(model_file='../data/RandomForest_Ksmash_WordEmbedding.model')
y_pred = rf_model.predict(df)
df_pred = pd.DataFrame({'prediction': y_pred})
df_pred.to_csv('predictions.csv', index=False)



