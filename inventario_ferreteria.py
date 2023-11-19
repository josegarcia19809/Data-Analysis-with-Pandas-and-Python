import pandas as pd


def imprimir_linea():
    print("-" * 100)


df_inventario = pd.read_csv("datax/inventario_ferreteria.csv")
print(df_inventario)

imprimir_linea()
df_inventario["Cantidad"] = [12, 15, 20, 30, 50]
print(df_inventario)

imprimir_linea()
df_inventario.insert(2, "Descuento", [8, 5, 10, 12, 5])
print(df_inventario)