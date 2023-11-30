import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar el archivo CSV
file_path = os.getenv('CSV_PATH')
data = pd.read_csv(file_path)

# Convertir la columna 'Timestamp' a un objeto datetime y calcular el tiempo transcurrido
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Elapsed Time (s)'] = (data['Timestamp'] - data['Timestamp'].iloc[0]).dt.total_seconds()

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear un gráfico de línea para SNR vs. Tiempo Transcurrido
plt.figure(figsize=(12, 6))
plt.plot(data['Elapsed Time (s)'], data['SNR'], label='SNR', color='blue')
plt.xlabel('Tiempo (Seg)')
plt.ylabel('SNR (dB)')
plt.title('SNR vs. Tiempo (Seg) --- Outdoor')
plt.legend()
plt.tight_layout()
plt.savefig('SNR_vs_Time__Outdoor.png')
#plt.show()

# Crear un gráfico de dispersión para SNR vs. Tiempo Transcurrido
plt.figure(figsize=(12, 6))
plt.scatter(data['Elapsed Time (s)'], data['SNR'], label='SNR', color='green')
plt.xlabel('Tiempo (Seg)')
plt.ylabel('SNR (dB)')
plt.title('Gráfico Dispersión de SNR vs Tiempo Transcurrido --- Outdoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Scatter_Plot_of_SNR_over_Time__Outdoor.png')
#plt.show()

# Crear el histograma de SNR

plt.figure(figsize=(12, 6))
plt.hist(data['SNR'], bins=30, color='purple')
plt.xlabel('SNR (dB)')
plt.ylabel('Frecuencia')
plt.title('Histograma de SNR  --- Outdoor')
plt.tight_layout()
plt.savefig('Histogram_of_SNR_Outdoor.png')
#plt.show()


# Calculamos los cuartiles y el IQR para SNR
q1 = np.percentile(data['SNR'], 25)  # Primer cuartil (Q1)
q3 = np.percentile(data['SNR'], 75)  # Tercer cuartil (Q3)
mediana = np.median(data['SNR'])     # Mediana (Q2)
iqr = q3 - q1                         # Rango intercuartilico (IQR)

# Determinamos los extremos de los bigotes
bigote_inferior = q1 - 1.5 * iqr
bigote_superior = q3 + 1.5 * iqr

# Identificamos los valores atípicos
outliers = data['SNR'][(data['SNR'] < bigote_inferior) | (data['SNR'] > bigote_superior)]

# Creamos el boxplot
plt.figure(figsize=(6, 8))  # Ajustamos el tamaño de la figura para que tenga proporciones similares a la imagen proporcionada
bp = plt.boxplot(data['SNR'], vert=True, patch_artist=True, showfliers=False)

# Establecemos el color de la caja
bp['boxes'][0].set_facecolor('lightblue')

# Anotamos los cuartiles y los valores atípicos
plt.text(1.25, mediana, f'$Mediana = {mediana}$', va='center', ha='center', backgroundcolor='white',color='orange')
plt.text(1.2, q1, f'$q_L = {q1}$', va='center', ha='center', backgroundcolor='white')
plt.text(1.2, q3, f'$q_U = {q3}$', va='center', ha='center', backgroundcolor='white')

for outlier in outliers:
    plt.text(1.2, outlier, f'{outlier}', va='center', ha='center', color='red')

# Añadimos líneas de bigote
plt.plot([1, 1], [bigote_inferior, bigote_superior], color='black', linestyle='-', linewidth=1)

# Añadimos los valores atípicos
plt.plot(np.full(outliers.shape, 1), outliers, 'ro')

# Añadimos títulos y etiquetas
plt.title('Diagrama de Caja de SNR ')
plt.xticks([1], ['SNR'])
plt.ylabel('SNR (dB)')

# Guardar y mostrar el boxplot
plt.tight_layout()
plt.savefig('Boxplot_of_SNR_Outdoor.png')
#plt.show()