# pages/filmes.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/filmes"  # URL da sua API

def criar_filme():
    st.subheader("Criar Filme")
    titulo = st.text_input("Título:")
    genero = st.text_input("Gênero:")
    ano = st.number_input("Ano:", min_value=1900, max_value=2100)
    if st.button("Criar Filme"):
        response = requests.post(API_URL, json={"titulo": titulo, "genero": genero, "ano": ano})
        if response.status_code == 201 or 200:
            st.success("Filme criado com sucesso!")
        else:
            st.error("Erro ao criar filme.")
            
def listar_filmes():
    st.subheader("Listar Filmes")
    response = requests.get(API_URL)
    if response.status_code == 200:
        filmes = response.json()
        if filmes:  # Verifica se a lista não está vazia
            for filme in filmes:
                st.write(f"ID: {filme.get('id', 'ID não encontrado')} | Título: {filme.get('titulo', 'Título não encontrado')} | Gênero: {filme.get('genero', 'Gênero não encontrado')}")
        else:
            st.write("Nenhum filme encontrado.")
    else:
        st.error("Erro ao listar filmes.")

def run():
    st.title("CRUD de Filmes")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Listar"])

    if menu == "Listar":
        listar_filmes()

def atualizar_filme():
    st.subheader("Atualizar Filme")
    filme_id = st.text_input("ID do Filme:")
    novo_titulo = st.text_input("Novo Título:")
    novo_genero = st.text_input("Novo Gênero:")
    novo_ano = st.number_input("Novo Ano:", min_value=1900, max_value=2100)
    if st.button("Atualizar Filme"):
        response = requests.put(f"{API_URL}/{filme_id}", json={"titulo": novo_titulo, "genero": novo_genero, "ano": novo_ano})
        if response.status_code == 200:
            st.success("Filme atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar filme.")

def deletar_filme():
    st.subheader("Deletar Filme")
    filme_id = st.text_input("ID do Filme para deletar:")
    if st.button("Deletar Filme"):
        response = requests.delete(f"{API_URL}/{filme_id}")
        if response.status_code == 204 or 200:
            st.success("Filme deletado com sucesso!")
        else:
            st.error("Erro ao deletar filme.")

def run():
    st.title("CRUD de Filmes")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Criar", "Listar", "Atualizar", "Deletar"])

    if menu == "Criar":
        criar_filme()
    elif menu == "Listar":
        listar_filmes()
    elif menu == "Atualizar":
        atualizar_filme()
    elif menu == "Deletar":
        deletar_filme()
