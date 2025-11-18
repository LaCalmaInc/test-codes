from colorama import Fore
import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://www.filmaffinity.com/cl/movie-group.php?group-id=40&chv=list&orderby=pos&p=1','https://www.filmaffinity.com/cl/movie-group.php?group-id=231&orderby=pos&chv=list','https://www.filmaffinity.com/cl/movie-group.php?group-id=5&p=1&orderby=pos&chv=list']

column_headers = ['Title','Author','Rating','Year','Awards','Users who rated']

title = ''
author = ''
rating = ''
year = ''
awards = ''
users_who_rated = ''

dataframe = pd.DataFrame(columns=column_headers)
numero_url = 1
for url in urls:
    print("Estamos en la url numero " + str(numero_url))
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html')
    lista = soup.find_all('ul', class_='movie-group-movies')

    etiqueta_autor = soup.find('h1',id='main-title')
    autor = etiqueta_autor.text.replace('Grupo: Adaptaciones de ','').strip()

    pager = soup.find('div',class_='pager')

    if pager:
        links_paginas = pager.find_all('a')
        arreglo_paginas = []
        for hrefs in links_paginas[:-1]:
            pagina = hrefs.get('href')
            arreglo_paginas.append(pagina)

    else:
        arreglo_paginas = []
    numero_url+=1
    
    loops = 0
    
    while loops < len(arreglo_paginas) + 1:
        for li in lista[0].find_all('li'):
            #obtener pagina de la obra para extraer premios
            a = li.find_all('a')[0]
            href = a.get('href')
            page2 = requests.get(href)
            soup2=BeautifulSoup(page2.text,'html')
            #-----------------------------------------------------------

            author = autor
            for nombre_obra in li.find_all('div', class_='mc-title'):#titulo
                title = nombre_obra.text.strip()
            for anio in li.find_all('span',class_='mc-year'):#año
                year = anio.text.strip()
            for rate in li.find_all('div',class_='avgrat-box'):#rating
                rating = rate.text.strip()
            for count in li.find_all('div',class_='ratcount-box'):#usuarios que calificaron
                users_who_rated = count.text.strip()
            #obtener premios de la obra
            
            premios = soup2.find_all('dd',class_='award')
            if premios:
                etiqueta_em = premios[0].find('em')
                a2 = etiqueta_em.find('a')
                href2 = a2.get('href')
                
                awards_page = requests.get(href2)
                soup3 = BeautifulSoup(awards_page.text, 'html')

                ul_premios = soup3.find('ul',class_= 'awards-list')

                lista_premios = []
                for li_premios in ul_premios.find_all('li'):
                    for ul_premio in li_premios.find_all('ul'):
                        for li_premio in ul_premio.find_all('li'):
                            premio = li_premio.find('a').text.strip()
                            lista_premios.append(premio)
                awards = lista_premios
                fila_temp = pd.Series([title, author, rating, year, awards, users_who_rated], index=column_headers)
                dataframe = pd.concat([dataframe, fila_temp.to_frame().T], ignore_index=True)

            else:
                awards = ""
                fila_temp = pd.Series([title, author, rating, year, awards, users_who_rated], index=column_headers)
                dataframe = pd.concat([dataframe, fila_temp.to_frame().T], ignore_index=True)  
        loops+=1
        if (len(arreglo_paginas) >= 1) and (loops <= len(arreglo_paginas)):
            page = requests.get(arreglo_paginas[loops - 1])
            soup = BeautifulSoup(page.text,'html')
            lista = soup.find_all('ul', class_='movie-group-movies')



dataframe
