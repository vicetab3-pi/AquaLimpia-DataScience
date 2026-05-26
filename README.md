# AquaLimpia-DataScience

## 1. Objetivos del Proyecto
El objetivo principal de este análisis es evaluar el desempeño de las plantas de tratamiento de aguas residuales de AquaLimpia S.A. Se busca identificar patrones relacionados con los incumplimientos intermitentes en los niveles de Demanda Biológica de Oxígeno (DBO) y en la eficiencia del tratamiento, para así apoyar la toma de decisiones preventivas y operacionales.

## 2. Proceso Analítico
Para asegurar un flujo de trabajo reproducible, el proyecto se estructuró en las siguientes fases:
* **Ingesta de Datos:** Carga del registro histórico operativo desde el dataset oficial en formato Excel (`dataset_set_AguasResiduales.xlsx`).
* **Evaluación de Calidad:** Inspección automatizada mediante Python para identificar valores nulos y detección de datos atípicos (outliers) en los caudales de entrada utilizando Z-score con la librería `scipy`.
* **Procesamiento Modular:** Utilización de scripts externos (`utils.py`) apoyados en `pandas` para limpiar y procesar la información bajo buenas prácticas de programación.
* **Segmentación y Salida:** División de los datos en dos reportes focalizados para áreas estratégicas de la empresa.

## 3. Resultados
Tras la ejecución del script principal, se obtuvieron los siguientes resultados:
* **Calidad de Datos:** El análisis confirmó la integridad del dataset, registrando 0 valores nulos en todas las columnas y 0 valores atípicos severos en el caudal de entrada.
* **Reporte de Operaciones:** Se generó exitosamente el archivo `reporte_operaciones.csv`, aislando variables críticas como el caudal, consumo de energía y lodos generados para evaluar la eficiencia operativa.
* **Reporte de Gestión Ambiental:** Se generó exitosamente el archivo `reporte_ambiental.csv`, detallando los niveles de DBO del efluente y el estado de cumplimiento normativo para respaldar las fiscalizaciones.
