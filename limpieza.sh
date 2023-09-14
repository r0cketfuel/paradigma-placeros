#!/bin/bash

cd apps

# Elimina todas las migraciones que coincidan con el patrón "nnnn_nombre.py"
find . -name '????_*.py' -delete

cd ..