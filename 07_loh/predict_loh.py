import pandas as pd
import sys
import joblib

# Load the model
model = joblib.load('loh_model.pkl')

# Load data to predict
input_file = sys.argv[1]
data_to_predict = pd.read_csv(input_file)

# Predict
X_predict = data_to_predict[feature_columns]
X_predict_scaled = scaler.transform(X_predict)
predictions = model.predict_proba(X_predict_scaled)[:, 1]

# Save predictions
data_to_predict['LOH Probability'] = predictions
data_to_predict.to_csv('predicted.csv', index=False)
