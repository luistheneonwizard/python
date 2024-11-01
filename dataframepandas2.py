import pandas as pd

df = pd.read_csv("poblacion.csv")

#filtro = df[df['Date'] > 2010]
#print(filtro[["COL", "ARG"]])
print(df["COL"])
df.at[0, "COL"] = 5000000
print(df["COL"])
# print(df.head())
# print(df.describe())
# print(df.tail())
# print(df.sample(10))
