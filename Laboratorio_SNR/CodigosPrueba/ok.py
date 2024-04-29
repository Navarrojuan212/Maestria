import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, csv_path):
        self.data = self.load_data(csv_path)
        self.prepare_data()

    def load_data(self, csv_path):
        """Carga los datos desde un archivo CSV."""
        #data = pd.read_csv(csv_path)
        data = pd.read_excel(csv_path)
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
        plt.title('Histogram SNR -- Indoor')
        plt.tight_layout()
        plt.savefig(save_path)

    def plot_boxplot(self, save_path):
        """Crea un boxplot para SNR."""
        plt.figure(figsize=(8, 10))
        sns.violinplot(y='SNR', data=self.data, inner='quartile', color='skyblue')
        box = sns.boxplot(y='SNR', data=self.data, width=0.1, fliersize=0, linewidth=2,
                          boxprops={'facecolor':'none', 'edgecolor':'black'},
                          whiskerprops={'color':'black'}, capprops={'color':'black'},
                          medianprops={'color':'red'}, showfliers=True)

        q1 = self.data['SNR'].quantile(0.25)
        median = self.data['SNR'].median()
        q3 = self.data['SNR'].quantile(0.75)
        outliers = self.data[(self.data['SNR'] < q1 - 1.5 * (q3 - q1)) | (self.data['SNR'] > q3 + 1.5 * (q3 - q1))]['SNR']

        plt.text(0.1, median+0.1, f'Median = {median:.2f} dB', verticalalignment='center', size='medium', color='red')
        plt.text(0.1, q1+0.1, f'Q1 = {q1:.2f} dB', verticalalignment='center', size='small', color='black')
        plt.text(0.1, q3+0.1, f'Q3 = {q3:.2f} dB', verticalalignment='center', size='small', color='black')

        for outlier in outliers:
            plt.text(0.1, outlier, f'{outlier:.2f}', verticalalignment='center', size='small', color='red')

        plt.title('Distribución de SNR - Indoor LAB_6_Outdoor')
        plt.ylabel('SNR (dB)')
        plt.tight_layout()
        plt.savefig(save_path)

    def plot_violin_graph(self, save_path):
        """Crea un gráfico de violín para la distribución de SNR."""
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='SNR', data=self.data, inner='quartile', palette='muted')
        plt.title('Distribución de SNR - Interior')
        plt.xlabel('SNR (dB)')
        plt.tight_layout()
        plt.savefig(save_path)

# Uso de la clase
csv_path1 = os.getenv('CSV_PATH_LAB_3')  # Asegúrate de que esta variable de entorno esté definida
visualizer = DataVisualizer(csv_path1)
visualizer.plot_line_graph('SNR_vs_Tiempo_Indoor_visualizer.png')
visualizer.plot_scatter_graph('Dispersion_SNR_vs_Tiempo_Indoor_visualizer.png')
visualizer.plot_histogram('Histograma_SNR_Indoor_visualizer.png')
visualizer.plot_boxplot('Boxplot_SNR_Indoor_visualizer.png')
visualizer.plot_violin_graph('Violin_SNR_Indoor_visualizer.png')
