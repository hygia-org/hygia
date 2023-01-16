import pickle
from sklearn.ensemble import RandomForestClassifier

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
  
  def predict(self, X):
    return self.model.predict(X)

