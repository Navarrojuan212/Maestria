import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, excel_paths, labels):
        self.data = self.load_data(excel_paths, labels)
        self.prepare_data()

    def load_data(self, excel_paths, labels):
        """Carga los datos desde archivos CSV y les asigna etiquetas."""
        all_data = []
        for excel_path, label in zip(excel_paths, labels):
            data = pd.read_excel(excel_path)
            data['Label'] = label
            all_data.append(data)
        return pd.concat(all_data, ignore_index=True)

    def prepare_data(self):
        """Prepara los datos para el análisis."""
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
        self.data['Elapsed Time (s)'] = (self.data['Timestamp'] - self.data['Timestamp'].iloc[0]).dt.total_seconds()

    def plot_boxplot(self, save_path):
        """Crea un gráfico de violín para SNR de varios conjuntos de datos."""
        plt.figure(figsize=(12, 8))
        sns.violinplot(x='Label', y='SNR', data=self.data, inner='quartile', palette='muted')
        plt.title('Distribución de SNR - Múltiples Laboratorios')
        plt.xlabel('Laboratorio')
        plt.ylabel('SNR (dB)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_path)

# Ejemplo de uso
csv_paths = [
    os.getenv('CSV_PATH_LAB_1'),
    os.getenv('CSV_PATH_LAB_2'),
    os.getenv('CSV_PATH_LAB_3'),
    os.getenv('CSV_PATH_LAB_4'),
    os.getenv('CSV_PATH_LAB_5'),
    os.getenv('CSV_PATH_LAB_6'),
    os.getenv('CSV_PATH_LAB_6_OUTDOOR')
]
labels = ['LAB_1', 'LAB_2', 'LAB_3', 'LAB_4', 'LAB_5', 'LAB_6', 'LAB_6_OUTDOOR']

visualizer = DataVisualizer(csv_paths, labels)
visualizer.plot_boxplot('Boxplot_SNR_Multiple_Labs.png')
print(csv_paths)