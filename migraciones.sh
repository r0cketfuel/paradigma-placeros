#!/bin/bash

# Elimina todas las migraciones que coincidan con el patrón "nnnn_nombre.py"
cd apps
find . -name '????_*.py' -delete

cd ..