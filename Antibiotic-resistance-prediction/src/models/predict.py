import joblib


def load_model(model_path="outputs/models/trained_model.pkl"):
    return joblib.load(model_path)


def predict(model, X):
    return model.predict(X)


def predict_proba(model, X):
    return model.predict_proba(X)