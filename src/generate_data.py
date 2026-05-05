import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine
import random

fake = Faker()
np.random.seed(42)

engine = create_engine("postgresql://user:password@db:5432/ecommerce")


categorias = ["Eletrônicos", "Roupas", "Casa", "Esportes"]
df_cat = pd.DataFrame({"nome": categorias})
df_cat["id"] = df_cat.index + 1
df_cat = df_cat[["id", "nome"]]
df_cat.to_sql("categorias", engine, if_exists="replace", index=False)

produtos = []
for i in range(20):
    produtos.append({
        "nome": fake.word(),
        "categoria_id": random.randint(1, 4),
        "preco": round(random.uniform(10, 500), 2)
    })

df_prod = pd.DataFrame(produtos)
df_prod["id"] = df_prod.index + 1
df_prod = df_prod[["id", "nome", "categoria_id", "preco"]]
df_prod.to_sql("produtos", engine, if_exists="replace", index=False)

vendas = []
for i in range(500):
    vendas.append({
        "produto_id": random.randint(1, 20),
        "data": fake.date_time_this_year(),
        "quantidade": random.randint(1, 5)
    })

df_vendas = pd.DataFrame(vendas)
df_vendas["id"] = df_vendas.index + 1
df_vendas = df_vendas[["id", "produto_id", "data", "quantidade"]]
df_vendas.to_sql("vendas", engine, if_exists="replace", index=False)
print("Dados gerados com sucesso!")
