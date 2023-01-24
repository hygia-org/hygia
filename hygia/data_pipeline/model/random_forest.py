import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
import pandas as pd

class RandomForestModel:
  def __init__(self, model_file=None, n_estimators=100, max_depth=None, random_state=0):
    self.model = None
    if model_file is not None:
      with open(model_file, 'rb') as f:
        self.model = pickle.load(f)
    if self.model is None:
      self.n_estimators = n_estimators
      self.max_depth = max_depth
      self.random_state = random_state
      self.model = RandomForestClassifier(n_estimators=self.n_estimators, max_depth=self.max_depth, random_state=self.random_state)
  
  def train_and_get_scores(self, df, concatened_column_name, all_features_columns, test_size=0.3):
    df_not_duplicates = df.drop_duplicates(subset=[concatened_column_name])
    
    KEY_SMASH_COUNT = df_not_duplicates['target'].value_counts()['key_smash']
    df_valid = df_not_duplicates[df_not_duplicates['target'] == 'valid'].sample(n=KEY_SMASH_COUNT, random_state=42)
    df_invalid = df_not_duplicates[df_not_duplicates['target'] != 'valid']
    df_balanced = pd.concat([df_valid, df_invalid])

    df_balanced['is_key_smash'] = df_balanced['target'] == 'key_smash'

    X = df_balanced[[*all_features_columns]]
    y = df_balanced['is_key_smash']

    clf=self.model
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    
    clf.fit(X_train,y_train)
    
    y_pred = clf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    scores = {
      'accuracy': accuracy,
      'precision': precision,
      'recall': recall,
      'f1': f1,
    }
    
    return clf, scores 
  
  def predict(self, X):
    return self.model.predict(X)

