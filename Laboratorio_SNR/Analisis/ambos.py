import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Asumiendo que las rutas de los archivos CSV son accesibles a través de las variables de entorno.
csv_path_indoor = os.getenv('CSV_PATH_LAB')
csv_path_outdoor = os.getenv('CSV_PATH')

# Cargar y preparar los datos
data1 = pd.read_csv(csv_path_indoor)  # Asumimos que este es tu conjunto de datos "indoor"
data = pd.read_csv(csv_path_outdoor)  # Asumimos que este es tu conjunto de datos "outdoor"

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear figura para los gráficos de violín para "indoor" y "outdoor"
plt.figure(figsize=(16, 10))

# -----------------------------
# Gráfico de violín para "indoor"
plt.subplot(1, 2, 1)
sns.violinplot(y='SNR', data=data1, inner='quartile', color='skyblue')
sns.boxplot(y='SNR', data=data1, width=0.1, fliersize=0, linewidth=2,
            boxprops={'facecolor':'none', 'edgecolor':'black'},
            whiskerprops={'color':'black'}, capprops={'color':'black'},
            medianprops={'color':'red', 'linestyle':'-'}, showfliers=True)

# Calculando y anotando estadísticas para "indoor"
q1_indoor = data1['SNR'].quantile(0.25)
median_indoor = data1['SNR'].median()
q3_indoor = data1['SNR'].quantile(0.75)
plt.text(0.1, median_indoor, f'Mediana: {median_indoor:.2f}', color='red')
plt.text(0.1, q1_indoor, f'Q1: {q1_indoor:.2f}', color='black')
plt.text(0.1, q3_indoor, f'Q3: {q3_indoor:.2f}', color='black')

plt.title('Distribución de SNR - Interior')

# -----------------------------
# Gráfico de violín para "outdoor"
plt.subplot(1, 2, 2)
sns.violinplot(y='SNR', data=data, inner='quartile', color='skyblue')
sns.boxplot(y='SNR', data=data, width=0.1, fliersize=0, linewidth=2,
            boxprops={'facecolor':'none', 'edgecolor':'black'},
            whiskerprops={'color':'black'}, capprops={'color':'black'},
            medianprops={'color':'red', 'linestyle':'-'}, showfliers=True)

# Calculando y anotando estadísticas para "outdoor"
q1_outdoor = data['SNR'].quantile(0.25)
median_outdoor = data['SNR'].median()
q3_outdoor = data['SNR'].quantile(0.75)
plt.text(0.1, median_outdoor, f'Mediana: {median_outdoor:.2f}', color='red')
plt.text(0.1, q1_outdoor, f'Q1: {q1_outdoor:.2f}', color='black')
plt.text(0.1, q3_outdoor, f'Q3: {q3_outdoor:.2f}', color='black')

plt.title('Distribución de SNR - Exterior')

# Guardar la figura combinada de ambos gráficos de violín en la carpeta 'img/'
plt.tight_layout()
plt.savefig('img/both_violins.png')

# Si deseas combinar ambos gráficos de violín en un solo gráfico para comparación directa
plt.figure(figsize=(8, 10))
sns.violinplot(data=[data1['SNR'], data['SNR']], inner='quartile', palette=['skyblue', 'lightgreen'])
plt.xticks([0, 1], ['Interior', 'Exterior'])
plt.title('Distribución de SNR - Interior vs Exterior')
plt.ylabel('SNR (dB)')

# Guardar el gráfico combinado en una sola imagen en la carpeta 'img/'
plt.tight_layout()
plt.savefig('img/combined_violin.png')

# Mostrar los gráficos
#plt.show()
