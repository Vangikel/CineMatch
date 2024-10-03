# pages/aggregation.py
import streamlit as st
import requests  # Para realizar chamadas à API

API_URL = "http://localhost:8000/recomendacoes"  # URL base da API

def run_aggregation():
    st.subheader("Pipeline de Recomendações")
    
    # Adicionar campo para o usuário inserir o ID
    usuario_id = st.text_input("Insira o ID do usuário para obter recomendações:")
    
    if st.button("Executar Recomendações"):
        if usuario_id:
            # Realizando a chamada com o usuário_id
            response = requests.get(f"{API_URL}/{usuario_id}")
            if response.status_code == 200:
                resultados = response.json()
                st.write(resultados)
            else:
                st.error("Erro ao executar a recomendação.")
        else:
            st.warning("Por favor, insira um ID de usuário válido.")

def run():
    st.title("Recomendações de Filmes")
    run_aggregation()

