import pandas as pd

df = pd.read_csv("poblacion.csv")

#filtro = df[df['Date'] > 2010]
#print(filtro[["COL", "ARG"]])

# print(df["COL"])
# df.at[0, "COL"] = 5000000
# print(df["COL"])

df = pd.read_csv("poblacion.csv")
print(df)
df = df.drop("ABW", axis=1)
print(df)
df.to_csv("salida.csv", index=False)

# print(df.head())
# print(df.describe())
# print(df.tail())
# print(df.sample(10))
