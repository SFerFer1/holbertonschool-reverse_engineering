#!/bin/bash

# 1. El nombre del archivo viene por argumento
file_name=$1

# 2. Validaciones básicas
if [ -z "$file_name" ]; then
    echo "Usage: $0 <elf_file>"
    exit 1
fi

if [ ! -f "$file_name" ]; then
    echo "Error: File '$file_name' not found."
    exit 1
fi

# 3. Extraer la información en las variables que espera messages.sh
magic_number=$(readelf -h "$file_name" | grep "Magic:" | sed 's/Magic://' | xargs)
class=$(readelf -h "$file_name" | grep "Class:" | awk '{print $2}')
# Tomamos el byte order limpiando la coma
byte_order=$(readelf -h "$file_name" | grep "Data:" | awk -F', ' '{print $2}')
entry_point_address=$(readelf -h "$file_name" | grep "Entry point address:" | awk '{print $4}')

# 4. Importar las funciones y ejecutar
source ./messages.sh

# Llamamos a la función sin pasarle parámetros, porque usa las variables globales
display_elf_header_info
