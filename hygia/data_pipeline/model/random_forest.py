import pickle
import pandas as pd
from colorama import Fore, Style

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score

class RandomForestModel:
  """
    This class presents the model Random Forest, allowing train and predict the model

    Examples - 
    Use this class like this:

    \code{.py}
        new_rf_model = hg.RandomForestModel()
        clf, scores = new_rf_model.train_and_get_scores(df, concatened_column_name, all_features_columns)
        scores
    \endcode
    """
  def __init__(self, model_file=None,
               normalization_absolutes_file=None,
               n_estimators=100, max_depth=None,
               random_state=0,
               normalize=True) -> None:
    """
    Initialize the RandomForestModel class.

    \param model_file (Type: path) Path to the model file
    """
    self.normalize = normalize
    self.model = None
    self.normalization_absolutes = None
    self.pre_trained = False
    if normalization_absolutes_file:
      self.normalization_absolutes = pd.read_csv(normalization_absolutes_file)
    if model_file:
      self.pre_trained = True
      with open(model_file, 'rb') as f:
        self.model = pickle.load(f)
    if self.model is None:
      self.n_estimators = n_estimators
      self.max_depth = max_depth
      self.random_state = random_state
      self.model = RandomForestClassifier(n_estimators=self.n_estimators, max_depth=self.max_depth, random_state=self.random_state)
  
  def __get_absolute_maximums(self, df, features_columns_to_normalize, concatened_column_name):
    if self.normalization_absolutes:
      return
    absolutes_dict = {}
    for column in features_columns_to_normalize:
      absolute_maximum = df[column].max()
      absolutes_dict[column.replace(f"_{concatened_column_name}", '')] = [absolute_maximum] if absolute_maximum else [1.0]
    self.normalization_absolutes = pd.DataFrame(absolutes_dict)
      
  def __normalization(self, df, features_columns_to_normalize, concatened_column_name):
    if not self.normalize:
      return df
    for features_column_to_normalize in features_columns_to_normalize:
      column_absolute_maximum = self.normalization_absolutes[features_column_to_normalize.replace(f"_{concatened_column_name}", '')].values[0]
      df[features_column_to_normalize] = df[features_column_to_normalize] / column_absolute_maximum
    return df
  
  def train_and_get_scores(self, df, concatened_column_name, all_features_columns, test_size=0.3):
    """
    Train and get scores for the model execution.

    \param df (DataFrame) Dataframe with the data.
    \param concatened_column_name (Type: str) Column name
    \param all_features_columns (Type: List) List of all features column nales
    """    
    print(f'{Fore.YELLOW}tranning model...{Fore.WHITE}')
    
    # Droping Duplicates
    df_not_duplicates = df.drop_duplicates(subset=[concatened_column_name])
    
    # Balancing
    KEY_SMASH_COUNT = df_not_duplicates['target'].value_counts()['key_smash']
    df_valid = df_not_duplicates[df_not_duplicates['target'] == 'valid'].sample(n=KEY_SMASH_COUNT, random_state=42)
    df_invalid = df_not_duplicates[df_not_duplicates['target'] != 'valid']
    df_balanced = pd.concat([df_valid, df_invalid])
    df_balanced['is_key_smash'] = df_balanced['target'] == 'key_smash'
    
    # Normalization
    key_smash_features_columns = [column for column in all_features_columns if column.startswith('feature_ks')]
    self.__get_absolute_maximums(df_balanced, key_smash_features_columns, concatened_column_name)
    df_balanced_normalized = self.__normalization(df_balanced.copy(), key_smash_features_columns, concatened_column_name)
    
    # Train/Test split
    X = df_balanced_normalized[[*all_features_columns]].values
    y = df_balanced_normalized['is_key_smash']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    
    # Train
    clf=self.model
    clf.fit(X_train,y_train)
    
    # Test
    y_pred = clf.predict(X_test)
    print(f'{Fore.GREEN}done{Fore.WHITE}')
    print(f'{Fore.YELLOW}get model score...{Fore.WHITE}')
    
    # Scoring
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f'{Style.BRIGHT}accuracy -> {Style.NORMAL}{accuracy}')
    print(f'{Style.BRIGHT}precision -> {Style.NORMAL}{precision}')
    print(f'{Style.BRIGHT}recall -> {Style.NORMAL}{recall}')
    print(f'{Style.BRIGHT}f1 -> {Style.NORMAL}{f1}')
    
    scores = {
      'accuracy': accuracy,
      'precision': precision,
      'recall': recall,
      'f1': f1,
    }
    
    return scores
  def predict(self, X, concatened_column_name):
    print(f'{Fore.YELLOW}running model...{Fore.WHITE}')
    
    key_smash_features_columns = [column for column in X.columns if column.startswith('feature_ks')]
    X = self.__normalization(X.copy(), key_smash_features_columns, concatened_column_name)
    
    return self.model.predict(X.values)
  
  def export_model(self, export_path:str, normalization_absolutes_file_path:str) -> None:
    print(f'{Fore.YELLOW}exporting model and normalization absolutes...{Fore.WHITE}')
    pickle.dump(self.model, open(export_path, 'wb'))
    self.normalization_absolutes.to_csv(normalization_absolutes_file_path, index=False)

