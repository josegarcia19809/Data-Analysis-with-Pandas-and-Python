import pandas as pd
import matplotlib.pyplot as plt
# Gráfica puntos unidos por una línea continua
serie_asistencias = pd.read_csv("datax/asistencias2.csv", index_col="Clase").squeeze()
print(serie_asistencias)

x_values = serie_asistencias.index
y_values = serie_asistencias.values
fig = plt.figure()
plt.plot(x_values, y_values, label="Asistencias")
plt.xlabel("Fecha de clases")
plt.ylabel("Cantidad de alumnos")
plt.title("Alumnos que asistieron a clases")
plt.xticks(x_values, x_values, rotation='vertical')
plt.legend()
plt.subplots_adjust(bottom=.4)
plt.show()
