import pandas as pd

def load_data(card_path, amr_path, susc_path):
    # CARD (cleaner file)
    card = pd.read_csv(card_path, low_memory=False, encoding="latin1")

    # AMR (messy file → python engine)
    amr = pd.read_csv(
        amr_path,
        encoding="latin1",
        sep=None,
        engine="python",
        on_bad_lines="skip"
    )

    # Susceptibility (same)
    susc = pd.read_csv(
        susc_path,
        encoding="latin1",
        sep=None,
        engine="python",
        on_bad_lines="skip"
    )

    return card, amr, susc


def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def preprocess_all(card, amr, susc):
    return clean_data(card), clean_data(amr), clean_data(susc)