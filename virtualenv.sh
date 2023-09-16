#!/bin/bash

# Creación del entorno virtual Python
virtualenv venv

# Activación del entorno virtual Python
source venv/bin/activate

if [ -n "$VIRTUAL_ENV" ]; then
    # Instalación de dependencias
    cd docker
    pip install -r requirements.txt
    cd ..
else
    echo "Error al activar entorno virtual de Python"
fi
