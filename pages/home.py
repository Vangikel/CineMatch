import streamlit as st
import requests  # Para realizar chamadas à API
import matplotlib.pyplot as plt

def run():
    # Estilos personalizados
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('assets/background.jpg');
            background-size: cover;
            background-position: center;
            padding: 20px;
        }
        h1 {
            font-family: 'Lobster', cursive;  /* Mudando a fonte do título */
            color: #ffcc00;  /* Cor do título */
            text-align: center;  /* Centralizando o título */
            font-size: 3em;  /* Tamanho do título */
            margin-top: 20px;  /* Margem acima do título */
        }
        h2 {
            font-family: 'Roboto', sans-serif;  /* Mudando a fonte do subtítulo */
            color: #ffffff;  /* Cor do subtítulo */
            text-align: center;  /* Centralizando o subtítulo */
        }
        p {
            font-family: 'Roboto', sans-serif;  /* Mudando a fonte do texto */
            color: #ffffff;  /* Cor do texto */
            text-align: left;  /* Alinhamento do texto */
        }
        .card {
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
        }
        </style>
        <link href="https://fonts.googleapis.com/css2?family=Lobster&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        """,
        unsafe_allow_html=True
    )

    st.title("Bem-vindo ao CineMatch!")
    
    st.subheader("Sua plataforma de gerenciamento de filmes")

    # Criando um layout de colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("assets/cinema.jpg", use_column_width=True)  # Verifique se a imagem está no diretório correto
        
    with col2:
        st.write(""" 
        O CineMatch é uma aplicação que permite que você gerencie seus filmes, gêneros e avaliações de forma simples e eficiente.

        Utilize o menu lateral para acessar as diferentes funcionalidades da aplicação:
        - **👤 Usuários**: Crie, leia, atualize e delete usuários.
        - **🎥 Filmes**: Gerencie seus filmes, adicionando novos títulos, editando informações e deletando quando necessário.
        - **📚 Gêneros**: Organize seus filmes por gênero, criando categorias que facilitam a busca.
        - **⭐ Avaliações**: Avalie os filmes que assistiu e compartilhe suas opiniões.
        - **📊 Agregações**: Execute análises para obter insights sobre seus filmes e avaliações.
        """)

    st.markdown("---")  # Adiciona uma linha horizontal para separação

    st.markdown("## Como Usar")
    st.write(""" 
    1. **Navegue pelo menu lateral**: Selecione a opção desejada.
    2. **Preencha os formulários**: Insira as informações necessárias para cada ação.
    3. **Visualize os resultados**: Após executar as ações, veja os resultados diretamente na interface.
    """)

    # Gráfico de exemplo
    st.markdown("## Avaliações Recentes")
    # Simulando dados para o gráfico
    filmes = ['Filme A', 'Filme B', 'Filme C']
    notas = [8, 7, 9]

    plt.bar(filmes, notas, color='orange')
    plt.xlabel('Filmes')
    plt.ylabel('Notas')
    plt.title('Notas dos Filmes Recentes')
    st.pyplot(plt)

    st.markdown("---")  # Adiciona uma linha horizontal para separação
    st.markdown(
    """
    <style>
    .card {
        background-color: #6399BA;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        padding: 15px;
        margin: 10px 0;
        color: #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    # Exemplo de cartão
    with st.container():
        st.markdown("## Cartão de Exemplo")
        st.markdown('<div class="card">Este é um cartão exemplo para mostrar informações importantes.</div>', unsafe_allow_html=True)

       
        # Cartão de informações do filme
        st.markdown("""
            <div class="card">
                <h3>Título do Filme</h3>
                <p>Gênero: Ação</p>
                <p>Ano: 2022</p>
                <p>Sinopse: Um breve resumo do enredo do filme.</p>
                color: #000000
            </div>
            
        """, unsafe_allow_html=True)

# Chame a função run() se este arquivo for executado diretamente
if __name__ == "__main__":
    run()


