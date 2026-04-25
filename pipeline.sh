#!/bin/bash

echo "Descarga de datos"

bash 1_descarga_omega.sh

echo "Creando base de datos"
python3 2_crear_db.py

echo "Análisis y visualización de las gráficas"
python3 3_analisis.py

echo "Todo se ha ejecutado correctamente"
