import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Cargar el scaler y columnas del entrenamiento
scaler = joblib.load('scaler.pkl')  # Asegúrate de guardar el scaler después del entrenamiento
columns = joblib.load('columns.pkl')  # Lista de columnas usadas en el modelo

# Preprocesamiento de los datos del cliente
def preprocess_data(input_data):
    # Convertir la entrada en un DataFrame
    df = pd.DataFrame([input_data])

    # Aplicar transformaciones necesarias
    binary_columns = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    label_encoder = LabelEncoder()
    for column in binary_columns:
        if column in df.columns:
            df[column] = label_encoder.fit_transform(df[column])

    multi_category_columns = ['InternetService', 'Contract', 'PaymentMethod', 'MultipleLines']
    df = pd.get_dummies(df, columns=multi_category_columns, drop_first=True)

    # Asegurar que las columnas coinciden
    for col in columns:
        if col not in df.columns:
            df[col] = 0  # Agregar columnas faltantes
    df = df[columns]  # Reordenar columnas

    # Escalar las variables numéricas
    numerical_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df[numerical_columns] = scaler.transform(df[numerical_columns])

    return df