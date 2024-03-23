import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


###########    Base de datos laboratorio SNR (Rutas en mi Linux)   ###############
#   CSV_PATH_LAB_1         ---> 1ro_SDRSharp_20240322_160129Z_SNR.xlsx
#   CSV_PATH_LAB_2         ---> 2do_SDRSharp_20240322_155648Z_SNR.xlsx
#   CSV_PATH_LAB_3         ---> 3ro_SDRSharp_20240322_155300Z_SNR.xlsx
#   CSV_PATH_LAB_4         ---> 4to_SDRSharp_20240322_154709Z_SNR.xlsx
#   CSV_PATH_LAB_5         ---> 5to_SDRSharp_20240322_160516Z_SNR.xlsx
#   CSV_PATH_LAB_6         ---> 6to_SDRSharp_20240322_160903Z_SNR.xlsx
#   CSV_PATH_LAB_6_Outdoor ---> 6to_outdoor_SDRSharp_20240322_161107Z_SNR.xlsx

class DataVisualizer:
    def __init__(self, csv_path):
        self.data = self.load_data(csv_path)
        self.prepare_data()

    def load_data(self, csv_path):
        """Carga los datos desde un archivo CSV."""
        data = pd.read_csv(csv_path)
        return data

    def prepare_data(self):
        """Prepara los datos para el análisis."""
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
        self.data['Elapsed Time (s)'] = (self.data['Timestamp'] - self.data['Timestamp'].iloc[0]).dt.total_seconds()

    def plot_line_graph(self, save_path):
        """Crea un gráfico de línea para SNR vs. Tiempo."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Elapsed Time (s)'], self.data['SNR'], label='SNR', color='orange')
        plt.xlabel('Tiempo (seg)')
        plt.ylabel('SNR (dB)')
        plt.title('SNR vs Tiempo -- Indoor')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)

    def plot_scatter_graph(self, save_path):
        """Crea un gráfico de dispersión para SNR vs. Tiempo."""
        plt.figure(figsize=(12, 6))
        plt.scatter(self.data['Timestamp'], self.data['SNR'], label='SNR', color='green')
        plt.xlabel('Timestamp')
        plt.ylabel('SNR (dB)')
        plt.title('Dispersión SNR vs Tiempo -- Outdoor')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)

    def plot_histogram(self, save_path):
        """Crea un histograma de SNR."""
        plt.figure(figsize=(12, 6))
        plt.hist(self.data['SNR'], bins=30, color='purple')
        plt.xlabel('SNR (dB)')
        plt.ylabel('Frequency')
        plt.title('Histograma SNR -- Indoor')
        plt.tight_layout()
        plt.savefig(save_path)

    def plot_boxplot(self, save_path):
        """Crea un boxplot para SNR."""
        # Añade aquí la implementación para el boxplot, incluyendo cálculo de cuartiles y bigotes
        pass

    def plot_violin_graph(self, save_path):
        """Crea un gráfico de violín para la distribución de SNR."""
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='SNR', data=self.data, inner='quartile', palette='muted')
        plt.title('Distribución de SNR - Interior')
        plt.xlabel('SNR (dB)')
        plt.tight_layout()
        plt.savefig(save_path)

# Uso de la clase
csv_path1 = os.getenv('CSV_PATH_LAB')  # Asegúrate de que esta variable de entorno esté definida
visualizer = DataVisualizer(csv_path1)
visualizer.plot_line_graph('SNR_vs_Tiempo_Indoor.png')
visualizer.plot_scatter_graph('Dispersion_SNR_vs_Tiempo_Indoor.png')
visualizer.plot_histogram('Histograma_SNR_Indoor.png')
visualizer.plot_boxplot('Boxplot_SNR_Indoor.png')
visualizer.plot_violin_graph('Violin_SNR_Indoor.png')

