import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Supongamos que tienes tres conjuntos de datos
data1 = pd.Series(np.random.randn(1000))
data2 = pd.Series(np.random.randn(1000) * 2)
data3 = pd.Series(np.random.randn(1000) + 3)

fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)
sns.histplot(data1, color="blue", kde=True, ax=axs[0])
sns.histplot(data2, color="red", kde=True, ax=axs[1])
sns.histplot(data3, color="green", kde=True, ax=axs[2])

axs[0].set_title('Data Set 1')
axs[1].set_title('Data Set 2')
axs[2].set_title('Data Set 3')

plt.tight_layout()
plt.show()
