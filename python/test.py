import pandas as pd

columnas = ['Titulo', 'Autor', 'Año']

diccionario = {
    'Titulo': ['Cien Años de Soledad', 'Don Quijote de la Mancha', 'La Odisea'],
    'Autor': ['Gabriel García Márquez', 'Miguel de Cervantes', 'Homero'],
    'Año': [1967, 1605, -800]
    }

df = pd.DataFrame(diccionario, columns=columnas)
print(df)