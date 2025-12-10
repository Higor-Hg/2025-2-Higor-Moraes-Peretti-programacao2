from datetime import datetime
from pathlib import Path 
import pandas as pd
import streamlit as st 

# Retorna o diretório (pasta) onde o script Python (gerar_datasets.py) atualmente em execução está localizado
pasta_datasets = Path(__file__).parent / 'datasets'

vendas_csv = pasta_datasets / "compras.csv"
caminho_lojas_csv = pasta_datasets / "lojas.csv"
caminho_produtos_csv = pasta_datasets / "produtos.csv"

df_compras = pd.read_csv(vendas_csv, sep=";", decimal= ",", index_col=0)
df_lojas = pd.read_csv(caminho_lojas_csv, sep=";", decimal= ",")
df_produtos = pd.read_csv(caminho_produtos_csv, sep=";", decimal= ",")

df_lojas["estado/cidade"] = df_lojas["estado"] + "/" + df_lojas["cidade"]
lista_lojas = df_lojas["estado/cidade"].tolist()
loja_selecionada = st.sidebar.selectbox("Selecione a loja: ", lista_lojas)

lista_vendedores = df_lojas.loc[df_lojas["estado/cidade"] == loja_selecionada, "vendedores"].iloc[0]
lista_vendedores = lista_vendedores.strip("][").replace("","").split(",")

vendedor_selecionado = st.sidebar.selectbox("Selecione o vendedor: ", lista_vendedores)
#print(lista_vendedores)

lista_produtos = df_produtos["nome"].tolist()
produto_selecionado = st.sidebar.selectbox("Selecione o produto", lista_produtos)

nome_cliente = st.sidebar.text_input("Nome do cliente")
genero_selecionado = st.sidebar.selectbox("Gênero do cliente: ", ["Masculino", "Feminino"])


