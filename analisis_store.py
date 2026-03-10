import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
ventas = pd.read_csv("dataset.txt")
tiendas = pd.read_csv("stores.txt")

#Unir ambas tablas por 'Store ID'
data = pd.merge(ventas, tiendas, on="Store ID")

#Asiganación de variables para filtración
filtro_month = "Enero"
filtro_year = 2016
filtro_distrito = "SURCO"

#Filtración de variables por mes y año
ventas_filtro = data[(data["Month"] == filtro_month) & (data["Year"] == filtro_year) & (data["Distrito"] == filtro_distrito)]

#Ventas promedio por tienda
plt.figure(figsize=(12, 6))
sns.barplot(data=ventas_filtro, x="Store ID", y="Units Sold", estimator='mean', palette=["fuchsia", "yellow"])
plt.title("Ventas Promedio por Tienda")
plt.show()