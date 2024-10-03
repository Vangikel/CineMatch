# pages/avaliacoes.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/avaliacoes"  # URL da sua API

def criar_avaliacao():
    st.subheader("Criar Avaliação")
    usuario_id = st.text_input("ID do Usuário:")
    filme_id = st.text_input("ID do Filme:")
    nota = st.number_input("Nota (1 a 10):", min_value=1, max_value=10)
    if st.button("Criar Avaliação"):
        response = requests.post(API_URL, json={"usuario_id": usuario_id, "filme_id": filme_id, "nota": nota})
        if response.status_code == 201 or 200:
            st.success("Avaliação criada com sucesso!")
        else:
            st.error("Erro ao criar avaliação.")

'''def listar_avaliacoes():
    st.subheader("Listar Avaliações")
    response = requests.get(API_URL)
    if response.status_code == 200:
        avaliacoes = response.json()
        for avaliacao in avaliacoes:
            st.write(f"ID: {avaliacao['avaliacao_id']} | Usuário ID: {avaliacao['usuario_id']} | Filme ID: {avaliacao['filme_id']} | Nota: {avaliacao['nota']}")
'''
def listar_avaliacoes():
    st.subheader("Listar Avaliações")
    response = requests.get(API_URL)
    
    # Adicionando diagnósticos
    if response.status_code == 200:
        avaliacoes = response.json()
        if avaliacoes:  # Verifica se a lista não está vazia
            for avaliacao in avaliacoes:
                # Extraindo o ID corretamente
                avaliacao_id = avaliacao["_id"]["$oid"] if "_id" in avaliacao and "$oid" in avaliacao["_id"] else "ID não encontrado"
                usuario_id = avaliacao.get("usuario_id", "Usuário ID não encontrado")
                filme_id = avaliacao.get("filme_id", "Filme ID não encontrado")
                nota = avaliacao.get("nota", "Nota não encontrada")
                
                st.write(f"ID: {avaliacao_id} | Usuário ID: {usuario_id} | Filme ID: {filme_id} | Nota: {nota}")
        else:
            st.write("Nenhuma avaliação encontrada.")
    else:
        # Imprimindo informações adicionais para diagnóstico
        st.error(f"Erro ao listar avaliações. Status Code: {response.status_code}")
        st.write("Conteúdo da resposta:", response.text)
def atualizar_avaliacao():
    st.subheader("Atualizar Avaliação")
    avaliacao_id = st.text_input("ID da Avaliação:")
    nova_nota = st.number_input("Nova Nota (1 a 10):", min_value=1, max_value=10)
    if st.button("Atualizar Avaliação"):
        response = requests.put(f"{API_URL}/{avaliacao_id}", json={"nota": nova_nota})
        if response.status_code == 200:
            st.success("Avaliação atualizada com sucesso!")
        else:
            st.error("Erro ao atualizar avaliação.")

def deletar_avaliacao():
    st.subheader("Deletar Avaliação")
    avaliacao_id = st.text_input("ID da Avaliação para deletar:")
    if st.button("Deletar Avaliação"):
        response = requests.delete(f"{API_URL}/{avaliacao_id}")
        if response.status_code == 204:
            st.success("Avaliação deletada com sucesso!")
        else:
            st.error("Erro ao deletar avaliação.")

def run():
    st.title("CRUD de Avaliações")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Criar", "Listar", "Atualizar", "Deletar"])

    if menu == "Criar":
        criar_avaliacao()
    elif menu == "Listar":
        listar_avaliacoes()
    elif menu == "Atualizar":
        atualizar_avaliacao()
    elif menu == "Deletar":
        deletar_avaliacao()
