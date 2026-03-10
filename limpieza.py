import pandas as pd

# Carga de datos
ventas = pd.read_csv("dataset.txt")
tiendas = pd.read_csv("stores.txt")

#Revisión de tipos de datos
print(ventas.info())
print(tiendas.info())

#Creación de nueva tabla con variables identificadas
data_ventas = ventas[["Store ID", "Total Price", "Base Price", "Units Sold", "Month", "Year"]]
data_tiendas = tiendas[["Store ID", "Nombre", "Distrito ID", "Distrito"]]

#Creación de una nueva variable
#Calculamos el 'Descuento'
data_ventas["Descuento"] = data_ventas["Base Price"] - data_ventas["Total Price"]

#Verificación de nulos
print(data_ventas.isnull().sum())
print(data_tiendas.isnull().sum())

# Eliminar filas con valores nulos
data_ventas = data_ventas.dropna()

# Convertir Store ID a entero
data_ventas["Store ID"] = data_ventas["Store ID"].astype(int)

# Revisar nuevamente los datos
print("\nDespués de limpieza:")
print(data_ventas.info())

# MERGE DE TABLAS

data_final = pd.merge(data_ventas, data_tiendas, on="Store ID", how="left")

print(data_final.head())

# Exportar a CSV
data_final.to_csv("data_consolida.csv", index=False)