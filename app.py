import streamlit as st


# --------------------------------------------------------------------
# CONFIGURAÇÃO DA PAGINA
st.set_page_config(page_title = "Portifólio | Ciência de Dados", page_icon = "📊", layout = "wide")


# --------------------------------------------------------------------
# ESSA FUNÇÃO É A RESPOSÁVEL POR CARREGAR E ESTIILIZAR OS ELEMENTOS DA PÁGINA.

def carregar_estilos(caminho_css):
    """Lê o arquivo CSS externo e o injeta na aplicação"""
    with open(caminho_css, "r", encoding = "utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

carregar_estilos("utils/style.css")


# AQUI É FEITO A ATRIBUIÇÃO DAS PAGINAS AS VARIAVEIS, UTILIZADAS PARA ACOMODAR A HOME E A PAGINA DE PROJETOS
home = st.Page("paginas/home.py", title="Início", default=True)
projetos = st.Page("paginas/projetos.py", title="Projetos", url_path="projetos")

pg = st.navigation([home, projetos], position="hidden")
pg.run()


