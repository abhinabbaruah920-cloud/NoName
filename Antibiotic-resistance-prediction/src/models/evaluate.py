from sklearn.metrics import classification_report, hamming_loss
import numpy as np


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("\n📊 Evaluation Results:\n")

    # Convert to numpy (safety)
    y_test = np.array(y_test)
    y_pred = np.array(y_pred)

    # Hamming Loss
    loss = hamming_loss(y_test, y_pred)
    print(f"✅ Hamming Loss: {loss:.4f}")

    # Per-label accuracy
    accuracy_per_label = (y_test == y_pred).mean(axis=0)
    print("\n📈 Accuracy per antibiotic:")
    print(accuracy_per_label)

    return loss