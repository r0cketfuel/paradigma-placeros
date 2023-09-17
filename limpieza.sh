#!/bin/bash

# Eliminar docker
cd docker
docker-compose down -v
cd ..

# Elimina todas las migraciones que coincidan con el patrón "nnnn_nombre.py"
cd apps
find . -name '????_*.py' -delete

cd ..
cd data
sudo rm -r db
cd ..

# Creación docker
cd docker
# docker-compose -f docker-compose-dev.yml up --build
docker-compose up --build -d
cd ..