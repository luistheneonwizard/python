import pandas as pd
#crear un Dataframe
data = {'Nombre': ['Ana', 'Luis', 'Carlos', 'Maria', 'Juan', 'Camila'], 'Edad': [27, 22, 39, 46, 19, 21]}
df = pd.DataFrame(data)
# filtro = df[df['Edad'] > 30]
# print(filtro)
#print(df.head())
print(df.tail())
print(df.sample())