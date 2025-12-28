from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import joblib

class QoEPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.smote = SMOTE(random_state=42)

    def train(self, X, y):
        # Balance data using SMOTE as seen in your notebook
        X_res, y_res = self.smote.fit_resample(X, y)
        self.model.fit(X_res, y_res)
        return "Model trained successfully."

    def predict(self, X):
        return self.model.predict(X)

    def save(self, filename):
        joblib.dump(self.model, filename)