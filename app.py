from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Cargar el modelo, escalador y columnas esperadas
model = joblib.load('modelo_churn.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el esquema de los datos del cliente
class DatosCliente(BaseModel):
    tenure: float
    MonthlyCharges: float
    TotalCharges: float
    OnlineSecurity: int
    Contract_Two_year: int
    PaymentMethod_Electronic_check: int
    InternetService_Fiber_optic: int
    TechSupport: int
    OnlineBackup: int
    DeviceProtection: int
    InternetService_No: int

# Endpoint para predecir
@app.post("/predecir")
def predecir(cliente: DatosCliente):
    try:
        # Convertir los datos del cliente en un DataFrame
        datos = pd.DataFrame([cliente.dict()])

        # Comparar las columnas actuales con las esperadas
        print("Columnas del DataFrame:")
        print(datos.columns.tolist())
        print("\nColumnas esperadas:")
        print(expected_columns.tolist())

        # Reordenar las columnas según las esperadas por el modelo
        datos = datos.reindex(columns=expected_columns, fill_value=0)

        # Validar el DataFrame generado
        print("Datos después de reordenar:")
        print(datos.head())

        # Escalar las características numéricas
        datos_scaled = scaler.transform(datos)

        # Realizar la predicción
        prediccion = model.predict(datos_scaled)
        probabilidad = model.predict_proba(datos_scaled)

        # Formatear la respuesta
        return {
            "Predicción": "Churn" if prediccion[0] == 1 else "No Churn",
            "Probabilidad": {
                "No Churn": round(probabilidad[0][0], 2),
                "Churn": round(probabilidad[0][1], 2)
            }
        }
    except Exception as e:
        # Capturar errores específicos y enviar una respuesta descriptiva
        raise HTTPException(status_code=500, detail=f"Error en el procesamiento: {str(e)}")