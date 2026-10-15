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


# --------------------------------------------------------------------
# SEÇÃO HERO

#  DIVIDINDO A TELA EM 2 COLUNAS
col1, col2 = st.columns([2,1])

# PREENCHENDO A COLUNA 1
with col1:
    # TITULOS
    st.title("CIÊNCIA DE DADOS")
    
    # LEGENDAS
    st.write("Machine learning • Data Analysis • Statis")
    st.write("Projetos de Ciência de Dados voltados à análise, ""modelagem e compreensão de problemas do setor financeiro.")

    # CRIANDO OS BOTÕES E DEFININDO AS POSIÇÕES COM COLUNAS
    botao1, botao2, botao3= st.columns([1,1,5])
    # TEXTO DO BOTÃO 1
    with botao1:
        st.button("Explorar projetos")
        
    # TEXTO DO BOTÃO 2
    with botao2:
        st.button("Github")

# COLUNA 2 DA PAGINA
with col2:
    st.html("""
        <svg width="200" height="200">
            <circle
                cx="100"
                cy="100"
                r="30"
                fill="#149685"
            />
        </svg>
    """)


st.divider()
# --------------------------------------------------------------------




# --------------------------------------------------------------------
# SEÇÃO ABOUT THE PORTIFOLIO

# TITULO DA SEÇÃO
st.header("Sobre o Portifolio")

# LEGENDA DA SEÇÃO
st.write("Este portifólio reúne projetos desenvolvidos para explorar " "diferentes problemas de Data Science, desde classificação" " " \
"e previsão até segmentação de cleintes e análise de séries ""temporais.")

st.divider()
# --------------------------------------------------------------------



# --------------------------------------------------------------------
# SEÇÃO OQ EU CONSTRUO

# TITULO DA SEÇÃO
st.header("O que eu construo")

# DIVIDINDO EM 3 COLUNAS PARA OS CARDS
col3, col4, col5 = st.columns(3)

# CARD PARA CLASSIFICAÇÃO
with col3:
    st.subheader("Classificação")
    st.write("Aprendizado supervisionado")
    st.write("Credit Risk, Churn and Prediction")

# CARD PARA AGRUPAMENTO
with col4:
    st.subheader("Segmentação")
    st.write("Aprendizado não supervisionado")
    st.write("Customer and Banking segmentation")

# CARD PARA SÉRIES TEMPORAIS
with col5:
    st.subheader("Previsão")
    st.write("Séries Temporais")
    st.write("Forecasting and Temporal Analysis")


st.divider()
# --------------------------------------------------------------------





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
            Classification • Banking • Machine Learning
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


st.divider()
# --------------------------------------------------------------------





# --------------------------------------------------------------------
# SEÇÃO DA FOOTER DA PAGINA
st.html("""
<div class="footer">

    <div class="footer-content">

        <h3>PORTFÓLIO DE CIÊNCIA DE DADOS</h3>

        <p>
            Machine Learning • Data Analysis • Forecasting
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