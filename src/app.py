import streamlit as st
import pandas as pd
from db import get_engine

st.set_page_config(page_title="Dashboard E-commerce", layout="wide")

st.title("📊 Dashboard de Vendas - E-commerce")

engine = get_engine()

query = """
SELECT v.data, p.nome, c.nome as categoria, v.quantidade, p.preco
FROM vendas v
JOIN produtos p ON v.produto_id = p.id
JOIN categorias c ON p.categoria_id = c.id
"""

df = pd.read_sql(query, engine)
df["faturamento"] = df["quantidade"] * df["preco"]


st.sidebar.header("Filtros")
categoria = st.sidebar.selectbox("Categoria", df["categoria"].unique())
df = df[df["categoria"] == categoria]


col1, col2, col3 = st.columns(3)

col1.metric("💰 Faturamento Total", f"R$ {df['faturamento'].sum():.2f}")
col2.metric("📦 Total de Vendas", int(df["quantidade"].sum()))
col3.metric("🛒 Ticket Médio", f"R$ {df['faturamento'].mean():.2f}")


st.subheader("📈 Evolução das Vendas")
df_time = df.groupby("data")["faturamento"].sum()
st.line_chart(df_time)

st.subheader("🏆 Top Produtos")
top_prod = df.groupby("nome")["quantidade"].sum().sort_values(ascending=False)
st.bar_chart(top_prod.head(10))