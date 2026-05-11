import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": [np.nan, 5, 6],
    "C": [7, 8, np.nan]
})

sns.heatmap(df.isnull(), cbar=False)

plt.title("Mapa de Calor de Valores NaN")

plt.show()