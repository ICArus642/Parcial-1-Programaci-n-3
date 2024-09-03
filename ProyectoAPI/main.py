from UI import modulo_ui as UI

# Lista de departamentos de Colombia 
departamentos_colombia = [
    "ATLANTICO",
    "BOGOTA",
    "BOLIVAR",
    "BOYACA",
    "CALDAS",
    "CAQUETA",
    "CASANARE",
    "CAUCA",
    "CESAR",
    "CHOCO",
    "CORDOBA",
    "CUNDINAMARCA",
    "GUAINIA",
    "GUAVIARE",
    "HUILA",
    "LA GUAJIRA",
    "MAGDALENA",
    "META",
    "NARIÑO",
    "NORTE SANTANDER",
    "PUTUMAYO",
    "QUINDIO",
    "RISARALDA",
    "SAN ANDRES",
    "SANTANDER",
    "SUCRE",
    "TOLIMA",
    "VALLE DEL CAUCA",
    "VICHADA"   
]

while True:
    nombre_departamento = input("Ingrese el nombre del departamento del que desea extraer los datos: ")
    nombre_departamento = nombre_departamento.upper()

    if nombre_departamento in departamentos_colombia:
        break
    else:
        print("El departamento ingresado no es válido. Intente de nuevo.")

while True:
    limite_registros = int(input("Ingrese el número de registros que desea extraer: "))
    
    if limite_registros < 0 or limite_registros > 1000:
        print("El número de registros ingresado no es válido. Intente de nuevo.")
        
    else: 
        break;
    
UI.imprimir_datos(limite_registros, nombre_departamento)