import pandas as pd
import sqlite3

df = pd.read_csv('omega_bruto.csv', sep=r'\s+', comment='#', skiprows=[1, 2])

cols_validas = ['Source', 'RA_ICRS', 'DE_ICRS', 'pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag']
df = df[cols_validas]

# Que tome los datos que son numeros
for col in ['pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Datos limpios
df_limpio = df.dropna(subset=['pmRA', 'pmDE', 'Gmag', 'BPmag', 'RPmag'])

conn = sqlite3.connect('arqueologia.db')
df_limpio.to_sql('estrellas', conn, if_exists='replace', index=False)
conn.close()

print("Se migraron bien los datos.")
