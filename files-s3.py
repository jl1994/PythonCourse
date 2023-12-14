import pymongo
import boto3
from tqdm import tqdm
import time
from concurrent.futures import ThreadPoolExecutor

# Conectar a MongoDB
cliente = pymongo.MongoClient(
    "mongodb+srv://Finkargo:6x3CBY9YrKLthJiI@finkargo-co-drp.lmf5b.mongodb.net/"
)
db = cliente["finkargo-documents"]
coleccion = db["file"]

# Define los nombres de los buckets
bucket_origen = 'docmanagement.finkargo.production'
bucket_destino = 'fk-drp-docmanagement-prod'

# Configura la sesión de AWS para utilizar el perfil aws-co
perfil_origen = 'aws-co'
s3_origen_session = boto3.Session(profile_name=perfil_origen, region_name="us-east-1")
s3_origen = s3_origen_session.client('s3')

# Configura la sesión de AWS para utilizar el perfil aws-co
perfil_destino = 'aws-co'
s3_destino_session = boto3.Session(profile_name=perfil_destino, region_name="us-west-2")
s3_destino = s3_destino_session.client('s3')


def process_document(row):
    try:
        path = f"{row['company']}/{row['creditrequest']}/{row['operation']}/{row['module']}/{row['name']}:{row['_id']}.pdf"

        for metadata in row['response_metadata']:
            version_id_old = metadata['VersionId']
            version_id_new = copy_s3_documents(path, version_id_old)
            update_mongo_metadata(row['_id'], metadata, version_id_new)
            update_mongo_version_id(row['_id'], version_id_old, version_id_new)
            print(f"Documento {row['_id']} modificado")
    except Exception as e:
        pass
    pbar.update(1)


def update_mongo_version_id(id_file, version_id_old, version_id_new):
    # Filtra el documento que deseas actualizar basado en el campo "version_id"
    filtro = {
        "_id": id_file,
        "version_id": version_id_old
    }

    # Define la actualización que quieres realizar
    actualizacion = {
        "$set": {
            "version_id": version_id_new
        }
    }

    # Realiza la actualización
    resultado = coleccion.update_one(filtro, actualizacion)

    if resultado.modified_count == 0:
        print("No se modifico version_id.")
    else:
        print(
            f"Documento version_id: {resultado.modified_count} modificado")


def update_mongo_metadata(id_file, metadata, version_id_new):
    # Filtra el documento que deseas actualizar basado en el campo "RequestId"
    filtro = {
        "_id": id_file,
        "response_metadata": {
            "$elemMatch": {
                "RequestId": metadata["RequestId"]
            }
        }
    }

    # Define la actualización que quieres realizar
    actualizacion = {
        "$set": {
            "response_metadata.$.VersionId": version_id_new
        }
    }

    # Realiza la actualización
    resultado = coleccion.update_one(filtro, actualizacion)

    if resultado.modified_count == 0:
        print("No se modifico metadata.")
    else:
        print(
            f"Documento metadata: {resultado.modified_count} modificado")


def copy_s3_documents(objeto_key, version_id_old):
    # Copia cada versión al bucket de destino
    response_destino = s3_destino.copy_object(
        CopySource={'Bucket': bucket_origen,
                    'Key': objeto_key, 'VersionId': version_id_old},
        Bucket=bucket_destino,
        Key=objeto_key,
        Metadata={'VersionId': version_id_old},
        MetadataDirective='REPLACE'
    )
    return response_destino["VersionId"]


# Realizar una consulta a documentos de MX
query = {
    'alpha2': 'CO',
    'version_id': {'$exists': True}
}

# Iterar a través de los resultados con una barra de carga
resultados = coleccion.find(query)
resultados = list(resultados)  # Convierte el cursor en una lista para conocer su longitud
tiempo_inicial = time.time()

# Configurar la barra de carga
pbar = tqdm(total=len(resultados), desc="Procesando documentos")


# Utilizar ThreadPoolExecutor para procesar documentos en hilos
with ThreadPoolExecutor(max_workers=100) as executor:  # Ajusta el número de hilos según tus necesidades
    for row in resultados:
        executor.submit(process_document, row)

# Finalizar la barra de carga
pbar.close()

# Calcular el tiempo de ejecución
tiempo_final = time.time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(f"Tiempo de ejecución: {tiempo_ejecucion:.2f} segundos")