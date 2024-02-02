import pandas as pd
import time
from bancosito import extraccion
tb = pd.read_csv('tabla_del_banco.csv')
tb.columns = ['Países', 'Equivalencia a un peso mexicano']

moneda = ''
pesos = 0
valor = 0

def lista_de_opciones():
    number = ''
    print('Listado de países:')
    print(tb['Países'])
    number = input('Escribe el numero del países que quieras: ')
    while True:
        if number.isnumeric() == True:
            if int(number) > 0 and int(number) < 33:
                return number
                break
            else:
                print('Escribe un numero válido por favor')
                time.sleep(1)
                print()
                number = input('Escribe el numero del países que quieras: ')
        else:
            print('Escribe un numero válido por favor')
            time.sleep(1)
            print()
            number = input('Escribe el numero del países que quieras: ')

def definir_pesos():
    number = input('Escribe la equivalencia en pesos mexicanos: ')
    while True:
        if number.isnumeric() == True:
            return number
            break
        else:
            print('Escribe un numero válido por favor')
            time.sleep(1)
            print()
            number = input('Escribe la equivalencia en pesos mexicanos: ')
    


moneda_num = lista_de_opciones()
time.sleep(1)
pesos = int(definir_pesos())

mon, num = extraccion()

moneda = mon[int(moneda_num)]
valor = num[int(moneda_num)]

print(moneda)

def equivalencia(valor, pesos):
    time.sleep(3)
    equivalencia = int(pesos) * float(valor)
    return equivalencia

equi = equivalencia(valor, pesos)
print(pesos, 'pesos mexicanos equivale ha', equi, 'en', moneda)


