"""Carga y limpieza de los datos (mismos pasos que la Fase 3 de la notebook)."""
import numpy as np
import pandas as pd
import streamlit as st

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"


@st.cache_data
def cargar_datos():
    df = pd.read_csv(URL)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna().drop(columns=["customerID"])
    df["Churn_num"] = (df["Churn"] == "Yes").astype(int)
    return df


def tasa_de_baja(df, variable, nombres):
    """% de clientes que se fueron en cada categoría de una variable."""
    tasa = df.groupby(variable)["Churn_num"].mean() * 100
    return tasa.rename(index=nombres).sort_values(ascending=False)


def histograma_antiguedad(df):
    """Cantidad de clientes por antigüedad (de a 6 meses), separados en se quedan / se van."""
    bordes = range(0, 78, 6)
    se_quedan = np.histogram(df[df["Churn"] == "No"]["tenure"], bins=bordes)[0]
    se_van = np.histogram(df[df["Churn"] == "Yes"]["tenure"], bins=bordes)[0]
    etiquetas = [f"{b}-{b + 6}" for b in bordes[:-1]]
    return se_quedan, se_van, etiquetas
