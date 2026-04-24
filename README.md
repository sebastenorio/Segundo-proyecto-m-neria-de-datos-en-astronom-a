# Arqueología Galáctica y el Misterio de Omega Centauri

Omega Centauri no es un cúmulo globular ordinario. Existe evidencia científica de que podría ser el **núcleo remanente de una galaxia enana** que la Vía Láctea "devoró" hace miles de millones de años. 

El objetivo de este proyecto es actuar como un "arqueólogo galáctico", utilizando el movimiento propio para separar las estrellas que realmente pertenecen al cúmulo de aquellas que pertenecen al disco de nuestra galaxia y que solo están ahí de fondo visualmente.

---

## Datos de Localización
Para centrar la búsqueda, utilicé las coordenadas precisas obtenidas a través de la interfaz de **SIMBAD**:

| Parámetro | Valor Original (HMS/DMS) | Grados Decimales |
| :--- | :--- | :--- |
| **RA (Ascensión Recta)** | 13h 26m 47.28s | **201.69699°** |
| **DEC (Declinación)** | -47° 28' 46.1" | **-47.47947°** |

---

## Metodología

### 1. Descarga de Datos
Utilicé un script en Bash (`1_descarga_omega.sh`) para realizar una consulta ADQL al catálogo **Gaia DR3** mediante el endpoint de VizieR. Se extrajo un radio de 0.5° con las siguientes columnas clave: `Source`, `RA_ICRS`, `DE_ICRS`, `pmRA`, `pmDE`, `Gmag`, `BPmag`, `RPmag`.

### 2. Limpieza y Base de Datos (SQL & Python)
Debido a que los datos astronómicos suelen venir con caracteres especiales, el script `2_crear_db.py` realizó lo siguiente:
* Limpieza de metadatos y líneas decorativas del archivo.
* Conversión de datos a formato numérico (`float`).
* Eliminación de filas nulas.
* Almacenamiento en una base de datos **SQLite** (`arqueologia.db`).

### 3. Análisis
El punto clave fue graficar el **Movimiento Propio** (`pmRA` vs `pmDE`). Al hacerlo, se identificó un "racimo" muy denso desplazado del origen (0,0), lo que confirma que el cúmulo se mueve como un enjambre unido. Para aislarlo, apliqué el siguiente filtro SQL:

```sql
SELECT * FROM estrellas 
WHERE pmRA BETWEEN -6 AND -2 
AND pmDE BETWEEN -9 AND -5
```
---

## Resultados

### Gráfica 1: Identificación de la Población
En esta gráfica de dispersión identifiqué el movimiento de Omega Centauri separado del fondo galáctico. El punto denso representa las estrellas ligadas gravitacionalmente al cúmulo.

![Gráfica de Movimiento Propio]

### Gráfica 2: Diagrama HR (Color-Magnitud)
Con las estrellas filtradas, calculé el índice de color ($BP - RP$) y grafiqué la Magnitud G invertida. El resultado es un diagrama mucho más limpio donde se distinguen las fases evolutivas de las estrellas del cúmulo.

![Diagrama Color-Magnitud]

---

## 🧠 Conclusión
El movimiento propio es una herramienta fundamental para la arqueología galáctica. Gracias a este filtro, logré aislar Omega Centauri y obtener un diagrama estelar coherente, demostrando que este objeto es efectivamente una población estelar distinta a la de la Vía Láctea, consistente con la teoría de su origen como galaxia enana capturada.

---

## Herramientas
* **Python:** Pandas, Matplotlib, Sqlite3.
* **Bash:** Wget.
* **Catálogos:** Gaia DR3, VizieR, SIMBAD.

---

## Declaración de Uso de IA
Para este proyecto utilicé herramientas de IA como apoyo técnico en la resolución de errores de lectura de datos (parseo de archivos con espacios variables) y en la optimización de los scripts de graficación. La interpretación científica de los resultados y la lógica de los filtros SQL fueron desarrolladas de manera consciente como parte del proceso de aprendizaje.