import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names


# pip install pandas
# pip install names
# pip install openpyxl
# pip install streamlit


# ================= CONFIGURAÇÕES =================


QUANTIDADE_MAXIMA_REGISTROS = 100


# Retorna o diretório onde o script está salvo
pasta_datasets = Path(__file__).parent / "datasets"


# Cria a pasta se não existir
pasta_datasets.mkdir(parents=True, exist_ok=True)


# ================= BASES DE DADOS =================


LOJAS = [
    {"estado": "SP", "cidade": "São Paulo", "vendedores": ["Juninho Pernambucano", "Bruno Henrique"]},
    {"estado": "RJ", "cidade": "Rio de Janeiro", "vendedores": ["Gaules", "Cellbit"]},
    {"estado": "RS", "cidade": "Sapucaia do Sul", "vendedores": ["Adamastor", "Clovis"]},
    {"estado": "SC", "cidade": "Coronel Freitas", "vendedores": ["Marcelo Caps", "Mayron"]},
    {"estado": "MG", "cidade": "Belo Horizonte", "vendedores": ["Nathan", "Enzo"]},
]


PRODUTOS = [
    {"nome": "Notebook Dell Inspiron", "id": 1, "preço": 3000},
    {"nome": "Nvidia GeForce RTX 5060 Ti 16 GB", "id": 2, "preço": 4000},
    {"nome": "Mouse Gamer X11", "id": 3, "preço": 200},
    {"nome": "Fone De Ouvido KZ EDX Pro", "id": 4, "preço": 70},
    {"nome": "Controle Sem Fio 8BitDo", "id": 5, "preço": 430},
]


FORMA_PAGTO = ["cartão de crédito", "pix", "boleto", "dinheiro", "cartão de débito"]
GENERO_CLIENTES = ["Masculino", "Feminino"]


# ================= GERADOR DE COMPRAS =================


compras = []


for _ in range(QUANTIDADE_MAXIMA_REGISTROS):
    loja = random.choice(LOJAS)
    vendedor = random.choice(loja["vendedores"])
    produto = random.choice(PRODUTOS)


    data_hora_compra = datetime.now() - timedelta(
        days=random.randint(1, 365),
        hours=random.randint(-5, 5),
        minutes=random.randint(-30, 30)
    )


    genero_cliente = random.choice(GENERO_CLIENTES)
    nome_cliente = names.get_full_name()
    forma_pagamento = random.choice(FORMA_PAGTO)


    compras.append({
        "data_hora_compra": data_hora_compra,
        "cidade_loja": loja["cidade"],
        "estado_loja": loja["estado"],
        "vendedor": vendedor,
        "nome_produto": produto["nome"],
        "produto_id": produto["id"],
        "preco_produto": produto["preço"],
        "cliente_nome": nome_cliente,
        "cliente_genero": genero_cliente,
        "forma_pagto": forma_pagamento
    })


# ================= DATAFRAMES =================


df_compras = pd.DataFrame(compras)
df_compras = df_compras.sort_values("data_hora_compra").reset_index(drop=True)
df_compras["id_compra"] = df_compras.index + 1


df_lojas = pd.DataFrame(LOJAS)
df_produtos = pd.DataFrame(PRODUTOS)


# ================= EXPORTAÇÃO CSV =================


df_compras.to_csv(pasta_datasets / "compras.csv", index=False, sep=";", decimal=",")
df_lojas.to_csv(pasta_datasets / "lojas.csv", index=False, sep=";", decimal=",")
df_produtos.to_csv(pasta_datasets / "produtos.csv", index=False, sep=";", decimal=",")


# ================= EXPORTAÇÃO EXCEL =================


df_compras.to_excel(pasta_datasets / "compras.xlsx", index=False)
df_lojas.to_excel(pasta_datasets / "lojas.xlsx", index=False)
df_produtos.to_excel(pasta_datasets / "produtos.xlsx", index=False)


print("Geração dos datasets concluída com sucesso.")        