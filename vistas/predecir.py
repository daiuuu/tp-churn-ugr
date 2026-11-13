"""Vista 2 - Predecir si un cliente se dará de baja (RF3, RF4)."""
import streamlit as st

from logica.datos import cargar_datos
from logica.modelo import entrenar_modelo, predecir_cliente
from plantillas import componentes as ui
from plantillas.textos import CONTRATO, INTERNET, PAGO, SOPORTE

modelo, columnas, _, _ = entrenar_modelo(cargar_datos())

ui.encabezado_pagina("Predecir", "Cargá los datos de un cliente para estimar su probabilidad de baja.")
ui.titulo("Datos del cliente", "el cargo total se estima como antigüedad × cargo mensual")

col_formulario, col_resultado = st.columns([3, 2], gap="large")

with col_formulario:
    with st.form("formulario"):
        c1, c2 = st.columns(2)
        tenure = c1.slider("Antigüedad (meses)", 0, 72, 6)
        monthly = c1.number_input("Cargo mensual (USD)", 18.0, 120.0, 85.0)
        contract = c1.selectbox("Tipo de contrato", list(CONTRATO), format_func=CONTRATO.get)
        payment = c1.selectbox("Método de pago", list(PAGO), format_func=PAGO.get)
        internet = c2.selectbox("Servicio de internet", list(INTERNET), index=1, format_func=INTERNET.get)
        support = c2.selectbox("Soporte técnico", list(SOPORTE), index=1, format_func=SOPORTE.get)
        senior = c2.radio("Adulto mayor", ["No", "Sí"], horizontal=True)
        paperless = c2.radio("Factura digital", ["Sí", "No"], horizontal=True)
        enviar = st.form_submit_button("Calcular riesgo")

with col_resultado:
    if enviar:
        if internet == "No":
            support = "No internet service"
        cliente = {
            "tenure": tenure, "MonthlyCharges": monthly, "TotalCharges": tenure * monthly,
            "Contract": contract, "InternetService": internet, "TechSupport": support,
            "PaymentMethod": payment, "SeniorCitizen": 1 if senior == "Sí" else 0,
            "PaperlessBilling": "Yes" if paperless == "Sí" else "No",
        }
        ui.resultado(predecir_cliente(modelo, columnas, cliente))
    else:
        ui.resultado_vacio()
