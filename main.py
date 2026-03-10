import pandas as pd

ventas = pd.read_csv("stores.txt")

# cantidad_unica =ventas["Store ID"].nunique()

print(ventas.info())
