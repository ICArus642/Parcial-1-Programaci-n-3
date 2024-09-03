from sodapy import Socrata
import pandas as pd

def extraccion(limite_registros, nombre_departamento):
    
    # Crear una instancia del cliente Socrata para conectar con la API pública de datos.gov.co
    client = Socrata("www.datos.gov.co", None)
    
    # Identificador del dataset en la plataforma de datos.gov.co
    dataset_identifier = "gt2j-8ykr"
    
    # Realizar la consulta al dataset
    # Filtra los registros donde el nombre del departamento coincide con el nombre proporcionado
    # Limita la cantidad de registros retornados a 'limite_registros'
    results = client.get(dataset_identifier, where=f"departamento_nom='{nombre_departamento}'", limit=limite_registros)
    
    # Verificar si se obtuvieron resultados
    if results:
        # Convertir los resultados a un DataFrame de pandas
        results_df = pd.DataFrame.from_records(results)
        
        # Seleccionar un subconjunto de columnas de interés
        subset = results_df[['departamento_nom', 'ciudad_municipio_nom', 'edad', 'fuente_tipo_contagio', 'estado']]
        
        # Retornar el DataFrame con el subconjunto de datos
        return subset
    else:
        # Imprimir un mensaje si no se encontraron datos para el departamento especificado
        print("No se encontraron datos para el departamento especificado.")
        return None
