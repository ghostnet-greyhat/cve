#!/bin/bash

# Pide al usuario que ingrese el CVE o el nombre del exploit a buscar
read -p "Ingrese el CVE o el nombre del exploit que desea buscar: " vuln

# Define la URL de la base de datos
url="https://api.cve.mitre.org/api/iiq?"

# Envía una solicitud GET a la API de la base de datos con la consulta de búsqueda
response=$(curl -s "$url""search=$vuln")

# Verifica si la solicitud fue exitosa y si hay resultados
if [ "$(echo "$response" | jq -r '.results | length')" -gt 0 ]; then
    # Muestra los resultados de la búsqueda
    echo "$response" | jq -r '.results[] | "CVE ID: \(.id)\nDescripción: \(.description)\nReferencias: \(.references | join(", "))\nSeverity: \(.severity)\n------------------------"'
else
    echo "No se encontraron resultados para su consulta."
fi
