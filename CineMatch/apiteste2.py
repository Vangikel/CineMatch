from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List

app = FastAPI()
client = MongoClient("mongodb+srv://ibituruna:b2b76kYJxKQ7ePiw@cinecluster.nrwz4.mongodb.net/")
db = client["cinecluster"]

# Coleções
usuarios_collection = db["usuarios"]
filmes_collection = db["filmes"]
avaliacoes_collection = db["avaliacoes"]
generos_collection = db["generos"]

# Modelos
class Usuario(BaseModel):
    nome: str
    email: str
    senha: str

class Filme(BaseModel):
    titulo: str
    genero: str
    ano: int

class Avaliacao(BaseModel):
    usuario_id: str
    filme_id: str
    nota: int

class Genero(BaseModel):
    nome: str

# Modelos de Resposta
class UsuarioResponse(BaseModel):
    id: str
    nome: str
    email: str

    @classmethod
    def from_mongo(cls, usuario):
        return cls(id=str(usuario["_id"]), nome=usuario["nome"], email=usuario["email"])

class FilmeResponse(BaseModel):
    id: str
    titulo: str
    genero: str
    ano: int

    @classmethod
    def from_mongo(cls, filme):
        return cls(id=str(filme["_id"]), titulo=filme["titulo"], genero=filme["genero"], ano=filme["ano"])

class GeneroResponse(BaseModel):
    id: str
    nome: str

    @classmethod
    def from_mongo(cls, genero):
        return cls(id=str(genero["_id"]), nome=genero["nome"])

# CRUD para Usuários
@app.post("/usuarios/", response_model=UsuarioResponse)
def criar_usuario(usuario: Usuario):
    result = usuarios_collection.insert_one(usuario.dict())
    return UsuarioResponse.from_mongo({"_id": result.inserted_id, **usuario.dict()})

@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def ler_usuario(usuario_id: str):
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        return UsuarioResponse.from_mongo(usuario)
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/usuarios/", response_model=List[UsuarioResponse])
def listar_usuarios():
    usuarios = list(usuarios_collection.find())
    return [UsuarioResponse.from_mongo(usuario) for usuario in usuarios]

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: str, usuario: Usuario):
    try:
        result = usuarios_collection.update_one(
            {"_id": ObjectId(usuario_id)},  # Converta para ObjectId
            {"$set": usuario.dict()}
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: str):
    result = usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"message": "Usuário deletado com sucesso"}

# CRUD para Filmes
@app.post("/filmes/", response_model=FilmeResponse)
def criar_filme(filme: Filme):
    result = filmes_collection.insert_one(filme.dict())
    return FilmeResponse.from_mongo({"_id": result.inserted_id, **filme.dict()})

@app.get("/filmes/{filme_id}", response_model=FilmeResponse)
def ler_filme(filme_id: str):
    filme = filmes_collection.find_one({"_id": ObjectId(filme_id)})
    if filme:
        return FilmeResponse.from_mongo(filme)
    raise HTTPException(status_code=404, detail="Filme não encontrado")

@app.get("/filmes/", response_model=List[FilmeResponse])
def listar_filmes():
    filmes = list(filmes_collection.find())
    return [FilmeResponse.from_mongo(filme) for filme in filmes]

@app.put("/filmes/{filme_id}", response_model=FilmeResponse)
def atualizar_filme(filme_id: str, filme: Filme):
    result = filmes_collection.update_one(
        {"_id": ObjectId(filme_id)},
        {"$set": filme.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    filme_atualizado = filmes_collection.find_one({"_id": ObjectId(filme_id)})
    return FilmeResponse.from_mongo(filme_atualizado)

@app.delete("/filmes/{filme_id}")
def deletar_filme(filme_id: str):
    result = filmes_collection.delete_one({"_id": ObjectId(filme_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return {"message": "Filme deletado com sucesso"}

# CRUD para Gêneros
@app.post("/generos/", response_model=GeneroResponse)
def criar_genero(genero: Genero):
    result = generos_collection.insert_one(genero.dict())
    return GeneroResponse.from_mongo({"_id": result.inserted_id, **genero.dict()})

@app.get("/generos/{genero_id}", response_model=GeneroResponse)
def ler_genero(genero_id: str):
    genero = generos_collection.find_one({"_id": ObjectId(genero_id)})
    if genero:
        return GeneroResponse.from_mongo(genero)
    raise HTTPException(status_code=404, detail="Gênero não encontrado")

@app.get("/generos/", response_model=List[GeneroResponse])
def listar_generos():
    generos = list(generos_collection.find())
    return [GeneroResponse.from_mongo(genero) for genero in generos]

@app.put("/generos/{genero_id}", response_model=GeneroResponse)
def atualizar_genero(genero_id: str, genero: Genero):
    result = generos_collection.update_one(
        {"_id": ObjectId(genero_id)},
        {"$set": genero.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Gênero não encontrado")
    genero_atualizado = generos_collection.find_one({"_id": ObjectId(genero_id)})
    return GeneroResponse.from_mongo(genero_atualizado)

@app.delete("/generos/{genero_id}")
def deletar_genero(genero_id: str):
    result = generos_collection.delete_one({"_id": ObjectId(genero_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Gênero não encontrado")
    return {"message": "Gênero deletado com sucesso"}

# CRUD para Avaliações
@app.post("/avaliacoes/")
def criar_avaliacao(avaliacao: Avaliacao):
    result = avaliacoes_collection.insert_one(avaliacao.dict())
    return {"avaliacao_id": str(result.inserted_id)}

@app.get("/avaliacoes/")
def listar_avaliacoes():
    try:
        avaliacoes = []
        for avaliacao in avaliacoes_collection.find():
            avaliacao['_id'] = str(avaliacao['_id'])  # Converte ObjectId para string
            avaliacoes.append(avaliacao)
        return avaliacoes
    except Exception as e:
        print("Erro:", e)  # Para debug
        raise HTTPException(status_code=500, detail=str(e))

       
@app.put("/avaliacoes/{avaliacao_id}")
def atualizar_avaliacao(avaliacao_id: str, avaliacao: Avaliacao):
    result = avaliacoes_collection.update_one(
        {"_id": ObjectId(avaliacao_id)},
        {"$set": avaliacao.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"message": "Avaliação atualizada com sucesso"}

@app.delete("/avaliacoes/{avaliacao_id}")
def deletar_avaliacao(avaliacao_id: str):
    result = avaliacoes_collection.delete_one({"_id": ObjectId(avaliacao_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return {"message": "Avaliação deletada com sucesso"}

# Exemplo de Aggregation Pipeline para Recomendações
@app.get("/recomendacoes/{usuario_id}")
def recomendacoes(usuario_id: str):
    pipeline = [
        {
            "$match": {
                "usuario_id": usuario_id
            }
        },
        {
            "$lookup": {
                "from": "filmes",
                "localField": "filme_id",
                "foreignField": "_id",
                "as": "filme_info"
            }
        },
        {
            "$unwind": "$filme_info"
        },
        {
            "$group": {
                "_id": "$filme_info.genero",
                "filmes": {"$push": "$filme_info.titulo"}
            }
        }
    ]
    resultado = list(avaliacoes_collection.aggregate(pipeline))
    return resultado
