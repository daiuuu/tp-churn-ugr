"""Entrenamiento, predicción y métricas del árbol de decisión (Fases 4 y 5 de la notebook)."""
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

VARIABLES = ["tenure", "MonthlyCharges", "TotalCharges", "Contract", "InternetService",
             "TechSupport", "PaymentMethod", "SeniorCitizen", "PaperlessBilling"]


@st.cache_resource
def entrenar_modelo(df):
    X = pd.get_dummies(df[VARIABLES])
    y = df["Churn_num"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    modelo = DecisionTreeClassifier(max_depth=4, class_weight="balanced", random_state=42)
    modelo.fit(X_train, y_train)
    return modelo, X.columns, X_test, y_test


def predecir_cliente(modelo, columnas, cliente):
    """Devuelve la probabilidad de baja de un cliente (diccionario con las VARIABLES)."""
    fila = pd.get_dummies(pd.DataFrame([cliente]))
    fila = fila.reindex(columns=columnas, fill_value=0)  # mismas columnas que usó el modelo
    return modelo.predict_proba(fila)[0][1]


def calcular_metricas(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    metricas = {
        "Exactitud": accuracy_score(y_test, y_pred),
        "Precisión": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1-score": f1_score(y_test, y_pred),
    }
    return metricas, confusion_matrix(y_test, y_pred)


def importancia_variables(modelo, columnas, cantidad=6):
    importancia = pd.Series(modelo.feature_importances_, index=columnas)
    return importancia.sort_values(ascending=False).head(cantidad)
