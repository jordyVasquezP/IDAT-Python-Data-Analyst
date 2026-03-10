import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
ventas = pd.read_csv("dataset.txt")
tiendas = pd.read_csv("stores.txt")

#Asiganación de variables para filtración
filtro_month = "Enero"
filtro_year = 2016

#Filtración de variables por mes y año
ventas_enero = ventas[(ventas["Month"] == filtro_month) & (ventas["Year"] == filtro_year)]

#Gráfico de dispersión: Precio vs Unidades Vendidas
plt.figure(figsize=(10, 6))
sns.scatterplot(data=ventas_enero, x="Total Price", y="Units Sold")
plt.title(f"Relación entre Precio Total y Unidades Vendidas en {filtro_month} {filtro_year}")
plt.xlabel("Precio Total")
plt.ylabel("Unidades Vendidas")
plt.show()