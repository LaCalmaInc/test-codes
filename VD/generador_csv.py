import pandas as pd
import numpy as np

# Definir el tamaño del conjunto de datos
num_rows = 1000  # Número de filas
anios = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]
num_columns = 10

# Data de premios de seguridad
data = [["honda","honda","honda","honda","mazda","mazda","mazda","mazda","toyota","toyota","toyota","toyota","toyota","","","","","","","","",""],#2015
        ["toyota","toyota","toyota","toyota","toyota","toyota","honda","honda","honda","honda","honda","honda","mazda","mazda","mazda","mazda","mazda","","","","",""],#2016
        ["toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota","honda","honda","honda","honda","honda","mazda","mazda","mazda","mazda","mazda","mazda","",""],#2017
        ["honda","honda","mazda","toyota","toyota","mazda","","","","","","","","","","","","","","","",""],#2018
        ["honda","mazda","mazda","mazda","toyota","toyota","toyota","mazda","","","","","","","","","","","","","",""],#2019
        ["honda","honda","honda","mazda","mazda","mazda","mazda","mazda","mazda","mazda","toyota","toyota","toyota","","","","","","","","",""],#2020
        ["honda","honda","honda","honda","honda","mazda","mazda","mazda","mazda","mazda","mazda","mazda","toyota","toyota","toyota","","","","","","",""],#2021
        ["honda","honda","honda","honda","honda","honda","mazda","mazda","mazda","mazda","mazda","mazda","toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota"],#2022
        ["honda","honda","honda","honda","honda","mazda","mazda","mazda","mazda","mazda","toyota","toyota","toyota","toyota","toyota","toyota","toyota","toyota","","","",""],#2023
        ["honda","honda","mazda","mazda","mazda","mazda","mazda","toyota","","","","","","","","","","","","","",""]]#2024
#Data de finalistas WCOTY
data2 = [["","",""],#2005
         ["mazda","honda",""],#2006
         ["","",""],#2007
         ["mazda","",""],#2008
         ["toyota","honda","mazda"],#2009
         ["toyota","mazda",""],#2010
         ["","",""],#2011
         ["","",""],#2012
         ["toyota","mazda","mazda"],#2013
         ["mazda","",""],#2014
         ["mazda","",""],#2015
         ["mazda","toyota","mazda"],#2016
         ["toyota","honda","mazda"],#2017
         ["toyota","mazda",""],#2018
         ["","",""],#2019
         ["mazda","mazda",""],#2020
         ["honda","toyota","mazda"],#2021
         ["honda","toyota",""],#2022
         ["honda","mazda",""],#2023
         ["mazda","toyota",""]#2024
         ]

# Crear un DataFrame de pandas con los datos aleatorios
transposed_data = np.transpose(data)
transposed_data2 = np.transpose(data2)
df = pd.DataFrame(transposed_data2, columns = anios)

# Guardar el DataFrame como un archivo CSV
df.to_csv("datos_generados2.csv", index=False)

print("Datos generados y guardados en 'datos_generados.csv'")
