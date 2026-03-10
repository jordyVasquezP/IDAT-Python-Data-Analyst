import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Carga de datos
ventas = pd.read_csv("dataset.txt")
tiendas = pd.read_csv("stores.txt")

# Selección de variables
data_ventas = ventas[["Store ID", "Total Price", "Base Price", "Units Sold", "Month", "Year"]].copy()
data_tiendas = tiendas[["Store ID", "Nombre", "Distrito ID", "Distrito"]].copy()

# Crear variable descuento
data_ventas["Descuento"] = data_ventas["Base Price"] - data_ventas["Total Price"]

# Limpiar nulos
data_ventas = data_ventas.dropna()
data_tiendas = data_tiendas.dropna()

# Convertir tipo
data_ventas["Store ID"] = data_ventas["Store ID"].astype(int)
data_tiendas["Store ID"] = data_tiendas["Store ID"].astype(int)

# Unir tablas
data_final = pd.merge(data_ventas, data_tiendas, on="Store ID", how="left")

# Mapear meses a números
meses = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Setiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12
}
data_final["Month"] = data_final["Month"].map(meses)

# Variables predictoras y variable objetivo
X = data_final[["Base Price", "Total Price", "Descuento", "Month", "Year", "Distrito ID"]]
y = data_final["Units Sold"]

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicción
y_pred = modelo.predict(X_test)

# Evaluación
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Simulación de escenario 1 - sin descuento
escenario_1 = pd.DataFrame([{
    "Base Price": 20,
    "Total Price": 20,
    "Descuento": 0,
    "Month": 3,
    "Year": 2026,
    "Distrito ID": 29
}])
prediccion_1 = modelo.predict(escenario_1)
print("Escenario 1 - Marzo 2026 (Sin descuento):")
print("Unidades estimadas a vender:", prediccion_1[0])

# Simulación de escenario 2 - 10% de descuento
escenario_2 = pd.DataFrame([{
    "Base Price": 20,
    "Total Price": 18,
    "Descuento": 2,
    "Month": 3,
    "Year": 2026,
    "Distrito ID": 29
}])
prediccion_2 = modelo.predict(escenario_2)
print("Escenario 2 - Marzo 2026 (10% de descuento):")
print("Unidades estimadas a vender:", prediccion_2[0])

# Simulación de escenario 3 - 20% de descuento
escenario_3 = pd.DataFrame([{
    "Base Price": 20,
    "Total Price": 16,
    "Descuento": 4,
    "Month": 3,
    "Year": 2026,
    "Distrito ID": 29
}])
prediccion_3 = modelo.predict(escenario_3)
print("Escenario 3 - Marzo 2026 (20% de descuento):")
print("Unidades estimadas a vender:", prediccion_3[0])