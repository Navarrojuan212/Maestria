import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV files for Indoor and Outdoor
file_path_outdoor = os.getenv('CSV_PATH')
outdoor_data = pd.read_csv(file_path_outdoor)
outdoor_data['Environment'] = 'Outdoor'  # Add an 'Environment' column for outdoor data

file_path_indoor = os.getenv('CSV_PATH_LAB')
indoor_data = pd.read_csv(file_path_indoor)
indoor_data['Environment'] = 'Indoor'  # Add an 'Environment' column for indoor data

# Configurando el estilo de los gráficos
sns.set(style="whitegrid")

# Combine the indoor and outdoor datasets
combined_data = pd.concat([indoor_data, outdoor_data])

# Calculate the quartiles and median using numpy
q1_indoor = np.percentile(indoor_data['SNR'], 25)  # Q1
q3_indoor = np.percentile(indoor_data['SNR'], 75)  # Q3
median_indoor = np.median(indoor_data['SNR'])      # Median

q1_outdoor = np.percentile(outdoor_data['SNR'], 25)  # Q1
q3_outdoor = np.percentile(outdoor_data['SNR'], 75)  # Q3
median_outdoor = np.median(outdoor_data['SNR'])      # Median

# Create the boxplot
plt.figure(figsize=(12, 8))
boxplot = sns.boxplot(x='Environment', y='SNR', data=combined_data, palette=["lightblue", "lightgreen"])

# Annotate the quartiles and median for each box
plt.text(0, q1_indoor, f'Q1={q1_indoor:.2f}', va='center', ha='center', backgroundcolor='white')
plt.text(0, median_indoor, f'Median={median_indoor:.2f}', va='center', ha='center', backgroundcolor='white', color='orange')
plt.text(0, q3_indoor, f'Q3={q3_indoor:.2f}', va='center', ha='center', backgroundcolor='white')

plt.text(1, q1_outdoor, f'Q1={q1_outdoor:.2f}', va='center', ha='center', backgroundcolor='white')
plt.text(1, median_outdoor, f'Median={median_outdoor:.2f}', va='center', ha='center', backgroundcolor='white', color='orange')
plt.text(1, q3_outdoor, f'Q3={q3_outdoor:.2f}', va='center', ha='center', backgroundcolor='white')

# Finalize the plot with adjusted layout
plt.title('Boxplot of SNR for Indoor and Outdoor Environments')
plt.ylabel('SNR (dB)')
plt.xlabel('Environment')
plt.tight_layout()  # Adjust the layout to make sure everything fits without overlapping

# Save the plot to a file
boxplot_path_with_quartiles = 'img/Both_indoor_outdoor.png'
plt.savefig(boxplot_path_with_quartiles)
plt.show()
