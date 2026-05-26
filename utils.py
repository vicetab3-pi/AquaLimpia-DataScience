import pandas as pd
import numpy as np
from scipy import stats
import joblib

def cargar_datos(ruta):
    """Carga el dataset desde un archivo Excel y realiza limpieza básica."""
    # Usamos read_excel porque confirmaste que es un archivo Excel
    df = pd.read_excel(ruta)
    # Convertir fecha a datetime
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'])
    return df

def detectar_outliers_scipy(df, columna):
    """Utiliza SciPy para detectar valores atípicos mediante Z-score."""
    z_scores = np.abs(stats.zscore(df[columna].dropna()))
    return df[(z_scores > 3)]

def generar_reportes(df):
    """Genera los archivos para el Área de Operaciones y Gestión Ambiental."""
    # Archivo Operaciones
    cols_operaciones = ['fecha_registro', 'planta', 'caudal_entrada_m3_d', 'DBO_entrada_mg_L', 
                        'DBO_salida_mg_L', 'energia_aeracion_kWh', 'lodos_generados_kg_d']
    df_operaciones = df[cols_operaciones]
    df_operaciones.to_csv('reporte_operaciones.csv', index=False)
    
    # Archivo Gestión Ambiental
    cols_ambiental = ['fecha_registro', 'planta', 'DBO_salida_mg_L', 'cumplimiento_norma']
    df_ambiental = df[cols_ambiental]
    df_ambiental.to_csv('reporte_ambiental.csv', index=False)
    
    print("Reportes generados con éxito en la misma carpeta.")

def guardar_modelo_dummy(df, ruta_salida):
    """Ejemplo de uso de joblib para guardar un objeto."""
    joblib.dump(list(df.columns), ruta_salida)
    