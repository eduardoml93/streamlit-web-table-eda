import streamlit as st
import pandas as pd
import base64
import requests
from bs4 import BeautifulSoup
import plotly.express as px
from io import StringIO

# Função para carregar a imagem e converter para base64
def get_base64_of_image(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Função para definir o background com escurecimento
def set_background(image_file="bg.jpeg", darkness=0.5):
    base64_str = get_base64_of_image(image_file)
    css = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,{darkness}), rgba(0,0,0,{darkness})), 
                          url("data:image/jpeg;base64,{base64_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .title-box {{
        background: rgba(0, 0, 0, 0.3);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 28px;
        font-weight: bold;
        width: 60%;
        margin: auto;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Função para extrair tabelas via BeautifulSoup
# Função para extrair tabelas via BeautifulSoup (ajustada para evitar FutureWarning)
def extrair_tabelas(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    tabelas_html = soup.find_all('table')
    dfs = []
    for i, tabela in enumerate(tabelas_html):
        try:
            # Usando StringIO para evitar FutureWarning
            html_io = StringIO(str(tabela))
            df = pd.read_html(html_io)[0]
            dfs.append(df)
        except ValueError:
            st.warning(f"Não foi possível converter a tabela {i+1} em DataFrame.")
    return dfs

# Inicializar Session State
if "tables" not in st.session_state:
    st.session_state.tables = []
if "df" not in st.session_state:
    st.session_state.df = None
if "selected_table" not in st.session_state:
    st.session_state.selected_table = None
if "url" not in st.session_state:
    st.session_state.url = ""

# Aplicando o background
set_background("bg.jpg", darkness=0.5)

def main():
    st.markdown('<div class="title-box">Web Table Analyzer</div>', unsafe_allow_html=True)

    url = st.text_input("Digite a URL da página com tabelas:", value=st.session_state.url)
    st.session_state.url = url

    if st.button("Carregar Tabelas da Página"):
        dfs = extrair_tabelas(url)
        if dfs:
            st.session_state.tables = dfs
            st.success(f"Foram encontradas **{len(dfs)}** tabelas nesta página.")
            st.session_state.selected_table = 0
            st.session_state.df = dfs[0]
        else:
            st.warning("Nenhuma tabela encontrada na página fornecida.")
            st.session_state.tables = []
            st.session_state.df = None

    # Se houver tabelas carregadas
    if st.session_state.tables:
        idx = st.selectbox(
            "Escolha a tabela para análise",
            range(len(st.session_state.tables)),
            index=st.session_state.selected_table if st.session_state.selected_table is not None else 0
        )
        st.session_state.selected_table = idx
        st.session_state.df = st.session_state.tables[idx]

    # Se houver DataFrame selecionado, exibir e analisar
    if st.session_state.df is not None:
        st.write("### Visualização dos Dados:")
        st.dataframe(st.session_state.df)

        df = st.session_state.df
        num_cols = df.select_dtypes(include="number").columns
        cat_cols = df.select_dtypes(include="object").columns

        # Histograma
        st.write("### Histograma")
        if len(num_cols) > 0:
            selected_hist = st.selectbox("Selecione a coluna numérica", num_cols)
            fig_hist = px.histogram(df, x=selected_hist, nbins=20, title=f"Distribuição de {selected_hist}")
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("Não há colunas numéricas.")

        # Dispersão
        st.write("### Dispersão")
        if len(num_cols) >= 2:
            col_x = st.selectbox("Eixo X", num_cols, index=0)
            col_y = st.selectbox("Eixo Y", num_cols, index=1)
            fig_scatter = px.scatter(df, x=col_x, y=col_y, title=f"Dispersão: {col_x} vs {col_y}")
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("Não há colunas numéricas suficientes.")

        # Boxplot
        st.write("### Boxplot")
        if len(num_cols) > 0:
            selected_box = st.selectbox("Coluna para Boxplot", num_cols)
            fig_box = px.box(df, y=selected_box, title=f"Boxplot de {selected_box}")
            st.plotly_chart(fig_box, use_container_width=True)
        else:
            st.info("Não há colunas numéricas.")

        # Heatmap
        st.write("### Correlação (Heatmap)")
        if len(num_cols) > 1:
            corr = df[num_cols].corr()
            fig_heatmap = px.imshow(corr, text_auto=True, color_continuous_scale="RdBu_r")
            st.plotly_chart(fig_heatmap, use_container_width=True)
        else:
            st.info("Não há colunas numéricas suficientes.")

        # Gráfico de Contagem
        st.write("### Contagem de Categorias")
        if len(cat_cols) > 0:
            selected_cat = st.selectbox("Selecione coluna categórica", cat_cols)
            count_data = df[selected_cat].value_counts().reset_index()
            count_data.columns = [selected_cat, "Quantidade"]
            fig_bar = px.bar(count_data, x=selected_cat, y="Quantidade", title=f"Contagem de {selected_cat}")
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.info("Não há colunas categóricas.")

if __name__ == "__main__":
    main()
