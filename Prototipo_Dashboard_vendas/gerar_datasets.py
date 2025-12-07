import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
import names

# pip install pandas
# pip install names
# pip install openpyxl
# pip install streamlit 

#Gerar, de forma randômica, as massas de dados (dataset) para o protótipo

#Retorna o diretório (pasta) onde o script Python (gerar datsets.py)
#aualmente em execução está localizado
pasta_datasets = Path(__file__).parent /"datasets"

#Cria um diretório e todos os seus pais que existirem
pasta_datasets.mkdir(parents=True, exist_ok=True)

LOJAS = {
    {"estado": "Sp",
    "cidade":"São Paulo",
    "vendedores": ["Juninho Pernanbucano", "Bruno Henrique"]},
    
   {"estado": "RJ",
    "cidade":"Rio de Janeiro",
    "vendedores": ["Gaules", "Celbit"]},  
    
   {"estado": "RS",
    "cidade":"Sapucaia do Sul",
    "vendedores": ["Adamastor", "Clovis"]},
   
   {"estado": "SC",
    "cidade":"Coronel Freitas",
    "vendedores": ["Marcelo Caps", "Mayron"]},
   
    {"estado": "MG",
    "cidade":"Belo Horizonte",
    "vendedores": ["Nathan", "Enzo"]},
}

PRODUTOS = {
    {"nome": "Notebook Dell Inspiron",
     "id": 1,
     "preço": 3000},
    
    {"nome": "Nvidia GeForce RTX 5060 Ti 16 GB",
     "id": 2,
     "preço": 4000},
    
    {"nome": "Mouse Gamer X11 Attack Shark Tri Mode 22000dpi Paw3311 Dock",
     "id": 3,
     "preço": 200},
    
    {"nome": "Fone De Ouvido Kz Edx Pro",
     "id": 4,
     "preço": 70},
    
     {"nome": "Controle Sem Fio 8bitdo Ultimate 2 Gatilhos Hall Tmr Pro",
     "id": 5,
     "preço": 430},
    
}

FORMA_PAGTO = ["cartão de crédito", "pix", "boleto", "dinheiro", "cartão de débito"]

GENERO_CLIENTES = ["Masculino", "Feminino",]

compras = []

#Laço de repetição gerador do dataset
for _ in range(QUANTIDAE_MAXIMA_REGISTROS)
    loja = random.choice(LOJAS)
    
    vendedor = random.choice(loja["vendedores"])
    
    produto = random.choice(PRODUTOS)
    
    data_hora_compra = datetime.now() - timedelta(
        days    = random.randint(1, 365)
        hours   = random.randint(-5,5)
        minutes = random.randint(-30, 30)
    )
    
    genero_clientes = random.choice(GENERO_CLIENTES)
 
    nome_cliente    = names.get.full_name(genero_clientes)
 
    forma_pagamento = random.choice(FORMA_PAGTO)
    
    compras.append({
        "data_hora_compra": data_hora_compra,
        
        "id_da_compra": 0,
        
        "cidade_loja": loja["cidade"],
        
        "vendedor": vendedor,
        
        "nome_produto": produto["nome"],
        
        "cliente_nome": nome_cliente,
        
        "cliente_genero": Genero_cliente,
        
        "forma_pagto": forma_pagamento
    })
    
    
df_compras = pd.DataFrame(compras).set_index("data_hora_compra").sort_index()

# Gerar o "id_compra", que é o identificador ÚNICO de cada registro usando list comprehension

df_compras["id_compra"] = [id for id in range(len(df_compras))]

df_lojas = pd.DataFrame(LOJAS)

df_produtos = pd.DataFrame(PRODUTOS)

#Exportar os dataframes para arquivos

df_compras.to_csv(pasta_datasets / "compras.csv"
        , decimal=","
        , sep=";")

df_lojas.to_csv(pasta_datasets / "lojas.csv"
        , decimal=","
        , sep=";")

df_produtos.to_csv(pasta_datasets / "produtos.csv"
        , decimal=","
        , sep=";")

# Gerar arquivos.xlsx do Excel

df_compras.to_excel(pasta_datasets / "compras.xlsx"
        , decimal=","
        , sep=";")

df_lojas.to_excel(pasta_datasets / "lojas.xlsx"
        , decimal=","
        , sep=";")

df_produtos.to_excel(pasta_datasets / "produtos.xlsx"
        , decimal=","
        , sep=";")

print("Geração dos datasets concluída com sucesso.")
        
        



