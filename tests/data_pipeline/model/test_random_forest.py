import pandas as pd
from sklearn.datasets import make_classification
from hygia import RandomForestModel

class TestRandomForestModel:
    def test_random_forest_model(self):
        X, y = make_classification(random_state=42)

        columns = ['feature_'+str(i) for i in range(X.shape[1])]
        df = pd.DataFrame(X, columns=columns)
        df['target'] = ['valid' if label == 0 else 'key_smash' for label in y]

        model = RandomForestModel(normalize=False)

        scores = model.train_and_get_scores(df, 'target', columns)

        assert scores['accuracy'] >= 0.0 and scores['accuracy'] <= 1
        assert scores['precision'] >= 0.0 and scores['precision'] <= 1
        assert scores['recall'] >= 0.0 and scores['recall'] <= 1
        assert scores['f1'] >= 0.0 and scores['f1'] <= 1
