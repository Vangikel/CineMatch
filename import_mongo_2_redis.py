from fastapi import FastAPI
from pymongo import MongoClient
from redis import Redis
import json
from bson import ObjectId

app = FastAPI()

# Conexão com MongoDB
client = MongoClient("mongodb+srv://ibituruna:b2b76kYJxKQ7ePiw@cinecluster.nrwz4.mongodb.net/")
db = client["cinecluster"]

# Conexão com Redis
redis = Redis.from_url("redis://default:VOSH6t7r4AJ3tRMSY9LkSS2CW389Vw2I@redis-15202.c308.sa-east-1-1.ec2.redns.redis-cloud.com:15202")

# Função para converter ObjectId para string
def convert_object_id(data):
    if isinstance(data, ObjectId):
        return str(data)
    if isinstance(data, dict):
        return {key: convert_object_id(value) for key, value in data.items()}
    if isinstance(data, list):
        return [convert_object_id(element) for element in data]
    return data

# Função para importar todas as coleções para o Redis
@app.post("/importar_tudo_para_redis")
async def importar_tudo_para_redis():
    try:
        # Itera sobre todas as coleções do banco de dados MongoDB
        for collection_name in db.list_collection_names():
            collection = db[collection_name]
            documentos = list(collection.find())

            for documento in documentos:
                doc_id = str(documento["_id"])  # ID do documento
                documento_data = convert_object_id(documento)  # Converte ObjectId para string

                # Armazena o documento no Redis com uma chave que indica a coleção e o ID
                redis.set(f"{collection_name}:{doc_id}", json.dumps(documento_data))

        return {"message": "Todos os documentos foram importados para o Redis com sucesso!"}
    except Exception as e:
        return {"error": str(e)}
