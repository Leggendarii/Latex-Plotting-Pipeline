import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)

df = pd.DataFrame({
    "x": x,
    "sin": np.sin(x),
    "cos": np.cos(x)
})

df.to_csv("data/data.csv", index=False)
print("Dati generati in data/data.csv")
