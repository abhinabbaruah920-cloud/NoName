import os
import joblib
import matplotlib.pyplot as plt


def ensure_dirs():
    dirs = [
        "outputs/models",
        "outputs/plots",
        "outputs/reports"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)


def save_model(model, path="outputs/models/trained_model.pkl"):
    ensure_dirs()
    joblib.dump(model, path)
    print(f"Model saved at {path}")


def save_plot(fig, path):
    ensure_dirs()
    fig.savefig(path)
    print(f"Plot saved at {path}")


def save_report(text, path="outputs/reports/report.txt"):
    ensure_dirs()
    with open(path, "w") as f:
        f.write(text)
    print(f"Report saved at {path}")