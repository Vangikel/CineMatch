# neo4j_functions.py
from neo4j_connection import neo4j_conn

# Função para criar um usuário
def create_user(user_id, nome):
    query = """
    CREATE (u:User {id: $user_id, nome: $nome})
    """
    neo4j_conn.query(query, parameters={"user_id": user_id, "nome": nome})

# Função para criar um filme
def create_movie(movie_id, titulo, ano):
    query = """
    CREATE (m:Movie {id: $movie_id, titulo: $titulo, ano: $ano})
    """
    neo4j_conn.query(query, parameters={"movie_id": movie_id, "titulo": titulo, "ano": ano})

# Função para criar um gênero
def create_genre(nome):
    query = """
    CREATE (g:Genre {nome: $nome})
    """
    neo4j_conn.query(query, parameters={"nome": nome})

# Função para adicionar relacionamento "BELONGS_TO" entre filme e gênero
def add_movie_genre_relation(movie_id, genre_name):
    query = """
    MATCH (m:Movie {id: $movie_id}), (g:Genre {nome: $genre_name})
    CREATE (m)-[:BELONGS_TO]->(g)
    """
    neo4j_conn.query(query, parameters={"movie_id": movie_id, "genre_name": genre_name})

# Função para recomendar filmes do mesmo gênero favorito do usuário
def recommend_movies_based_on_genre(user_id):
    query = """
    MATCH (u:User {id: $user_id})-[:LIKES]->(g:Genre)<-[:BELONGS_TO]-(m:Movie)
    RETURN m.titulo AS recomendacao
    """
    results = neo4j_conn.query(query, parameters={"user_id": user_id})
    return [record["recomendacao"] for record in results]
