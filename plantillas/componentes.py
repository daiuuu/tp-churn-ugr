"""Piezas visuales reutilizables de la app (encabezado, tarjetas, listas, gráficos en HTML)."""
from pathlib import Path

import streamlit as st

CARPETA_STATIC = Path(__file__).parent.parent / "static"

# Íconos de línea (estilo Lucide)
ICONOS = {
    "resumen": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
    "predecir": '<circle cx="10" cy="7" r="4"/><path d="M10.3 15H7a4 4 0 0 0-4 4v2"/><circle cx="17" cy="17" r="3"/><path d="m21 21-1.9-1.9"/>',
    "modelo": '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>',
    "clientes": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "baja": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="22" x2="16" y1="11" y2="11"/>',
    "porcentaje": '<line x1="19" x2="5" y1="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "reloj": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "diana": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "mira": '<circle cx="12" cy="12" r="10"/><line x1="22" x2="18" y1="12" y2="12"/><line x1="6" x2="2" y1="12" y2="12"/><line x1="12" x2="12" y1="6" y2="2"/><line x1="12" x2="12" y1="22" y2="18"/>',
    "lupa": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "balanza": '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    "alerta": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    "escudo": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
}

PAGINAS = [("Resumen", "./", "resumen"), ("Predecir", "predecir", "predecir"), ("Modelo", "modelo", "modelo")]


def html(codigo):
    """Muestra un bloque de HTML."""
    st.markdown(codigo, unsafe_allow_html=True)


def icono(nombre, tam=16):
    return (f'<svg width="{tam}" height="{tam}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{ICONOS[nombre]}</svg>')


def numero(n):
    """Formato argentino: 7.032"""
    return f"{n:,.0f}".replace(",", ".")


def aplicar_estilos():
    css = (CARPETA_STATIC / "estilos.css").read_text(encoding="utf-8")
    html(f"<style>{css}</style>")


def encabezado(pagina_actual):
    links = ""
    for nombre, url, ic in PAGINAS:
        clase = "activo" if nombre == pagina_actual else ""
        links += f'<a href="{url}" target="_self" class="{clase}">{icono(ic, 15)} {nombre}</a>'
    html(f'<div class="barra"><a class="marca" href="./" target="_self">churn</a>'
         f'<nav class="menu">{links}</nav><span class="barra-info">UGR · Ingeniería del Software</span></div>')


def hero():
    html('<div class="hero"><div class="hero-palabra">churn</div>'
         '<div class="hero-texto"><h1>Predicción de bajas</h1>'
         '<p>Detectar a tiempo qué clientes de una empresa de telecomunicaciones están por darse de baja.</p></div>'
         '<div class="hero-etiqueta">CRISP-DM · ÁRBOL DE DECISIÓN</div></div>')


def encabezado_pagina(titulo_pagina, descripcion):
    html(f'<div class="encabezado-pagina"><div class="nombre-pagina">{titulo_pagina}</div><p>{descripcion}</p></div>')


def titulo(texto, derecha=""):
    html(f'<div class="titulo"><h2>{texto}</h2><span>{derecha}</span></div>')


def tarjetas(lista):
    """lista de (icono, etiqueta, valor)"""
    contenido = "".join(f'<div class="tarjeta"><div class="etiqueta">{icono(ic)} {etiqueta}</div>'
                        f'<div class="valor">{valor}</div></div>' for ic, etiqueta, valor in lista)
    html(f'<div class="grilla">{contenido}</div>')


def lista_datos(filas):
    """lista de (texto, detalle, dato): cada fila muestra un dato destacado a la derecha"""
    contenido = "".join(f'<div class="fila"><span>{texto} <small>/ {detalle}</small></span>'
                        f'<span class="dato">{dato}</span></div>' for texto, detalle, dato in filas)
    html(f'<div class="lista">{contenido}</div>')


def barras(titulo_panel, serie, formato="{:.0f}%"):
    """Barras horizontales; la primera (la mayor) se destaca en oliva."""
    maximo = serie.max()
    filas = ""
    for i, (nombre, valor) in enumerate(serie.items()):
        clase = "barra-relleno destacada" if i == 0 else "barra-relleno"
        filas += (f'<div class="barra-fila"><span>{nombre}</span><div class="barra-pista">'
                  f'<div class="{clase}" style="width:{valor / maximo * 100:.1f}%"></div></div>'
                  f'<span class="numero">{formato.format(valor)}</span></div>')
    html(f'<div class="panel"><h3>{titulo_panel}</h3>{filas}</div>')


def histograma(se_quedan, se_van, etiquetas):
    """Columnas apiladas: abajo los que se van (oliva), arriba los que se quedan (topo)."""
    maximo = max(q + v for q, v in zip(se_quedan, se_van))
    columnas = "".join(f'<div class="columna"><div style="height:{v / maximo * 100:.1f}%"></div>'
                       f'<div style="height:{q / maximo * 100:.1f}%"></div></div>'
                       for q, v in zip(se_quedan, se_van))
    ejes = "".join(f"<span>{e}</span>" for e in etiquetas)
    html('<div class="panel"><div class="leyenda"><span><i style="background:var(--topo)"></i>Se quedan</span>'
         '<span><i style="background:var(--oliva)"></i>Se van</span></div>'
         f'<div class="histograma">{columnas}</div><div class="ejes">{ejes}</div>'
         '<div class="eje-titulo">Meses como cliente</div></div>')


def matriz_confusion(m):
    html('<div class="panel"><h3>Matriz de confusión</h3><div class="matriz">'
         '<span></span><span class="encabezado">Predijo: se queda</span><span class="encabezado">Predijo: se va</span>'
         f'<span class="lateral">Se quedó</span><div class="celda acierto"><b>{numero(m[0][0])}</b>Verdaderos negativos</div>'
         f'<div class="celda error"><b>{numero(m[0][1])}</b>Falsos positivos</div>'
         f'<span class="lateral">Se fue</span><div class="celda error"><b>{numero(m[1][0])}</b>Falsos negativos</div>'
         f'<div class="celda acierto"><b>{numero(m[1][1])}</b>Verdaderos positivos</div></div></div>')


def resultado(prob):
    if prob >= 0.5:
        color, ic, estado = "var(--terracota)", "alerta", "Riesgo alto · probablemente se va"
        consejo = "Contactar al cliente y ofrecerle un beneficio o un contrato más largo."
    else:
        color, ic, estado = "var(--oliva)", "escudo", "Riesgo bajo · probablemente se queda"
        consejo = "No requiere acción inmediata. Seguir monitoreando."
    html(f'<div class="panel resultado"><div class="estado" style="color:{color}">{icono(ic, 18)} {estado}</div>'
         f'<div class="porcentaje">{prob * 100:.0f}%</div><div>probabilidad de baja</div>'
         f'<div class="barra-riesgo"><div style="width:{prob * 100:.0f}%;background:{color}"></div></div>'
         f'<div>{consejo}</div></div>')


def resultado_vacio():
    html('<div class="panel resultado vacio">Completá los datos del cliente y tocá '
         '<b>Calcular riesgo</b> para ver su probabilidad de baja.</div>')


def pie():
    html('<div class="pie"><span>Daiana Soria Piola · Ingeniería del Software · UGR</span>'
         '<span>Datos: IBM Telco Customer Churn</span></div>')
