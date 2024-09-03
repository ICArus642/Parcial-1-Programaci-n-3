from tabulate import tabulate
from API import modulo_api as API

def imprimir_datos(limite_registros, departamento):
    print(tabulate(API.extraccion(limite_registros, departamento), tablefmt = 'github', headers = ('NUMERO DEL REGISTRO', 'DEPARTAMENTO', 'CIUDAD', 'EDAD', 'TIPO', 'ESTADO')))
