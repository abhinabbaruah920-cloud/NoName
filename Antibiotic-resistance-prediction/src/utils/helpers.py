import os


def create_directories():
    dirs = [
        "outputs/models",
        "outputs/plots",
        "outputs/reports",
        "data/processed"
    ]

    for d in dirs:
        os.makedirs(d, exist_ok=True)


def save_text_report(text, path="outputs/reports/summary.txt"):
    with open(path, "w") as f:
        f.write(text)