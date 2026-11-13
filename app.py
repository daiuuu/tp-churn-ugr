"""Punto de entrada de la app: configura la página, el menú y muestra la vista elegida."""
import streamlit as st

from plantillas import componentes as ui

st.set_page_config(page_title="Churn | Predicción de bajas", layout="wide")
ui.aplicar_estilos()

paginas = [
    st.Page("vistas/resumen.py", title="Resumen", default=True),
    st.Page("vistas/predecir.py", title="Predecir", url_path="predecir"),
    st.Page("vistas/modelo.py", title="Modelo", url_path="modelo"),
]
pagina = st.navigation(paginas, position="hidden")

ui.encabezado(pagina.title)
pagina.run()
ui.pie()
