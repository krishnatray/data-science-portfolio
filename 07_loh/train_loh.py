import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import xgboost as xgb
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import joblib

# Load synthetic data
df = pd.read_csv('synthetic_data.csv')

# Splitting data into train, test, and validation sets
X = df[feature_columns]
y = df['hospitalization']
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Standardizing features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Train models
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "XGBoost": xgb.XGBClassifier(),
    "Deep Learning": Sequential([
                        Dense(64, activation='relu', input_shape=(len(feature_columns),)),
                        Dense(64, activation='relu'),
                        Dense(1, activation='sigmoid')
                    ])
}

best_model = None
best_precision = 0

for name, model in models.items():
    if name == "Deep Learning":
        # Deep Learning Model
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, verbose=0)
        y_pred = (model.predict(X_val_scaled) > 0.5).astype("int32")
    else:
        # Other models
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_val_scaled)

    accuracy = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred)
    recall = recall_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred)

    print(f"Model: {name}")
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")
    print()

    if precision > best_precision:
        best_precision = precision
        best_model = model

# Save the best model
joblib.dump(best_model, 'loh_model.pkl')
print(f"Best Model: {type(best_model).__name__} with Precision: {best_precision}")
