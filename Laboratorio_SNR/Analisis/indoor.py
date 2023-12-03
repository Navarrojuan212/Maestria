import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Acceder a la variable de entorno
csv_path = os.getenv('CSV_PATH_LAB')

# Cargar y preparar los datos
data = pd.read_csv(csv_path)
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Configurando el estilo de los gráficos
sns.set(style="whitegrid")

# Crear el gráfico de línea para SNR vs. Tiempo
plt.figure(figsize=(12, 6))
plt.plot(data['Timestamp'], data['SNR'], label='SNR', color='blue')
plt.xlabel('Tiempo (seg)')
plt.ylabel('SNR (dB)')
plt.title('SNR vs Tiempo -- Indoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('SNR_vs_Tiempo_Indoor.png')
#plt.show()

# Crear el gráfico de dispersión para SNR vs. Tiempo
plt.figure(figsize=(12, 6))
plt.scatter(data['Timestamp'], data['SNR'], label='SNR', color='green')
plt.xlabel('Timestamp')
plt.ylabel('SNR (dB)')
plt.title('Dispersión SNR vs Tiempo -- Outdoor')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Dispersion_SNR_vs_Tiempo_Indoor.png')
#plt.show()

# Crear el histograma de SNR
plt.figure(figsize=(12, 6))
plt.hist(data['SNR'], bins=30, color='purple')
plt.xlabel('SNR (dB)')
plt.ylabel('Frequency')
plt.title('Histograma SNR -- Indoor')
plt.tight_layout()
plt.savefig('Histograma_SNR_Indoor.png')
#plt.show()

# Crear el boxplot de SNR
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
plt.title('Boxplot SNR - Indoor ')
plt.xticks([1], ['SNR'])
plt.ylabel('SNR (dB)')

# Guardar y mostrar el boxplot
plt.tight_layout()
plt.savefig('Boxplot_SNR_Indoor.png')
#plt.show()

# --------------------------
#plt.figure(figsize=(12, 6))
#sns.boxplot(data['SNR'], color='orange')
#plt.xlabel('SNR (dB)')
#plt.title('Boxplot SNR -- Indoor')
#plt.tight_layout()
#plt.savefig('Boxplot_SNR_Indoor.png')
#plt.show()
# -----------------------------------
