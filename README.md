# Informe Final: Predicción de Abandono de Clientes

## 1. Introducción

El Presente proyecto tiene como objetivo predecir la probabilídad de abandono (Churn) 
de clientes en un servicio basado en sus caracteristicas y comportamientos previos. 
La retencion de clientes es un desafio clave en muchas industrias, y contar con 
herramientas predictivas permite diseñar estrategias proactivas para mitigar el churn.

**Problema**: ¿Qué caracteristicas o comportamientos son indicadores clave de abandono 
de clientes?

**Objetivo**: Construir un modelo predictivo que identifique clientes con mayor riesgo 
de abandonar el servicio y proporcionar insights basados en las caracteristicas más 
importantes.

## 2. Metodología

El proyecto se desarrolló en varias etapas:
    1. **Carga y exploración de Datos**:
        - Inspección de valores nulos y outliers.
        - Visualización de la distribución de la variable objetivo(Churn).
    2. **Análisis Exploratorio de Datos (EDA)**:
        - Análisis de correlación entre variables.
        - Visualización de características relevantes para entender el comportamiento de los clientes.
    3. **Preprocesamiento de Datos**:
        - Codificación de variables categóricas.
        - Normalización de características numéricas.
        - Manejo de desequilibrios en las clases con técnicas como SMOTE.
    4. **Construcción y Evaluación de modelos**:
        - Pruebas iniciales con modelos de regresión logística, árboles de decisión y Random Forest.
        - Optimización del modelo Random Forest con GridSearchCV.
        - Evaluación basada en métricas como precisión, recall y F1-score.
    5. **Importancia de Características**:
        - Análisis de las características más relevantes para la predicción.

## 3. Resultados

### Desempeño del modelo

El modelo **Random Forest** Optimizado logró una precisión general del 75.20% en el conjunto de prueba.
Algunas observaciones clave sobre el desempeño del modelo incluyen:

    - La clase 'No Churn' tuvo un mejor rendimiento con un recall de 76%, indicando que el modelo identifica correctamente la mayoría de los clientes que no abandonan el servicio.

    - La clase 'Churn' mostró un recall del 73%, lo cual es positivo pero puede mejorarse para minimizar falsos negativos (clientes que abandonan y no son detectados).
    
El balance entre precisión y recall indica que el modelo es razonablemente robusto, aunque podría beneficiarse de un análisis más profundo de las características y de ajustes adicionales.

### Importancia de Características

Basado en el análisis de importáncia de características del modelo optimizado, las siguientes variables resultaron ser las más relevantes para predecir el churn:

1. **OnlineSecurity**: La falta de un servicio de seguridad en línea tiene el mayor impacto en la probabilidad de abandono.
2. **Tenure**: Los clientes con mayor antigüedad tienen menos probabilidad de abandonar el servicio.
3. **Contract_Two year**: Contratos de dos años disminuyen la probabilidad de churn.
4. **PaymentMethod_Electronic check**: Este método de pago se asocia con una mayor probabilidad de churn, posiblemente por costos mas altos.

Estas características destacan aspectos específicos del servicio que influyen significativamente en la retención o abandono de clientes.

### Recomendaciones para la Retención de clientes.

1. **Promover la Seguridad en Línea**:
    - Ofrecer paquetes de seguridad en línea gratuitos o con descuento a clientes sin este servicio podría mejorar la retención.
2. **Incentivar la Permanencia**:
    - Diseñar programas de fidelización que recompensen a clientes con mayor antoigüedad y promuevan contratos a largo plazo.
3. **Analizar Métodos de Pago**:
    - Realizar un análisis costo-beneficio del servidor de fibra óptica, y explorar estrategias de precios más competitivos.
5. **Atención personalizada**:
    - Identificar clientes en riesgo con base en las características clave(e.g., corto tiempo de tenencia, falta de servicios adicionales) y ofrecer atención personalizada.



