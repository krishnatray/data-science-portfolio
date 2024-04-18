import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import xgboost as xgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib
import os
st.set_option('deprecation.showPyplotGlobalUse', False)
# Generate synthetic data
def generate_data():
    np.random.seed(0)
    num_samples = st.slider("Number of Samples", min_value=100, max_value=5000, value=1000)
    feature_columns = ['age', 'blood_pressure', 'cholesterol_level', 'weight', 'height']

    data = {
        'age': np.random.randint(18, 90, num_samples),
        'blood_pressure': np.random.randint(90, 180, num_samples),
        'cholesterol_level': np.random.randint(120, 300, num_samples),
        'weight': np.random.randint(50, 120, num_samples),
        'height': np.random.randint(150, 200, num_samples),
        'hospitalization': np.random.randint(2, size=num_samples)
    }

    df = pd.DataFrame(data)
    st.write("Synthetic Data:")
    st.write(df)

    # Display univariate analysis
    st.write("Univariate Analysis:")
    st.write(df.describe())

    # Display bivariate analysis
    st.write("Bivariate Analysis:")
    sns.pairplot(df, hue='hospitalization', diag_kind='kde')
    st.pyplot()

    # Display correlation matrix
    st.write("Correlation Matrix:")
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot()

    # Display box plots
    st.write("Box Plots:")
    for col in df.columns[:-1]:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x='hospitalization', y=col, data=df)
        plt.title(f'{col} vs. Hospitalization')
        st.pyplot()

    df.to_csv('synthetic_data.csv', index=False)
    st.success("Synthetic data saved successfully.")

# Train models
def train_models():
    if not os.path.exists('synthetic_data.csv'):
        st.error("Please generate synthetic data first.")
        return

    df = pd.read_csv('synthetic_data.csv')
    feature_columns = ['age', 'blood_pressure', 'cholesterol_level', 'weight', 'height']

    X = df[feature_columns]
    y = df['hospitalization']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(n_estimators=100),
        "K-Nearest Neighbors": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(),
        "Support Vector Machine": SVC(probability=True),
        "XGBoost": xgb.XGBClassifier()
    }

    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        st.write(f"Model: {name}")
        st.write(f"Accuracy: {accuracy}")
        st.write(f"Precision: {precision}")
        st.write(f"Recall: {recall}")
        st.write(f"F1 Score: {f1}")

        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        st.write(f"Confusion Matrix: \n{cm}")

        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, cmap='coolwarm', fmt="d")
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title(f'Confusion Matrix for {name}')
        st.pyplot()

        st.write()

        joblib.dump(model, f'{name.lower().replace(" ", "_")}_model.pkl')
    
    st.success("Models trained successfully.")

# Predict using selected model
def predict():
    if not os.path.exists('synthetic_data.csv'):
        st.error("Please generate synthetic data first.")
        return

    selected_model = st.selectbox("Select Model", ["Logistic Regression", "Random Forest", "K-Nearest Neighbors", 
                                                   "Decision Tree", "Support Vector Machine", "XGBoost"])

    if st.button("Predict"):
        model = joblib.load(f'{selected_model.lower().replace(" ", "_")}_model.pkl')
        data = pd.read_csv('synthetic_data.csv')

        X = data.drop(columns=['hospitalization'])
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        predictions = model.predict_proba(X_scaled)[:, 1]
        data['LOH Probability'] = predictions
        st.write("Predictions:")
        st.write(data)

# Main Streamlit app
def main():
    st.title("LOH Prediction")

    menu = ["Generate Data", "Train Models", "Predict"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Generate Data":
        generate_data()
    elif choice == "Train Models":
        train_models()
    elif choice == "Predict":
        predict()

main()