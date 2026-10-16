import streamlit as st
import base64
from pathlib import Path



# SEÇÃO HERO
st.html("""
<div class="hero">

    <div class="hero-content">

        <h1>CIÊNCIA DE DADOS</h1>

        <p>
            Machine Learning • Análise de Dados • Previsões
        </p>

        
        <a
            href="/projetos" target="-self" class="hero-explorar"
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

    <div class="hero-bottom"></div>
    </div>

</div>
""")

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



# SEÇÃO PROJETOS EM DESTAQUE

# FAZ COM QUE A IMAGEM SEJA CARREGADA SOMENTE 1 VEZ, AJUDA NO DESEMPENHO
@st.cache_data

# FUNÇÃO PARA IMPORTAÇÃO DA IMAGEN
def img_base64(caminho):
    return base64.b64encode(Path(caminho).read_bytes()).decode()

# CAPTURA O CAMINHO DO GRÁFICO JUNTO A FUNÇÃO
grafico = img_base64("assets/credit-risk/compracao_modelos.png")

# RESPONAVEL POR COLETAR OS DADOS QUE FICARÃO NOS CARDS
projetos = [
    {"nome": "PROJETO 2", "badges":["Regressão","Varejo"],"descricao": "Breve descrição do problema abordado e da técnica utilizada."},
    {"nome":"PROJETO 3","badges":["Regressão","Varejo"],"descricao":"Descrição Breve do segundo projeto."},
    {"nome": "PROJETO 4", "badges":["Regressão","Varejo"],"descricao": "Descrição breve do terceiro projeto."},
    {"nome": "PROJETO 5", "badges":["Regressão","Varejo"],"descricao": "Descrição breve do quarto projeto."},
    {"nome": "PROJETO 6", "badges":["Regressão","Varejo"],"descricao": "Descrição breve do quinto projeto."}
]

# MONTAR OS CARDS NA SEÇÃO PROJETOS EM DESTAQUE
def montar_card(p):
    badges = " • ".join(p["badges"])
    return f"""
    <div class="project-selector">
        <span class="tag">{p['nome']}</span>
        <p class="project-tags">{badges}</p>
        <div class="project-tooltip">{p['descricao']}</div>
    </div>
    """

# MONTA OS CARDS
cards = "".join(montar_card(p) for p in projetos)

# HMTL DA SEÇÃO, ESTRUTURA E CRIA AS CLASSES PARA SEREM FORMATADAS PELO CSS
st.html(
f"""
<section class = "secao-destaque">
    <h2>Projetos em Destaque</h2>
    <div class ="destaque-grid">

        <div class = "project-card">
            <span class = "tag tag-destaque">Credit Risk</span>

            <p class="project-tags">Classificação • Bancário • Machine Learning</p>

            <p>
            Projeto de Machine Learning voltado à previsão de inadimplência no contexto de risco de crédito.
            A solução utiliza dados financeiros, demográficos e comportamentais para identificar clientes com
            maior probabilidade de default, passando por análise exploratória, engenharia de variáveis,
            tratamento do desbalanceamento e comparação de diferentes modelos preditivos.
            </p>

        </div>

        <figure class ="project-chart">
            <img src="data:image/png;base64,{grafico}" alt = "Comparação entre modelos testados">
        </figure>

    </div>
    
    <div class="project-selector-container"> {cards} </div>
    <a
        href="/projetos"
        target="_self"
        class="project-explorar"
    >
        Explorar Projetos  →
    </a>
    <div class="project-bottom"></div>

</section>

"""
)
# --------------------------------------------------------------------

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



