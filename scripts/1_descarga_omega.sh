#!/bin/bash

# Coordenadas de SIMBAD
RA=201.69699
DEC=-47.47947
RADIUS=0.5

echo "Iniciando descarga de datos..."

# Se filtran las columnas
URL="https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=I/355/gaiadr3&-c=${RA}${DEC}&-c.rd=${RADIUS}&-out=Source,RA_ICRS,DE_ICRS,pmRA,pmDE,Gmag,BPmag,RPmag&-out.max=100000"

wget -O omega_bruto.csv "$URL"

echo "Se descargaron correctamente"
