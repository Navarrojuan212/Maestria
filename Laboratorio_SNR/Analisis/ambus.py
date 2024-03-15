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


# Función para añadir anotaciones de estadísticas a los gráficos
def add_annotations(ax, data):
    q1 = data.quantile(0.25)
    median = data.median()
    q3 = data.quantile(0.75)
    whisker_low = q1 - 1.5 * (q3 - q1)
    whisker_high = q3 + 1.5 * (q3 - q1)

    outliers = data[(data < whisker_low) | (data > whisker_high)]
    for outlier in outliers:
        ax.text(1, outlier, f'{outlier:.2f}', verticalalignment='center', size='small', color='red', ha='right')

    ax.text(1, median, f'Mediana: {median:.2f}', color='red', ha='right')
    ax.text(1, q1, f'Q1: {q1:.2f}', color='black', ha='right')
    ax.text(1, q3, f'Q3: {q3:.2f}', color='black', ha='right')


# -----------------------------
# Gráficos de violín individuales para "indoor" y "outdoor"
plt.figure(figsize=(16, 10))

# "Indoor"
plt.subplot(1, 2, 1)
sns.violinplot(y='SNR', data=data1, inner='quartile', color='skyblue')
sns.boxplot(y='SNR', data=data1, width=0.1, fliersize=0, linewidth=2,
            boxprops={'facecolor': 'none', 'edgecolor': 'black'},
            whiskerprops={'color': 'black'}, capprops={'color': 'black'},
            medianprops={'color': 'red', 'linestyle': '-'}, showfliers=True)
plt.title('Distribución de SNR - Interior')

# "Outdoor"
plt.subplot(1, 2, 2)
sns.violinplot(y='SNR', data=data, inner='quartile', color='skyblue')
sns.boxplot(y='SNR', data=data, width=0.1, fliersize=0, linewidth=2,
            boxprops={'facecolor': 'none', 'edgecolor': 'black'},
            whiskerprops={'color': 'black'}, capprops={'color': 'black'},
            medianprops={'color': 'red', 'linestyle': '-'}, showfliers=True)
plt.title('Distribución de SNR - Exterior')

plt.tight_layout()
plt.savefig('img/both_violins.png')

# -----------------------------
# Gráfico combinado de violín para "indoor" y "outdoor"
plt.figure(figsize=(10, 8))
combined_data = pd.concat([data1['SNR'], data['SNR']], axis=1)
combined_data.columns = ['Interior', 'Exterior']
sns.violinplot(data=combined_data, inner='quartile', palette=['skyblue', 'lightgreen'])

# Añadir anotaciones
ax = plt.gca()
add_annotations(ax, data1['SNR'])
add_annotations(ax, data['SNR'])

plt.title('Distribución de SNR - Interior vs Exterior')
plt.ylabel('SNR (dB)')

plt.tight_layout()
plt.savefig('img/combined_violin.png')

# plt.show()
