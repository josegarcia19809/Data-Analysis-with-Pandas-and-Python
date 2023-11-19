import pandas as pd
import matplotlib.pyplot as plt

serie_gastos = pd.read_csv("datax/gastos.csv", index_col="Días").squeeze()
print(serie_gastos)

# Grafica puntos unidos por una línea continua
x_values = serie_gastos.index
y_values = serie_gastos.values
fig = plt.figure()
plt.plot(x_values, y_values, label="Gastos")
plt.xlabel("Días de la semana")
plt.ylabel("Total de gastos")
plt.title("Gastos personales")

plt.xticks(x_values, x_values, rotation='vertical')
plt.legend()
plt.subplots_adjust(bottom=.4)
plt.show()
