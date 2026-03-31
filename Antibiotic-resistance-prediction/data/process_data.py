import pandas as pd
import os


def load_all_card_files(folder_path):
    dfs = []

    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            path = os.path.join(folder_path, file)
            try:
                df = pd.read_csv(path)
                df["source_file"] = file  # track origin
                dfs.append(df)
            except Exception as e:
                print(f"Error reading {file}: {e}")

    return dfs


def filter_columns(df):
    # Keep only useful columns
    useful_keywords = ["gene", "drug", "resistance", "antibiotic"]

    useful_cols = [
        col for col in df.columns
        if any(keyword in col.lower() for keyword in useful_keywords)
    ]

    # If nothing matched, keep original (failsafe)
    if not useful_cols:
        return df

    return df[useful_cols]


def merge_card_data(dfs):
    filtered_dfs = []

    for df in dfs:
        filtered_df = filter_columns(df)
        filtered_dfs.append(filtered_df)

    combined = pd.concat(filtered_dfs, ignore_index=True)

    return combined


def save_card_data(df, output_path="data/processed/card_data.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ CARD merged dataset saved at {output_path}")


if __name__ == "__main__":
    folder = "data/raw/card/"  # 👈 put all CARD CSVs here

    dfs = load_all_card_files(folder)
    combined = merge_card_data(dfs)
    save_card_data(combined)