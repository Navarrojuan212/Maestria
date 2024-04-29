import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Cargar los datos
file_path = os.getenv('CSV_PATH_LAB_1')
data = pd.read_excel(file_path)

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")
#sns.violinplot(y='SNR', data=data, inner='quartile', color='skyblue')

# Superponer un boxplot con parámetros que lo hagan visible pero no opaco
#box = sns.boxplot(y='SNR', data=data, width=0.1, fliersize=0, linewidth=2,
#                  boxprops={'facecolor':'none', 'edgecolor':'black'},
#                  whiskerprops={'color':'black'}, capprops={'color':'black'},
#                  medianprops={'color':'red'}, showfliers=True)

# Calcular los cuartiles y la mediana
q1 = data['SNR'].quantile(0.25)
median = data['SNR'].median()
q3 = data['SNR'].quantile(0.75)

# Obtener los valores atípicos (outliers)
outliers = data[(data['SNR'] < q1 - 1.5 * (q3 - q1)) | (data['SNR'] > q3 + 1.5 * (q3 - q1))]['SNR']

# Añadir anotaciones para la mediana y los cuartiles
plt.text(0.1, median+0.1, f'Mediana = {median:.2f} dB', verticalalignment='center', size='medium', color='red')
plt.text(0.1, q1+0.1, f'Q1 = {q1:.2f} dB', verticalalignment='center', size='small', color='black')
plt.text(0.1, q3+0.1, f'Q3 = {q3:.2f} dB', verticalalignment='center', size='small', color='black')

# Crear un gráfico de violín para la columna 'SNR'
plt.figure(figsize=(10, 6))
sns.violinplot(y=data['SNR'], data=data, inner='quartile', color='skyblue')
plt.title('SNR LAB_1 103.5 MHz (FM)')
plt.ylabel('SNR (dB)')

# Ajustar los límites del eje Y para ampliar la escala
plt.ylim(20, 30)  # Aquí puedes ajustar los límites según tus necesidades

# Guardando
plt.savefig('Images/Violin_SNR_LAB_1.png')