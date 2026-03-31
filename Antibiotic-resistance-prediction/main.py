from src.data.preprocess import load_data, preprocess_all
from src.data.merge_datasets import merge_datasets
from src.features.build_features import build_feature_matrix
from src.models.train import train_model
from src.models.evaluate import evaluate_model
from src.utils.helpers import create_directories

create_directories()

card, amr, susc = load_data(
    "data/processed/card_data.csv",   
    "data/raw/amr_data.xlsx",
    "data/raw/susceptibility_data.csv"
)

card, amr, susc = preprocess_all(card, amr, susc)

df = merge_datasets(card, amr, susc)




X, y = build_feature_matrix(df)

model, X_test, y_test = train_model(X, y)

evaluate_model(model, X_test, y_test)

