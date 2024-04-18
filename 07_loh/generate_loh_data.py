import numpy as np
import pandas as pd

# Generating synthetic data
np.random.seed(0)
num_samples = 1000

# Feature columns for LOH prediction
# Replace these with actual industry standard columns
feature_columns = ['age', 'blood_pressure', 'cholesterol_level', 'weight', 'height']

data = {
    'age': np.random.randint(18, 90, num_samples),
    'blood_pressure': np.random.randint(90, 180, num_samples),
    'cholesterol_level': np.random.randint(120, 300, num_samples),
    'weight': np.random.randint(50, 120, num_samples),
    'height': np.random.randint(150, 200, num_samples),
    'hospitalization': np.random.randint(2, size=num_samples)  # Binary classification: 1 for high risk, 0 for no risk
}

df = pd.DataFrame(data)
df.to_csv('synthetic_data.csv', index=False)
