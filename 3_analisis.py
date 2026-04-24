import pandas as pd
import sqlite3
import matplotlib.pyplot as plt 

conn = sqlite3.connect('arqueologia.db')

# Se seleccionan las necesarias
df = pd.read_sql("SELECT pmRA, pmDE FROM estrellas", conn)

# Gráfica 1
plt.figure(figsize=(6,6))
plt.scatter(df['pmRA'], df['pmDE'], s=0.1 , color='black', alpha=0.8)
plt.xlabel('pmRA')
plt.ylabel('pmDE')
plt.title('Movimiento propio')
plt.xlim(-15,10)
plt.ylim(-15,15)
plt.savefig('Gráfica_1.png')
print("Se guardo la gráfica como 'Gráfica_1.png'")
plt.show()


# Filtro
# Nuevo query
query = """
SELECT *
FROM estrellas
WHERE pmRA BETWEEN -6 AND -2
AND pmDE BETWEEN -9 AND -5
"""

df_cumulo = pd.read_sql(query, conn)
conn.close()

print(f"Estrellas del cúmulo: {len(df_cumulo)}")

# Gráfica 2

# índice de color
df_cumulo['color'] = df_cumulo['BPmag'] - df_cumulo['RPmag']

plt.figure(figsize=(6,8))
plt.scatter(df_cumulo['color'], df_cumulo['Gmag'], s=1, alpha=0.6)

plt.xlabel('BP - RP (Color)')
plt.ylabel('Gmag')
plt.title('Diagrama Color-Magnitud - Omega Centauri')

# Se invierte el eje y
plt.gca().invert_yaxis()
plt.savefig('Gráfica_2.png')
plt.show()
print("Se guardo la gráfica como 'Gráfica_2.png'")
