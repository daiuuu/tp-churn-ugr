[Fase 4 - Modelado]
- Selección de Churn como variable objetivo.
- Conversión de variables categóricas a dummies.
- División 70% entrenamiento / 30% prueba.
- Entrenamiento de un árbol de decisión (max_depth=4, class_weight=balanced).

[Fase 3 - Preparación de los datos]
- Conversión de TotalCharges a número y eliminación de 11 filas sin dato.
- Eliminación de la columna customerID.
- Análisis exploratorio: estadística descriptiva y 5 gráficos.
- Dataset limpio guardado en data/clientes_limpio.csv.

[Fase 2 - Comprensión de los datos]
- Metodología de adquisición de datos y alternativa para construir el dataset.
- Carga del dataset Telco Customer Churn (7.043 clientes, 21 columnas).
- Detección de problemas de calidad: TotalCharges como texto y clases desbalanceadas.

[Fase 1 - Comprensión del negocio]
- Definición del problema de fuga de clientes (churn).
- Objetivo general y objetivos específicos.
- Stakeholders y requerimientos funcionales y no funcionales.
- Creación del README.md.

