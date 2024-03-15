import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Asumiendo que las rutas de los archivos CSV son accesibles a través de las variables de entorno.
csv_path_indoor = os.getenv('CSV_PATH_LAB')
csv_path_outdoor = os.getenv('CSV_PATH')

# Cargar y preparar los datos
data1 = pd.read_csv(csv_path_indoor)  # Ajustar el código de limpieza como en indoor.py
data = pd.read_csv(csv_path_outdoor)  # Ajustar el código de limpieza como en Outdoor.py

# A continuación, se crea una figura con ambos gráficos de violín para interior y exterior.
plt.figure(figsize=(16, 10))

# Gráfico de violín para interior
plt.subplot(1, 2, 1)
sns.violinplot(y='SNR', data=data1, inner='quartile', palette='muted')
plt.title('Distribución de SNR - Interior')

# Gráfico de violín para exterior
plt.subplot(1, 2, 2)
sns.violinplot(y='SNR', data=data, inner='quartile', palette='muted')
plt.title('Distribución de SNR - Exterior')

# Guardar la figura combinada de ambos gráficos de violín.
plt.tight_layout()
plt.savefig('img/both_violins.png')

# Si se desea combinar los dos gráficos de violín en un solo gráfico
plt.figure(figsize=(8, 10))
sns.violinplot(data=[data1['SNR'], data['SNR']], inner='quartile', palette=['skyblue', 'lightgreen'])
plt.xticks([0, 1], ['Interior', 'Exterior'])
plt.title('Distribución de SNR - Interior vs Exterior')
plt.ylabel('SNR (dB)')

# Guardar el gráfico combinado en una sola imagen
plt.tight_layout()
plt.savefig('img/combined_violin.png')

# Mostrar los gráficos
#plt.show()
