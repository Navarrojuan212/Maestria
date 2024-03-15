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
plt.savefig('SNR_vs_Time_Outdoor.png')
#plt.show()

# Crear un gráfico de dispersión para SNR vs. Tiempo Transcurrido
plt.figure(figsize=(12, 6))
plt.scatter(data['Elapsed Time (s)'], data['SNR'], label='SNR', color='green')
plt.xlabel('Tiempo (Seg)')
plt.ylabel('SNR (dB)')
plt.title('Dispersión de SNR vs Tiempo - Outdoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Dispersion_SNR_vs_Tiempo_Outdoor.png')
#plt.show()

# Crear el histograma de SNR

plt.figure(figsize=(12, 6))
plt.hist(data['SNR'], bins=30, color='purple')
plt.xlabel('SNR (dB)')
plt.ylabel('Frecuencia')
plt.title('Histograma SNR - Outdoor')
plt.tight_layout()
plt.savefig('Histograma_SNR_Outdoor.png')
#plt.show()


# Calculamos los cuartiles y el IQR para SNR
q1 = np.percentile(data['SNR'], 25)  # Primer cuartil (Q1 = q_L)
q3 = np.percentile(data['SNR'], 75)  # Tercer cuartil (Q3 = q_U)
mediana = np.median(data['SNR'])     # Mediana (Q2 = q_M)
iqr = q3 - q1                         # Rango intercuartilico (IQR)

# Determinamos los extremos de los bigotes
bigote_inferior = q1 - 1.5 * iqr
bigote_superior = q3 + 1.5 * iqr
print(f"$Inferior = {bigote_inferior}$\n"+
      f"$Superior = {bigote_superior}$")

print(f"$IQR={iqr}$")

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
plt.title('Boxplot SNR - Outdoor ')
plt.xticks([1], ['SNR'])
plt.ylabel('SNR (dB)')

# Guardar y mostrar el boxplot
plt.tight_layout()
plt.savefig('img/Boxplot_SNR_Outdoor.png')
#plt.show()

## Violin
# Asumiendo que tienes un DataFrame llamado 'data' y quieres graficar la columna 'SNR'
plt.figure(figsize=(8, 10))  # Tamaño del gráfico ajustado para la orientación vertical

# Dibujar el gráfico de violín con cuartiles
sns.violinplot(y='SNR', data=data, inner='quartile', color='lightblue')

# Superponer un boxplot con transparencia
sns.boxplot(y='SNR', data=data, width=0.1, fliersize=0, linewidth=2, boxprops={'facecolor':'none', 'edgecolor':'black'}, whiskerprops={'color':'black'}, capprops={'color':'black'}, medianprops={'color':'black'})
#sns.boxplot(y='SNR', data=data, width=0.1, fliersize=0, whis=0, linewidth=2, color='darkblue', boxprops=dict(alpha=.3))

# Configuración del título y las etiquetas
plt.title('Distribución de SNR - Interior')
plt.ylabel('SNR (dB)')  # Etiqueta para el eje Y en lugar del eje X

# Guardar y Mostrar el gráfico
plt.tight_layout()
plt.savefig('img/Violin_SNR_Outdoor.png')
#plt.show()