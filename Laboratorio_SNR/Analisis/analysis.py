import os
import pandas as pd
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
plt.xlabel('Timestamp')
plt.ylabel('SNR (dB)')
plt.title('SNR vs. Time  --- Laboratory')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Crear el gráfico de dispersión para SNR vs. Tiempo
plt.figure(figsize=(12, 6))
plt.scatter(data['Timestamp'], data['SNR'], label='SNR', color='green')
plt.xlabel('Timestamp')
plt.ylabel('SNR (dB)')
plt.title('Scatter Plot of SNR over Time  --- Laboratory')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Crear el histograma de SNR
plt.figure(figsize=(12, 6))
plt.hist(data['SNR'], bins=30, color='purple')
plt.xlabel('SNR (dB)')
plt.ylabel('Frequency')
plt.title('Histogram of SNR  --- Laboratory')
plt.tight_layout()
plt.show()

# Crear el boxplot de SNR
plt.figure(figsize=(12, 6))
sns.boxplot(data['SNR'], color='orange')
plt.xlabel('SNR (dB)')
plt.title('Boxplot of SNR  --- Laboratory')
plt.tight_layout()
plt.show()
