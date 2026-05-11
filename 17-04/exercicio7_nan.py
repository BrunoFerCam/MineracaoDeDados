import pandas as pd
import numpy as np

df = pd.DataFrame({
    "idade": [20, np.nan, 35, np.nan]
})

df["flag_omissao"] = df["idade"].isna().astype(int)

df["idade"] = df["idade"].fillna(df["idade"].mean())

print(df)