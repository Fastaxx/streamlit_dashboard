import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Analyse Ventes")

df = pd.read_csv("Sales Data.csv",index_col="Order ID")
del df["Unnamed: 0"]

## --Sidebar--

st.sidebar.header("Filtres")
city = st.sidebar.multiselect(
	"Selectionner la ville",
	options=df["City"].unique(),
	default=df["City"].unique())

product = st.sidebar.selectbox(
	"Selectionner le produit",
	options=df["Product"].unique())

df_selection = df.query(
	"City == @city & Product == @product")

## --KPI--
total_sales = int(df_selection["Sales"].sum())
average_sale_by_transaction = round(df_selection["Sales"].mean(), 2)

#st.dataframe(df_selection)
st.markdown("""Key Metrics""")

kpi1, kpi2 = st.columns(2)

kpi1.metric(label=f"Ventes Totales de {product}",
			value=total_sales,
			delta=None)

kpi2.metric(label="Ventes moyennes par transaction",
			value=average_sale_by_transaction,
			delta=None)

## --Sales par heures--
sales_by_hour = df_selection.groupby(by="Hour").sum()["Sales"]
st.write(sales_by_hour)
fig_heure_vente= px.bar(
	sales_by_hour,
	x=sales_by_hour,
	y="Sales",
	title="<b>Ventes par heure</b>",
	)


#st.plotly_chart(fig_heure_vente)




