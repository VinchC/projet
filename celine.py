import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(
    "data\ZonAnn.Ts+dSST.csv",
    skiprows=1
)
df.columns = [
    "Year", "Global", "NH", "SH",
    "24N_90N", "24S_24N", "90S_24S",
    "64N_90N", "44N_64N", "24N_44N",
    "EQU_24N", "24S_EQU", "44S_24S",
    "64S_44S", "90S_64S"
]
df.info()
df.head()
df.describe()
df["Year"] = pd.to_datetime(df["Year"], format="%Y")

for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

