# pages/generos.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/generos"  # URL da sua API

def criar_genero():
    st.subheader("Criar Gênero")
    nome = st.text_input("Nome do Gênero:")
    if st.button("Criar Gênero"):
        response = requests.post(API_URL, json={"nome": nome})
        if response.status_code == 201 or 200:
            st.success("Gênero criado com sucesso!")
        else:
            st.error("Erro ao criar gênero.")


def listar_generos():
    st.subheader("Listar Gêneros")
    response = requests.get(API_URL)
    if response.status_code == 200:
        generos = response.json()
        if generos:  # Verifica se a lista não está vazia
            for genero in generos:
                st.write(f"ID: {genero.get('id', 'ID não encontrado')} | Nome: {genero.get('nome', 'Nome não encontrado')}")
        else:
            st.write("Nenhum gênero encontrado.")
    else:
        st.error("Erro ao listar gêneros.")

def atualizar_genero():
    st.subheader("Atualizar Gênero")
    genero_id = st.text_input("ID do Gênero:")
    novo_nome = st.text_input("Novo Nome:")
    if st.button("Atualizar Gênero"):
        response = requests.put(f"{API_URL}/{genero_id}", json={"nome": novo_nome})
        if response.status_code == 200:
            st.success("Gênero atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar gênero.")

def deletar_genero():
    st.subheader("Deletar Gênero")
    genero_id = st.text_input("ID do Gênero para deletar:")
    if st.button("Deletar Gênero"):
        response = requests.delete(f"{API_URL}/{genero_id}")
        if response.status_code == 204 or 200:
            st.success("Gênero deletado com sucesso!")
        else:
            st.error("Erro ao deletar gênero.")

def run():
    st.title("CRUD de Gêneros")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Criar", "Listar", "Atualizar", "Deletar"])

    if menu == "Criar":
        criar_genero()
    elif menu == "Listar":
        listar_generos()
    elif menu == "Atualizar":
        atualizar_genero()
    elif menu == "Deletar":
        deletar_genero()
