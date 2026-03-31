from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
import joblib
import os


def train_model(X, y, model_path="outputs/models/trained_model.pkl"):
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = MultiOutputClassifier(
        RandomForestClassifier(
            n_estimators=20,
            max_depth=10,
            n_jobs=-1
        )
    )

    model.fit(X_train, y_train)

    # Ensure folder exists
    os.makedirs("outputs/models", exist_ok=True)

    # ✅ Save model
    joblib.dump(model, model_path)

    # ✅ Save feature columns 
    joblib.dump(X.columns.tolist(), "outputs/models/feature_columns.pkl")

    print("✅ Model and feature columns saved")

    return model, X_test, y_test