import pandas as pd
df = pd.read_csv(r"C:\Users\regina.alvarenga\Downloads\funcionarios.csv")



df["liquido"] = df["lucro"] - df["salario"]

print(df)
"\n"

df["nome"] = df["nome"].str.upper()

print(df)
"\n"
df["Lucro positivo"] = df["liquido"].apply(lambda x: "Lucro positivo" if x > 0 else "Lucro negativo")
print(df)
"\n"

df = df.rename(columns={"liquido": "Lucro liquido", "Lucro positivo" : "Lucro final"})
print(df)
"\n"

df["Salario_maior_5000"] = df["salario"].apply(lambda x: "possui" if x > 5000  else "não possui" )

df = df.rename(columns={"ativos": "empregado"})
print(df)
"\n"

df = df[df["ativo"] == True]     
print(df)  