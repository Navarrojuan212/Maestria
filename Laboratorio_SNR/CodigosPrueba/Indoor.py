import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Acceder a la variable de entorno
csv_path1 = os.getenv('CSV_PATH_LAB_1')

# Cargar y preparar los datos
#data1 = pd.read_csv(csv_path1)
data1 = pd.read_excel(csv_path1)
data1['Timestamp'] = pd.to_datetime(data1['Timestamp'])
data1['Elapsed Time (s)'] = (data1['Timestamp'] - data1['Timestamp'].iloc[0]).dt.total_seconds()

# Configurando el estilo de los gráficos
sns.set(style="whitegrid")

# Crear el gráfico de línea para SNR vs. Tiempo
plt.figure(figsize=(12, 6))
plt.plot(data1['Elapsed Time (s)'], data1['SNR'], label='SNR', color='orange')
#plt.plot(data1['Timestamp'], data1['SNR'], label='SNR', color='blue')
plt.xlabel('Tiempo (seg)')
plt.ylabel('SNR (dB)')
plt.title('SNR vs Tiempo -- Indoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Images/SNR_vs_Tiempo_Indoor.png')
#plt.show()

# Crear el gráfico de dispersión para SNR vs. Tiempo
plt.figure(figsize=(12, 6))
plt.scatter(data1['Timestamp'], data1['SNR'], label='SNR', color='green')
plt.xlabel('Timestamp')
plt.ylabel('SNR (dB)')
plt.title('Dispersión SNR vs Tiempo -- Outdoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Images/Dispersion_SNR_vs_Tiempo_Indoor.png')
#plt.show()

# Crear el histograma de SNR
plt.figure(figsize=(12, 6))
plt.hist(data1['SNR'], bins=30, color='purple')
plt.xlabel('SNR (dB)')
plt.ylabel('Frequency')
plt.title('Histogram SNR -- Indoor')
plt.tight_layout()
plt.savefig('Images/Histograma_SNR_Indoor.png')
#plt.show()

# Crear el boxplot de SNR
# Calculamos los cuartiles y el IQR para SNR
q1_indoor = np.percentile(data1['SNR'], 25)  # Primer cuartil (Q1 = q_L)
q3_indoor = np.percentile(data1['SNR'], 75)  # Tercer cuartil (Q3 = q_U)
mediana_indoor = np.median(data1['SNR'])     # Mediana (Q2 = q_M)
iqr_indoor = q3_indoor - q1_indoor                         # Rango intercuartilico (IQR)
print(f"$Mediana = {mediana_indoor}$")
# Determinamos los extremos de los bigotes
bigote_inferior_indoor = q1_indoor - 1.5 * iqr_indoor
bigote_superior_indoor = q3_indoor + 1.5 * iqr_indoor
print(f"$Inferior = {bigote_inferior_indoor}$\n" +
      f"$Superior = {bigote_superior_indoor}$")

# Identificamos los valores atípicos
outliers_indoor = data1['SNR'][(data1['SNR'] < bigote_inferior_indoor) | (data1['SNR'] > bigote_superior_indoor)]

# Creamos el boxplot
plt.figure(figsize=(6, 8))  # Ajustamos el tamaño de la figura para que tenga proporciones similares a la imagen proporcionada
bp_indoor = plt.boxplot(data1['SNR'], vert=True, patch_artist=True, showfliers=False)

# Establecemos el color de la caja
bp_indoor['boxes'][0].set_facecolor('lightblue')

# Anotamos los cuartiles y los valores atípicos
plt.text(1.25, mediana_indoor, f'$Mediana = {mediana_indoor}$', va='center', ha='center', backgroundcolor='white', color='red')
plt.text(1.2, q1_indoor, f'$q_L = {q1_indoor}$', va='center', ha='center', backgroundcolor='white')
plt.text(1.2, q3_indoor, f'$q_U = {q3_indoor}$', va='center', ha='center', backgroundcolor='white')

for outlier in outliers_indoor:
    plt.text(1.2, outlier, f'{outlier}', va='center', ha='center', color='red')

# Añadimos líneas de bigote
plt.plot([1, 1], [bigote_inferior_indoor, bigote_superior_indoor], color='black', linestyle='-', linewidth=1)

# Añadimos los valores atípicos
plt.plot(np.full(outliers_indoor.shape, 1), outliers_indoor, 'ro')

# Añadimos títulos y etiquetas
plt.title('Boxplot SNR - Indoor ')
plt.xticks([1], ['SNR'])
plt.ylabel('SNR (dB)')

# Guardar y mostrar el boxplot
plt.tight_layout()
plt.savefig('Images/Boxplot_SNR_Indoor.png')
#plt.show()

# Gráfico de violín para visualizar la distribución de SNR
##plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico según necesites
##sns.violinplot(x=data1['SNR'])  # Cambia 'data1' por el nombre de tu DataFrame
##plt.title('Distribución de SNR - Interior')  # Ajusta el título según corresponda
##plt.xlabel('SNR')  # Etiqueta para el eje X


# Asumiendo que tienes un DataFrame llamado 'data' y quieres graficar la columna 'SNR'
plt.figure(figsize=(10, 6))
sns.violinplot(x='SNR', data=data1, inner = 'quartile', palette='muted')  # El argumento 'inner' se utiliza para mostrar los cuartiles
#sns.violinplot(x='SNR', data=data1, inner='box', palette='muted')  # El argumento 'inner' se utiliza para mostrar los cuartiles

# Calcular estadísticas como la mediana y los cuartiles
median = data1['SNR'].median()
q1 = data1['SNR'].quantile(0.25)
q3 = data1['SNR'].quantile(0.75)

# Añadir anotaciones para la mediana y los cuartiles
plt.text(median + 0.1, 0.04, f'Mediana = {median}', horizontalalignment='left', size='medium', color='black', weight='semibold')
plt.text(q1 - 0.1, 0.04, f'q1 = {q1}', horizontalalignment='right', size='medium', color='black', weight='semibold')
plt.text(q3 + 0.1, 0.04, f'q3 = {q3}', horizontalalignment='left', size='medium', color='black', weight='semibold')

plt.title('Distribución de SNR - Interior')
plt.xlabel('SNR (dB)')
#plt.show()

# Guardar y mostrar el boxplot
plt.tight_layout()
plt.savefig('Images/Violin_SNR_Indoor.png')
#plt.show()
