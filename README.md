# Team NoName
# 🧬 Antibiotic Resistance Prediction System

## Overview
Antimicrobial resistance is one of the most critical global health challenges. This project uses Machine Learning to predict antibiotic resistance and suggest effective treatments. The system analyzes patient and clinical data to determine which antibiotics are likely to be ineffective (resistant) and which can be recommended.
## Features
- Multi-label antibiotic resistance prediction
- Machine learning-based decision support
- Real-time predictions using Streamlit UI
- Automatic feature engineering and preprocessing
- Handles real-world messy datasets
## Problem Statement
Predict antibiotic resistance patterns based on patient and clinical data to support better treatment decisions.
## Model Details
- Algorithm: Random Forest (MultiOutputClassifier)
- Type: Multi-label classification
- Evaluation Metric:
  - Hamming Loss
  - Per-antibiotic accuracy

## Installation

### Create virtual environment
python -m venv venv
Activate:
venv\Scripts\activate
### 3. Install dependencies
pip install -r requirements.txt
## How to Run
### Step 1: Train model
python main.py
### Step 2: Run Streamlit app
streamlit run app/streamlit_app.py
## Demo
The system allows users to:
- Input patient details
- Predict antibiotic resistance
- Get recommended antibiotics
## Example Output
❌ Resistant:
AMX/AMP
CIP
✅ Recommended:
GEN
IPM
## 🔥 Future Improvements
- SHAP explainability
- Deep learning models
- Real-time hospital integration
- API deployment
