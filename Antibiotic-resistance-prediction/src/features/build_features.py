import pandas as pd


def build_feature_matrix(df):
    print("\n🔍 Available columns:\n", list(df.columns))

    # Columns to exclude (non-useful)
    exclude_cols = [
        'ID', 'Name', 'Email', 'Address', 'age/gender',
        'Collection_Date', 'Notes'
    ]

    # Target columns = antibiotics
    target_columns = [col for col in df.columns if col not in exclude_cols]

    print(f"✅ Using {len(target_columns)} antibiotic columns as targets")

    # Convert target values to binary (R=1, others=0)
    mapping = {
        "S": 0, "Susceptible": 0,
        "R": 1, "Resistant": 1,
        "I": 0, "Intermediate": 0
    }

    df[target_columns] = df[target_columns].astype(str)

    for col in target_columns:
        df[col] = df[col].map(mapping).fillna(0)

    # 🎯 Targets
    y = df[target_columns]

    # 🎯 Features (THIS WAS MISSING ❗)
    X = df.drop(columns=target_columns)

    # Convert categorical → numeric
    X = pd.get_dummies(X, drop_first=True)

    # Ensure numeric
    X = X.apply(pd.to_numeric, errors='coerce')

    # Fill NaN
    X = X.fillna(0)

    # Reduce features
    X = X.loc[:, X.sum() > 20]

    # Limit size
    if X.shape[1] > 1000:
        X = X.iloc[:, :1000]

    print("✅ X shape:", X.shape)
    print("✅ y shape:", y.shape)

    return X, y