import joblib
import numpy as np

model = joblib.load('modelo_churn.pkl')
datos = np.array([[12, 1, 1, 1, 1, 0, 0, 0, 200.5, 0]])
prediccion = model.predict(datos)
probabilidad = model.predict_proba(datos)
print("Predicción:", prediccion)
print("Probabilidad:", probabilidad)