# app.py
import streamlit as st
from multiapp import MultiApp
from pages import home, usuarios, filmes, generos, avaliacoes, aggregation

app = MultiApp()

# Adicionando as páginas
app.add_app("Home", home.run)
app.add_app("Usuários", usuarios.run)
app.add_app("Filmes", filmes.run)
app.add_app("Gêneros", generos.run)
app.add_app("Avaliações", avaliacoes.run)
app.add_app("Agregação", aggregation.run)
# Executar o aplicativo
app.run()

