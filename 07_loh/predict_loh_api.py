from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model
model = joblib.load('loh_model.pkl')

# Define feature columns
feature_columns = ['age', 'blood_pressure', 'cholesterol_level', 'weight', 'height']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    X_predict = df[feature_columns]
    predictions = model.predict_proba(X_predict)[:, 1]
    return jsonify({'LOH Probability': predictions[0]})

if __name__ == '__main__':
    app.run(debug=True)
