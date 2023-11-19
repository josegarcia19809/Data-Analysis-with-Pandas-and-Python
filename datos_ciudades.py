import pandas as pd
import numpy as np

city_data = {
    "City": ["New York City", "Paris", "Barcelona", "Rome"],
    "Country": ["United States", "France", "Spain", "Italy"],
    "Population": [8600000, 2141000, 5515000, 2873000]
}

cities = pd.DataFrame(city_data)
print(cities)
print("-" * 100)
# Mostrar el contenido de un renglón
print(cities.loc[0])
