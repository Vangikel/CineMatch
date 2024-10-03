'''# pages/usuarios.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/usuarios"  # URL da sua API

def criar_usuario():
    st.subheader("Criar Usuário")
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")  # Adicionando campo de senha
    if st.button("Criar Usuário"):
        response = requests.post(API_URL, json={"nome": nome, "email": email, "senha": senha})  # Incluindo senha na requisição
        if response.status_code == 201 or 200:
            st.success("Usuário criado com sucesso!")
        else:
            st.error("Erro ao criar usuário.")

def listar_usuarios():
    st.subheader("Listar Usuários")
    response = requests.get(API_URL)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            st.write(f"ID: {usuario['usuario_id']} | Nome: {usuario['nome']} | Email: {usuario['email']}")

def atualizar_usuario():
    st.subheader("Atualizar Usuário")
    usuario_id = st.text_input("ID do Usuário:")
    novo_nome = st.text_input("Novo Nome:")
    nova_senha = st.text_input("Nova Senha:", type="password")  # Adicionando campo de nova senha
    if st.button("Atualizar Usuário"):
        response = requests.put(f"{API_URL}/{usuario_id}", json={"nome": novo_nome, "senha": nova_senha})  # Incluindo nova senha na requisição
        if response.status_code == 200:
            st.success("Usuário atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar usuário.")

def deletar_usuario():
    st.subheader("Deletar Usuário")
    usuario_id = st.text_input("ID do Usuário para deletar:")
    if st.button("Deletar Usuário"):
        response = requests.delete(f"{API_URL}/{usuario_id}")
        if response.status_code == 204:
            st.success("Usuário deletado com sucesso!")
        else:
            st.error("Erro ao deletar usuário.")

def run():
    st.title("CRUD de Usuários")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Criar", "Listar", "Atualizar", "Deletar"])

    if menu == "Criar":
        criar_usuario()
    elif menu == "Listar":
        listar_usuarios()
    elif menu == "Atualizar":
        atualizar_usuario()
    elif menu == "Deletar":
        deletar_usuario()
'''
# pages/usuarios.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/usuarios"  # URL da sua API

def criar_usuario():
    st.subheader("Criar Usuário")
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    senha = st.text_input("Senha:", type="password")  # Adicionando campo de senha
    if st.button("Criar Usuário"):
        response = requests.post(API_URL, json={"nome": nome, "email": email, "senha": senha})  # Incluindo senha na requisição
        if response.status_code in [201, 200]:  # Corrigindo a verificação de status
            st.success("Usuário criado com sucesso!")
        else:
            st.error("Erro ao criar usuário.")

def listar_usuarios():
    st.subheader("Listar Usuários")
    response = requests.get(API_URL)
    if response.status_code == 200:
        usuarios = response.json()
        st.write(usuarios)  # Adicionando esta linha para ver a estrutura dos dados
        if usuarios:  # Verifica se a lista não está vazia
            for usuario in usuarios:
                # Usando get para evitar KeyError
                st.write(f"ID: {usuario.get('id', 'ID não encontrado')} | Nome: {usuario.get('nome', 'Nome não encontrado')} | Email: {usuario.get('email', 'Email não encontrado')}")
        else:
            st.write("Nenhum usuário encontrado.")  # Mensagem para lista vazia
    else:
        st.error("Erro ao listar usuários.")



'''def atualizar_usuario():
    st.subheader("Atualizar Usuário")
    usuario_id = st.text_input("ID do Usuário:")
    novo_nome = st.text_input("Novo Nome:")
    nova_senha = st.text_input("Nova Senha:", type="password")  # Adicionando campo de nova senha
    if st.button("Atualizar Usuário"):
        response = requests.put(f"{API_URL}/{usuario_id}", json={"nome": novo_nome, "senha": nova_senha})  # Incluindo nova senha na requisição
        if response.status_code == 200:
            st.success("Usuário atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar usuário.")'''
def atualizar_usuario():
    st.subheader("Atualizar Usuário")
    
    # Campos para entrada de dados
    usuario_id = st.text_input("ID do Usuário:")
    novo_nome = st.text_input("Novo Nome:")
    novo_email = st.text_input("Novo Email:")  # Campo para novo email
    nova_senha = st.text_input("Nova Senha:", type="password")  # Campo para nova senha
    
    # Botão de atualização
    if st.button("Atualizar Usuário"):
        # Fazendo a requisição PUT com nome, email e senha
        response = requests.put(
            f"{API_URL}/{usuario_id}", 
            json={"nome": novo_nome, "email": novo_email, "senha": nova_senha}  # Incluindo o email na requisição
        )
        
        # Verificando a resposta
        if response.status_code == 200:
            st.success("Usuário atualizado com sucesso!")
        else:
            st.error("Erro ao atualizar usuário.")

def deletar_usuario():
    st.subheader("Deletar Usuário")
    usuario_id = st.text_input("ID do Usuário para deletar:")
    if st.button("Deletar Usuário"):
        response = requests.delete(f"{API_URL}/{usuario_id}")
        if response.status_code == 204 or 200:
            st.success("Usuário deletado com sucesso!")
        else:
            st.error("Erro ao deletar usuário.")

def run():
    st.title("CRUD de Usuários")
    menu = st.sidebar.selectbox("Selecione uma opção", ["Criar", "Listar", "Atualizar", "Deletar"])

    if menu == "Criar":
        criar_usuario()
    elif menu == "Listar":
        listar_usuarios()
    elif menu == "Atualizar":
        atualizar_usuario()
    elif menu == "Deletar":
        deletar_usuario()
