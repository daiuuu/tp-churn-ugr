"""Vista 1 - Resumen de los datos (RF1, RF2)."""
import streamlit as st

from logica.datos import cargar_datos, histograma_antiguedad, tasa_de_baja
from plantillas import componentes as ui
from plantillas.textos import CONTRATO, INTERNET, SOPORTE

df = cargar_datos()

ui.hero()

ui.titulo("El dataset", f"{ui.numero(len(df))} clientes")
ui.tarjetas([
    ("clientes", "Clientes", ui.numero(len(df))),
    ("baja", "Se fueron", ui.numero(df["Churn_num"].sum())),
    ("porcentaje", "Tasa de baja", f"{df['Churn_num'].mean() * 100:.1f}%"),
    ("reloj", "Antigüedad media", f"{df['tenure'].mean():.0f} meses"),
])

ui.titulo("Tasa de baja por categoría", "% de clientes que se fueron")
tasa_contrato = tasa_de_baja(df, "Contract", CONTRATO)
tasa_internet = tasa_de_baja(df, "InternetService", INTERNET)
tasa_soporte = tasa_de_baja(df, "TechSupport", SOPORTE)
col1, col2, col3 = st.columns(3)
with col1:
    ui.barras("Tipo de contrato", tasa_contrato)
with col2:
    ui.barras("Servicio de internet", tasa_internet)
with col3:
    ui.barras("Soporte técnico", tasa_soporte)

ui.titulo("Antigüedad de los clientes", "cantidad de clientes cada 6 meses")
ui.histograma(*histograma_antiguedad(df))

ui.titulo("Hallazgos")
bajas_primer_anio = (df[df["Churn_num"] == 1]["tenure"] <= 12).mean() * 100
ui.lista_datos([
    ("Contrato mes a mes", "tasa de baja de este tipo de contrato", f"{tasa_contrato['Mes a mes']:.0f}%"),
    ("Primer año", "de las bajas ocurre en los primeros 12 meses", f"{bajas_primer_anio:.0f}%"),
    ("Fibra óptica", "tasa de baja de los clientes con fibra", f"{tasa_internet['Fibra óptica']:.0f}%"),
    ("Sin soporte técnico", "tasa de baja de quienes no lo contratan", f"{tasa_soporte['No']:.0f}%"),
])
