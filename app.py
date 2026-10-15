import streamlit as st

# --------------------------------------------------------------------
# CONFIGURAÇÃO DA PAGINA
st.set_page_config(page_title = "Data Science Portfolio", page_icon = "📊", layout = "wide")

st.html("""
    <style>

    </style>
"""
)
# --------------------------------------------------------------------

# SEÇÃO HERO
st.html("""
<div class="hero">

    <div class="hero-content">

        <h1>CIÊNCIA DE DADOS</h1>

        <p>
            Machine Learning • Análise de Dados • Previsões
        </p>

        
        <a
            class="hero-explorar"
        >
            Explorar Projetos  
        </a>

        
        <a
            href="https://github.com/Rd-Brito13"
            target="_blank"
            class="hero-github"
        >
            GitHub 
        </a>


    </div>
    <div class="hero-bottom-explorar">

    <div class="hero-bottom">
    </div>

</div>
""")

# --------------------------------------------------------------------




# --------------------------------------------------------------------
# SEÇÃO VISÃO GERAL
st.html("""
<div class="visao-geral">

    <div class="visao-content">

        <h2>Visão Geral</h2>

        <p>
            Este é um portfólio interativo com projetos de Ciência de Dados desenvolvidos do início ao fim, da coleta dos dados ao modelo em funcionamento. 
            Aqui você encontra análises exploratórias e visualizações que revelam padrões e insights, modelos de Machine Learning de classificação, regressão e agrupamento avaliados com métricas claras, e soluções preditivas aplicadas a cenários reais. 
            Além de conhecer o raciocínio por trás de cada projeto, você pode colocar os modelos à prova, basta clicar no botão "Explorar Projetos" disponível no inicio da pagina.
        </p>
    </div>
</div>
""")
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# SEÇÃO TIPOS DE PROJETOS
st.html("""
<section class="tipos-projetos">
    <h2>Tipos de Projetos</h2>
    <div class="cards">
        
        <div class = "card">
        <span class="tag">Aprendizado Supervisionado</span>
        <h3>Classificação</h3>
        <p>Risco de crédito, churn e previsão de comportamento</p>
        </div>

        <div class="card">
        <span class="tag">Aprendizado não Supervisionado</span>
        <h3>Segmentação</h3>
        <p>Segmentação de clientes e de perfis bancários</p>
        </div>

        <div class = "card">
        <span class="tag">Séries temporais</span>
        <h3>Previsão</h3>
        <p>Forecasting e análise de padrões ao longo do tempo</p>
        </div>
    </div>
</section>
""")
#--------------------------------------------------------





# --------------------------------------------------------
# SEÇÃO PROJETOS EM DESTAQUE
st.header("Projetos em Destaque")
 

# CRIANDO AS COLUNAS PARA A DESCRIÇÃO DO CARD DO PROJETO E A IMAGEM UTILIZADA
col6, col7 = st.columns([2,1])

# FORMATAÇÃO HTML PARA O CARD 6 E AS LEGENDAS
with col6:
    st.html("""
    <div class="project-card">
        <h3>CREDIT RISK</h3>

        <p class="project-tags">
            Classificação • Bancário • Machine Learning
        </p>

        <p>
        Projeto de Machine Learning voltado à previsão de indimplência no contexto de risco de crédito.
        A solução utiliza dados financeiros, demográficos e comportamentais para identificar clientes com
        maior probabilidade de default, passando por análise exploratória, 
        engenharia de variáveis, tratamento do desbalanceamento e comparação de diferentes modelos preditivos.
        </p>
        <p class = "project-tech">
        Python • Pandas • Numpy • Scikit-learn • XGBoost • Matplotlib • Seaborn
        </p>
    </div>
    """)

# IMPLEMENTAÇÃO DA IMAGEN PARA COMPARAÇÃO DOS MODELOS
with col7:
    st.image(
        "assets/credit-risk/compracao_modelos.png"
    )


# RESPONSAVEL POR CRIAR O CONTEINER, A DIV ONDE FICA O SPAN COM O TEXTO DENTRO DO CONTAINER E A DESCRIÇÃO DO TOOLTIP
st.html(
    """
<div class = "project-selector-container">
    <div class = "project-selector">
        <span>PROJECT 1</span>

        <div class = "project-tooltip">
            Breve descrição do projeto. Aqui vamos apresentar
            rapidamente o problema a abordado e a ténica utilizada.
        </div>
    </div>

    <div class="project-selector">
        <span>PROJECT 2</span>

        <div class="project-tooltip">
            Descrição breve do segundo projeto.
        </div>
    </div>

    <div class="project-selector">
        <span>PROJECT 3</span>

        <div class="project-tooltip">
            Descrição breve do terceiro projeto.
        </div>
    </div>

    <div class="project-selector">
        <span>PROJECT 4</span>

        <div class="project-tooltip">
            Descrição breve do quarto projeto.
        </div>
    </div>

    <div class="project-selector">
        <span>PROJECT 5</span>

        <div class="project-tooltip">
            Descrição breve do quinto projeto.
        </div>
    </div>

</div>
    """
)

# AQUI FICA O BOTÃO QUE SERÁ UTILIZADO PARA LEVAR A GUIA DE PROJETOS
st.write("Explore outros projetos →")







# --------------------------------------------------------------------
# SEÇÃO DA FOOTER DA PAGINA
st.html("""
<div class="footer">

    <div class="footer-content">

        <h3>PORTFÓLIO DE CIÊNCIA DE DADOS</h3>

        <p>
            Machine Learning • Análise de Dados • Previsões
        </p>

        <a
            href="https://github.com/Rd-Brito13"
            target="_blank"
            class="footer-github"
        >
            GitHub →
        </a>

    </div>

    <div class="footer-bottom">
        © 2026 - Rodrigo Brito
    </div>

</div>
""")
# --------------------------------------------------------------------




# --------------------------------------------------------------------
# ESSA FUNÇÃO É A RESPOSÁVEL POR CARREGAR E ESTIILIZAR OS ELEMENTOS DA PÁGINA.

def carregar_estilos(caminho_css):
    """Lê o arquivo CSS externo e o injeta na aplicação"""
    with open(caminho_css, "r", encoding = "utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

carregar_estilos("utils\style.css")

# --------------------------------------------------------------------