import pandas as pd
from utils import cargar_datos, generar_reportes, detectar_outliers_scipy

# 1. Cargar datos con la ruta absoluta de tu archivo Excel
ruta_archivo = r"C:\Users\ACER\Documents\AquaLimpia\AquaLimpia-DataScience\dataset_set_AguasResiduales.xlsx"

# Llamamos a la función
df = cargar_datos(ruta_archivo)

# 2. Análisis de calidad
nulos = df.isnull().sum()
print("Valores nulos por columna:\n", nulos)

outliers_caudal = detectar_outliers_scipy(df, 'caudal_entrada_m3_d')
print(f"Detectados {len(outliers_caudal)} outliers en el caudal.")

# 3. Generar archivos de salida requeridos
generar_reportes(df)
