import os
import pandas as pd

# Lista de rutas de archivos Excel
excel_files = [
    os.getenv('CSV_PATH_LAB_1'),
    os.getenv('CSV_PATH_LAB_2'),
    os.getenv('CSV_PATH_LAB_3'),
    os.getenv('CSV_PATH_LAB_4'),
    os.getenv('CSV_PATH_LAB_5'),
    os.getenv('CSV_PATH_LAB_6'),
    os.getenv('CSV_PATH_LAB_6_Outdoor')
]

# Leer cada archivo Excel y guardar los datos en un diccionario
data_frames = {}
for i, file_path in enumerate(excel_files, start=1):
    data_frames[f'Lab_{i}'] = pd.read_excel(file_path)

# Fusionar los DataFrames en uno solo usando la columna de tiempo como índice
combined_data = pd.concat(data_frames.values(), axis=1)

# Verificar el DataFrame combinado
print(combined_data.head())
print(combined_data.info())
