import pandas as pd


def imprimir_linea():
    print("-" * 100)


df_trabajadores = pd.read_csv("datax/trabajadores_edades.csv")
print(df_trabajadores)
imprimir_linea()

# Renombrar todas las columnas
df_trabajadores.columns = ["Nombre", "Edad"]
print(df_trabajadores)
imprimir_linea()

# Renombrar columnas de forma individual
df_trabajadores.rename(columns={
    "Nombre": "Primer nombre"
}, inplace=True)
print(df_trabajadores)
imprimir_linea()

# Borrar una columna
df_trabajadores.drop("Edad", axis=1, inplace=True)
print(df_trabajadores)
imprimir_linea()

# Borrar varias columnas
# df_trabajadores.drop(["Nombre", "Edad"], axis=1, inplace=True)
