from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from preprocessing import preprocess_data

# Cargar el modelo entrenado
model = joblib.load('modelo_churn.pkl')

# Crear la aplicación FastAPI
app = FastAPI()

# Definir la estructura de los datos del cliente
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
    # Convertir los datos del cliente a un formato compatible
    cliente_dict = cliente.dict()
    datos_procesados = preprocess_data(cliente_dict)

    # Realizar predicción
    prediccion = model.predict(datos_procesados)
    probabilidad = model.predict_proba(datos_procesados)

    # Formatear la respuesta
    resultado = {
        "Predicción": "Churn" if prediccion[0] == 1 else "No Churn",
        "Probabilidad": {
            "No Churn": round(probabilidad[0][0], 2),
            "Churn": round(probabilidad[0][1], 2),
        }
    }
    return resultado