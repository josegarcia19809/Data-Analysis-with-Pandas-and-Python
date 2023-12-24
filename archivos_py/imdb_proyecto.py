import pandas as pd


def imprimir_linea():
    print("-" * 100)


df_imdb = pd.read_csv("../datax/imdb.csv")
print(df_imdb)
imprimir_linea()
print(df_imdb.head())
imprimir_linea()
print(df_imdb.info())
imprimir_linea()

# Seleccionar la columna año
anio_lanzamiento = df_imdb["año"]
print(anio_lanzamiento)
imprimir_linea()
# Seleccionar la columna nombre
nombre = df_imdb.nombre
print(nombre)
imprimir_linea()

# Seleccionar la columna nombre y año de lanzamiento
nombre_y_anio_lanzamiento = df_imdb[["nombre", "año"]]
print(nombre_y_anio_lanzamiento)
imprimir_linea()

# Seleccionar el renglón que tiene el índice 2
avengers = df_imdb.iloc[2]
print(avengers)
imprimir_linea()

# Seleccionar los renglones que van desde el índice 3 hasta la 7
varias_peliculas = df_imdb.iloc[3:8]
print(varias_peliculas)
imprimir_linea()

# Seleccionar los renglones que van desde el índice 0 hasta la 4
varias_peliculas = df_imdb.iloc[:5]
print(varias_peliculas)
imprimir_linea()

# Seleccionar los últimos 3 renglones
varias_peliculas = df_imdb.iloc[-3:]
print(varias_peliculas)
imprimir_linea()

# Seleccionar los renglones que van desde el índice 0 hasta el 9, de 3 en 3
varias_peliculas = df_imdb.iloc[0:10:3]
print(varias_peliculas)
imprimir_linea()

# Seleccionar los renglones cuyo genero sea de horror
pd.options.display.max_columns = None
peliculas_horror = df_imdb[df_imdb["genero"] == "horror"]
print(peliculas_horror)
imprimir_linea()

# Seleccionar los renglones cuyo año sea mayor que 2013
pd.options.display.max_columns = None
peliculas_despues_2013 = df_imdb[df_imdb["año"] > 2013]
print(peliculas_despues_2013)
imprimir_linea()

# Seleccionar los renglones cuyo género no sea de romance
pd.options.display.max_columns = None
peliculas_no_romance = df_imdb[df_imdb["genero"] != "romance"]
print(peliculas_no_romance)
imprimir_linea()

# Seleccionar los renglones cuyo género sea de comedia o que hayan salido después de 2014
peliculas_comedia_o_despues_2014 = df_imdb[(df_imdb["genero"] == "comedy") | (df_imdb["año"] > 2014)]
print(peliculas_comedia_o_despues_2014)
imprimir_linea()

# Seleccionar los renglones cuyo género sea de comedia o que hayan salido después de 2014
condicion_comedia = df_imdb["genero"] == "comedy"
condicion_despues_2104 = df_imdb["año"] > 2014
condicion_comedia_despues_2104 = (condicion_comedia) | (condicion_despues_2104)
peliculas_comedia_o_despues_2014 = df_imdb[condicion_comedia_despues_2104]
columnas = ["nombre", "genero", "año"]
print(peliculas_comedia_o_despues_2014[columnas])
imprimir_linea()

# Seleccionar los renglones cuyo género sea de drama y que hayan salido después de 2013
peliculas_drama_despues_2013 = df_imdb[(df_imdb["genero"] == "drama") & (df_imdb["año"] > 2013)]
print(peliculas_drama_despues_2013)
imprimir_linea()

# Seleccionar determinadas películas
mi_seleccion = df_imdb[df_imdb["nombre"].isin(["Star Wars", "Dark Shadows", "Blade"])]
print(mi_seleccion)
imprimir_linea()

# Resetear los índices
mi_seleccion = mi_seleccion.reset_index(drop=True)
print(mi_seleccion)
imprimir_linea()
