import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataHandler:
    def __init__(self, env_var, encoding='utf-8'):
        file_path = os.getenv(env_var)
        if file_path is None:
            raise ValueError("No se ha definido la variable de entorno con la ruta del archivo.")
            # Determinar la extensión del archivo y cargar los datos apropiadamente
        if file_path.endswith('.csv'):
            try:
                self.data = pd.read_csv(file_path, encoding=encoding)
            except UnicodeDecodeError:
                self.data = pd.read_csv(file_path, encoding='iso-8859-1')  # Otro intento con una codificación común
        elif file_path.endswith(('.xls', '.xlsx')):
            self.data = pd.read_excel(file_path)
        else:
            raise ValueError("El archivo especificado no tiene una extensión reconocida (.csv, .xls, .xlsx).")
        self.process_data()

    def process_data(self):
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
        self.data['Elapsed Time (s)'] = (self.data['Timestamp'] - self.data['Timestamp'].iloc[0]).dt.total_seconds()

class SNRPlotter:
    def __init__(self, data):
        self.data = data
        sns.set(style="whitegrid")

    def plot_time_series(self,  xlabel='Tiempo (s)', ylabel='SNR (dB)', title='SNR vs Tiempo', save_path='ruta'):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Elapsed Time (s)'], self.data['SNR'], label='SNR', color='blue')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_scatter_with_trendline(self, xlabel='Tiempo (Seg)', ylabel='SNR (dB)', title='Dispersión de SNR vs Tiempo', save_path='ruta'):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x=self.data['Elapsed Time (s)'], y=self.data['SNR'], label='SNR', color='green')
        sns.regplot(x=self.data['Elapsed Time (s)'], y=self.data['SNR'], scatter=False,
                    color='blue')  # Agregar línea de tendencia
        #plt.scatter(self.data['Elapsed Time (s)'], self.data['SNR'], label='SNR', color='green')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_histogram(self, xlabel='SNR (dB)', ylabel='Frecuencia', title='Histogram de SNR', save_path='ruta'):
        plt.figure(figsize=(12, 6))
        plt.hist(self.data['SNR'], bins=30, color='purple')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_violin_and_box(self, xlabel='', ylabel='SNR (dB)', title='Distribución de SNR con Violin y Boxplot', save_path='ruta'):
        plt.figure(figsize=(8, 10))
        sns.violinplot(y='SNR', data=self.data, inner='quartile', color='skyblue')
        sns.boxplot(y='SNR', data=self.data, width=0.1, fliersize=0, linewidth=2,
                    boxprops={'facecolor': 'none', 'edgecolor': 'black'},
                    whiskerprops={'color': 'black'}, capprops={'color': 'black'},
                    medianprops={'color': 'red'}, showfliers=True)

        # Calculamos los cuartiles y el IQR para SNR
        q1 = np.percentile(self.data['SNR'], 25)  # Primer cuartil (Q1 = q_L)
        q3 = np.percentile(self.data['SNR'], 75)  # Tercer cuartil (Q3 = q_U)
        median = np.median(self.data['SNR'])  # Mediana (Q2 = q_M)
        iqr = q3 - q1  # Rango intercuartilico (IQR)

        # Determinamos los extremos de los bigotes
        bigote_inferior = q1 - 1.5 * iqr
        bigote_superior = q3 + 1.5 * iqr

        outliers = self.data[(self.data['SNR'] < bigote_inferior ) | (self.data['SNR'] > bigote_superior)]['SNR']

        # Añadir anotaciones para la mediana y los cuartiles
        plt.text(0.1, median + 0.1, f'Mediana = {median:.2f} dB', verticalalignment='center', size='medium',
                 color='red')
        plt.text(0.1, q1 + 0.1, f'Q1 = {q1:.2f} dB', verticalalignment='center', size='small', color='black')
        plt.text(0.1, q3 + 0.1, f'Q3 = {q3:.2f} dB', verticalalignment='center', size='small', color='black')

        # Anotar los valores atípicos
        for outlier in outliers:
            plt.text(0.1, outlier, f'{outlier:.2f}', verticalalignment='center', size='small', color='red')

        # Configuración del título y las etiquetas
        plt.title(title)
        plt.ylabel(ylabel)

        # Guardar y mostrar el boxplot
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

# Lista de nombres de las variables de entorno que contienen las rutas de las bases de datos
env_vars = [
    'CSV_PATH_LAB_1', 'CSV_PATH_LAB_2', 'CSV_PATH_LAB_3', 'CSV_PATH_LAB_4', 'CSV_PATH_LAB_5',
    'CSV_PATH_LAB_6', 'CSV_PATH_LAB_6_Outdoor', 'CSV_PATH_SOTANO_1_B', 'CSV_PATH_SOTANO_2_E'
]

# Bucle para procesar cada base de datos y generar los gráficos correspondientes
for env_var in env_vars:
    # Crear una instancia del manejador de datos y del plotter con los datos cargados
    try:
        data_handler = DataHandler(env_var)
        plotter = SNRPlotter(data_handler.data)

        # Personalizar los nombres de archivo según la variable de entorno
        base_filename = env_var.replace('CSV_PATH_', '')

        # Generar gráficos con personalizaciones
        plotter.plot_time_series(
            xlabel='Tiempo transcurrido (s)',
            ylabel='Relación Señal-Ruido (dB)',
            title=f'Relación Señal-Ruido a lo largo del tiempo - {base_filename}',
            save_path=f'Imagesss/TimeSeries/{base_filename}_SNR_TimeSeriesPlot.png'
        )

        plotter.plot_scatter_with_trendline(
            xlabel='Tiempo transcurrido (s)',
            ylabel='Relación Señal-Ruido (dB)',
            title=f'Dispersión de la Relación Señal-Ruido - {base_filename}',
            save_path=f'Imagesss/Scatter/{base_filename}_SNR_ScatterPlot.png'
        )

        plotter.plot_histogram(
            xlabel='Relación Señal-Ruido (dB)',
            ylabel='Frecuencia de aparición',
            title=f'Historiograma de la Relación Señal-Ruido - {base_filename}',
            save_path=f'Imagesss/Histogram/{base_filename}_SNR_HistogramPlot.png'
        )

        plotter.plot_violin_and_box(
            xlabel='Datos',
            ylabel='Relación Señal-Ruido (dB)',
            title=f'Distribución y Caja de la Relación Señal-Ruido - {base_filename}',
            save_path=f'Imagesss/Violin/{base_filename}_SNR_ViolinPlot.png'
        )
    except ValueError as e:
        print(f"Error: {e} (posiblemente la variable de entorno {env_var} no está definida o el archivo no se pudo leer correctamente)")

