import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

URL = 'https://www.expansion.com/ahorro/conversor-divisas/cambio_pesomexicano'

barco = webdriver.Firefox()
barco.get(URL)

time.sleep(10)

titulo_de_monedas = []
info_de_monedas = []

def excabar():
    sopa = BeautifulSoup(barco.page_source, "html.parser")

    for all_trs in sopa.find_all('tr'):
        
        all_tds = all_trs.find_all('td')
        if len(all_tds) > 1:
            info_de_monedas.append(all_tds[2])
            titulo_de_monedas.append(all_tds[0])
        else:
            continue

excabar() 

def extraccion():
    titulos_array = []
    infos_array = []
    for titulos in titulo_de_monedas:
        title = str(titulos)
        titlie1 = title.split('>')[3]
        titlie2 = titlie1.replace('</strong', '')
        titulos_array.append(titlie2.capitalize())
    for infos in info_de_monedas:
        info = str(infos)
        info1 = info.replace('<td>', '')
        info2 = info1.replace('</td>', '')
        infos_array.append(float(info2))
        
    return titulos_array, infos_array

#print(info_de_monedas)

todos_los_nombres,todos_los_valores = extraccion()
#print(todos_los_nombres)
#print(todos_los_valores)

#def mach_arrays(nombres, valores):
 #   valores_y_nombres = []
  #  for nombre in nombres:
   #     for valor in valores:
    #        vn = [nombre, valor]
     #       valores_y_nombres.extend(vn)
    #return valores_y_nombres


#valores_y_nombres = mach_arrays(todos_los_nombres, todos_los_valores)

csv_tabla = pd.DataFrame(todos_los_valores, todos_los_nombres)
csv_tabla.to_csv('tabla_del_banco.csv', index= True, index_label= 'id')


