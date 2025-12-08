import pandas as pd
import streamlit as st
from pathlib import Path 

# Retorna o diretório (pasta) onde o script Python (gerar_datasets.py) atualmente em execução está localizado
pasta_datasets = Path(__file__).parent / "datasets"

vendas_csv = pasta_datasets / "compras.csv"

print(f"caminho arquivo: {vendas_csv}")

#Criar dataframe vendas

df_compras = pd.read_csv(vendas_csv, sep=";", decimal= ",", index_col=0)

#Criar colunas
colunas = list(df_compras.columns)

#definir sidebar
colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas", colunas, colunas)

#Propriedades da sidetar
coluna01, coluna02 = st.sidebar.columns(2)

coluna_filtro = coluna01.selectbox("Selecione a coluna", (c for c in colunas if c not in ["id_compra"]))

valor_filtro = coluna02.selectbox("Selecione o valor",
        list(df_compras[coluna_filtro].unique()))

btn_filtrar = coluna01.button("Filtrar")

btn_limpar = coluna02.button("Limpar")

if btn_filtrar:
    st.dataframe(df_compras.loc[df_compras[coluna_filtro] == valor_filtro], colunas_selecionadas)
    
elif btn_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
    
else:
    st.dataframe(df_compras[colunas_selecionadas])
