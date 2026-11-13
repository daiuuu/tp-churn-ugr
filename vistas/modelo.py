"""Vista 3 - Métricas del modelo (RF5)."""
import streamlit as st

from logica.datos import cargar_datos
from logica.modelo import calcular_metricas, entrenar_modelo, importancia_variables
from plantillas import componentes as ui
from plantillas.textos import VARIABLES

modelo, columnas, X_test, y_test = entrenar_modelo(cargar_datos())
metricas, matriz = calcular_metricas(modelo, X_test, y_test)

ui.encabezado_pagina("Modelo", "Árbol de decisión evaluado sobre el 30% de los clientes que no usó para entrenar.")

ui.titulo("Métricas", f"{ui.numero(len(y_test))} clientes de prueba")
iconos = {"Exactitud": "diana", "Precisión": "mira", "Recall": "lupa", "F1-score": "balanza"}
ui.tarjetas([(iconos[nombre], nombre, f"{valor:.2f}") for nombre, valor in metricas.items()])

ui.titulo("Resultados sobre los clientes de prueba")
col1, col2 = st.columns(2, gap="large")
with col1:
    ui.matriz_confusion(matriz)
with col2:
    importancia = importancia_variables(modelo, columnas).rename(index=VARIABLES)
    ui.barras("Variables más importantes", importancia, formato="{:.2f}")

ui.titulo("Qué significa cada métrica")
ui.lista_datos([
    ("Exactitud", "% de clientes bien clasificados", f"{metricas['Exactitud']:.0%}"),
    ("Precisión", "de los marcados como 'se va', cuántos realmente se fueron", f"{metricas['Precisión']:.0%}"),
    ("Recall", "de los que se fueron, cuántos detectó el modelo", f"{metricas['Recall']:.0%}"),
    ("F1-score", "equilibrio entre precisión y recall", f"{metricas['F1-score']:.2f}"),
])
