import streamlit as st
import joblib


# aplica a função para carregar o modelo dentro do streamlit
@st.cache_resource
def carregar_modelo(caminho):
    return joblib.load(caminho)

# -------------------------------------------------------------------
# DADOS DOS PROJETOS
PROJETOS = {
    "credit-risk": {
        "nome": "Credit Risk",
        "disponivel": True,
        "modelo":"assets/credit-risk/XGB_credit_risk.pkl", # caminho para o modelo
        "threshold":"0.37", # threshold utilizado
        "badges": "Classificação • Bancário • Machine Learning",
        "descricao": (
            "Modelo de classificação que estima a probabilidade de um cliente se tornar "
            "inadimplente, a partir de informações financeiras, demográficas e comportamentais."
        ),
        "orientacao": (
            "Preencha os campos abaixo com o perfil de um cliente fictício e clique em "
            "Rodar modelo para ver a probabilidade de inadimplência estimada."
        ),
    },
    "projeto-2": {"nome": "Projeto 2", "disponivel": False},
    "projeto-3": {"nome": "Projeto 3", "disponivel": False},
    "projeto-4": {"nome": "Projeto 4", "disponivel": False},
    "projeto-5": {"nome": "Projeto 5", "disponivel": False},
    "projeto-6": {"nome": "Projeto 6", "disponivel": False},
}

# --------------------------------------------------------------------
# CONTROLE DE SELEÇÃO
if "projeto" not in st.session_state:
    st.session_state.projeto = None

def selecionar(chave):
    st.session_state.projeto = chave

col_principal, col_lista = st.columns([3, 1], gap="large")

# --------------------------------------------------------------------
# LISTA LATERAL DE PROJETOS
with col_lista:
    with st.container(key="lista-projetos"):
        st.html('<p class="lista-titulo">Projetos</p>')
        for chave, p in PROJETOS.items():
            rotulo = p["nome"] if p["disponivel"] else f"{p['nome']} · Em breve"
            st.button(
                rotulo,
                key=f"btn-{chave}",
                on_click=selecionar,
                args=(chave,),
                disabled=not p["disponivel"],
                type="primary" if st.session_state.projeto == chave else "secondary",
                use_container_width=True,
            )

# --------------------------------------------------------------------
# ÁREA PRINCIPAL
with col_principal:
    st.html('<a class="voltar" href="/" target="_self">← Voltar ao início</a>')

    selecionado = st.session_state.projeto

    # ESTADO 1: NENHUM PROJETO SELECIONADO
    if selecionado is None:
        st.html("""
        <section class="lab-intro">
            <h2>Laboratório de Modelos</h2>
            <p>
                Aqui você pode testar na prática os modelos de Machine Learning desenvolvidos
                neste portfólio. Escolha um projeto na lista ao lado, preencha os dados
                solicitados e veja como o modelo responde em tempo real.
            </p>
        </section>
        """)
        st.html('<div class="resultado-vazio">Selecione um projeto na lista para começar.</div>')

    # ESTADO 2: PROJETO SELECIONADO
    else:
        p = PROJETOS[selecionado]
        modelo = carregar_modelo(p["modelo"]) # carerga o modelo
        st.write(modelo.feature_names_in_) # exibe os campos que o modelo espera receber
        st.html(f"""
        <section class="lab-intro">
            <span class="tag tag-destaque">{p['nome']}</span>
            <p class="project-tags">{p['badges']}</p>
            <p>{p['descricao']}</p>
            <p class="lab-orientacao">{p['orientacao']}</p>
        </section>
        """)

        with st.form(f"form-{selecionado}"):
            st.html('<p class="lab-aviso">Os campos de entrada serão adicionados aqui.</p>')
            rodar = st.form_submit_button("Rodar modelo")

        if rodar:
            st.html('<div class="resultado">O resultado do modelo vai aparecer aqui.</div>')
        else:
            st.html('<div class="resultado-vazio">Preencha os campos e clique em Rodar modelo para ver a previsão.</div>')