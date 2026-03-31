# Team NoName

# 🧬 Antibiotic Resistance Prediction System

## Overview

Antimicrobial resistance is one of the most critical global health challenges.  
This project uses Machine Learning to predict antibiotic resistance and suggest effective treatments.

The system analyzes patient and clinical data to determine which antibiotics are likely to be ineffective (resistant) and which can be recommended.

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
