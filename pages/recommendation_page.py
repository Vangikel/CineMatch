'''# Em uma página do Streamlit (ex: recommendation_page.py)
import streamlit as st
from neo4j_functions import create_user, create_movie, create_genre, add_movie_genre_relation, recommend_movies_based_on_genre

def recommendation_page():
    st.title("Recomendações Baseadas em Gêneros de Filmes")

    # Criar um usuário para exemplo
    if st.button("Adicionar Usuário"):
        create_user("user123", "Alice")
        st.write("Usuário Alice criado!")

    # Exibir recomendações
    if st.button("Recomendar Filmes"):
        recommendations = recommend_movies_based_on_genre("user123")
        st.write("Filmes recomendados para Alice:")
        for movie in recommendations:
            st.write(movie)

def run():
    st.title("Recomendações de Filmes")
    
    # Solicitando o ID do usuário para buscar recomendações personalizadas
    user_id = st.text_input("Digite o ID do Usuário para ver as recomendações:")
    
    if st.button("Obter Recomendações") and user_id:
        # Busca as recomendações usando a função get_recommendations
        recommendations = get_recommendations(user_id)
        
        if recommendations:
            st.subheader("Filmes recomendados para você:")
            for rec in recommendations:
                st.write(f"**Título:** {rec['titulo']}")
                st.write(f"**Gênero:** {rec['genero']}")
                st.write(f"**Ano:** {rec['ano']}")
                st.write("---")
        else:
            st.write("Nenhuma recomendação encontrada para este usuário.")'''
# recommendation_page.py
import streamlit as st
from neo4j_connection import neo4j_conn  # Conectando com o Neo4j

def get_recommendations(user_id):
    query = """
    MATCH (u:User {user_id: $user_id})-[:ASSISTIU]->(f:Filme)<-[:ASSISTIU]-(outro:User)-[:ASSISTIU]->(rec:Filme)
    WHERE NOT (u)-[:ASSISTIU]->(rec)
    RETURN rec.titulo AS titulo, rec.genero AS genero, rec.ano AS ano
    LIMIT 5
    """
    
    # Usando o método 'query' da classe Neo4jConnection
    result = neo4j_conn.query(query, parameters={"user_id": user_id})
    
    # Processando os resultados
    recommendations = [{"titulo": record["titulo"], "genero": record["genero"], "ano": record["ano"]} for record in result]
    
    return recommendations

def run():
    st.title("Recomendações de Filmes")
    
    user_id = st.text_input("Digite o ID do Usuário para ver as recomendações:")
    
    if st.button("Obter Recomendações") and user_id:
        recommendations = get_recommendations(user_id)
        
        if recommendations:
            st.subheader("Filmes recomendados para você:")
            for rec in recommendations:
                st.write(f"**Título:** {rec['titulo']}")
                st.write(f"**Gênero:** {rec['genero']}")
                st.write(f"**Ano:** {rec['ano']}")
                st.write("---")
        else:
            st.write("Nenhuma recomendação encontrada para este usuário.")
