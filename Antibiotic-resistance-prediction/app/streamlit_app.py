import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Antibiotic Predictor", layout="wide")

# -------------------------------
# CUSTOM STYLING (SOFT UI)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #f7f9fc;
}
.main {
    background-color: #f7f9fc;
}
h1 {
    color: #2c3e50;
}
.stButton>button {
    background-color: #6c8cff;
    color: white;
    border-radius: 8px;
    padding: 10px;
}
.stButton>button:hover {
    background-color: #5a78e0;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("🧬 Antibiotic Resistance Predictor")
st.write("Predict resistance and suggest effective antibiotics.")

# -------------------------------
# LOAD MODEL + FEATURES
# -------------------------------
MODEL_PATH = "outputs/models/trained_model.pkl"
FEATURE_PATH = "outputs/models/feature_columns.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_resource
def load_features():
    return joblib.load(FEATURE_PATH)

if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURE_PATH):
    st.error("❌ Model or feature file missing. Run training first.")
    st.stop()

model = load_model()
feature_columns = load_features()

# -------------------------------
# INPUT SECTION
# -------------------------------
st.sidebar.header("🧾 Patient Details")

diabetes = st.sidebar.selectbox("Diabetes", ["No", "Yes"])
hypertension = st.sidebar.selectbox("Hypertension", ["No", "Yes"])
hospital = st.sidebar.selectbox("Hospitalized Before", ["No", "Yes"])
infection_freq = st.sidebar.slider("Infection Frequency", 0, 10, 2)

# -------------------------------
# CREATE INPUT DATA
# -------------------------------
input_data = pd.DataFrame({
    "Diabetes": [diabetes],
    "Hypertension": [hypertension],
    "Hospital_before": [hospital],
    "Infection_Freq": [infection_freq]
})

# Encode input
input_encoded = pd.get_dummies(input_data)

# Align with training features
def align_features(input_df):
    # Step 1: create full zero dataframe
    aligned_df = pd.DataFrame(0, index=[0], columns=feature_columns)

    # Step 2: copy matching columns from input
    for col in input_df.columns:
        if col in aligned_df.columns:
            aligned_df[col] = input_df[col].values[0]

    return aligned_df

input_encoded = align_features(input_encoded)

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🔍 Predict"):

    prediction = model.predict(input_encoded)[0]

    antibiotics = [
        'AMX/AMP', 'AMC', 'CZ', 'FOX', 'CTX/CRO', 'IPM',
        'GEN', 'AN', 'Acide nalidixique', 'ofx',
        'CIP', 'C', 'Co-trimoxazole', 'Furanes', 'colistine'
    ]

    resistant = []
    recommended = []

    for i, ab in enumerate(antibiotics[:len(prediction)]):
        if prediction[i] == 1:
            resistant.append(ab)
        else:
            recommended.append(ab)

    st.markdown("---")
    st.subheader("📊 Results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ❌ Resistant")
        if resistant:
            for r in resistant:
                st.write(f"• {r}")
        else:
            st.write("None")

    with col2:
        st.markdown("### ✅ Recommended")
        if recommended:
            for r in recommended:
                st.write(f"• {r}")
        else:
            st.write("None")

    # -------------------------------
    # INSIGHT BOX
    # -------------------------------
    st.markdown("---")
    st.info(
        "This prediction helps identify effective antibiotics and avoid resistance. "
        "Useful for decision support in clinical scenarios."
    )