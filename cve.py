#!/usr/bin/env python3

import os
import requests
import json

# Limpia la pantalla de la terminal
os.system("clear")

# Pide al usuario que ingrese el CVE o el nombre del exploit a buscar
vuln = input("Ingrese el CVE o el nombre del exploit que desea buscar: ")

# Define la URL de la base de datos
url = "https://api.cve.mitre.org/api/iiq?"

# Envía una solicitud GET a la API de la base de datos con la consulta de búsqueda
response = requests.get(url + "search=" + vuln)

# Verifica si la solicitud fue exitosa y si hay resultados
if response.status_code == 200 and response.json():
    # Muestra los resultados de la búsqueda
    results = response.json()["results"]
    for result in results:
        print("CVE ID: " + result["id"])
        print("Descripción: " + result["description"])
        print("Referencias: " + ", ".join(result["references"]))
        print("Severity: " + result["severity"])
        print("------------------------")
else:
    print("No se encontraron resultados para su consulta.")
