#!/bin/bash

#==========================================================#
# Función para imprimir una "✔" en verde o una "✘" en rojo #
#==========================================================#
function print_checkbox {
    if [ "$1" = "true" ]; then
        echo -e "[\e[32m✔\e[0m] $2"
    else
        echo -e "[\e[31m✘\e[0m] $2"
    fi
}

#==========================================================#
# Función para verificar si una dependencia está instalada #
#==========================================================#
function check_dependency {
    command -v "$1" &>/dev/null
}

python_installed=false
pip_installed=false
virtualenv_installed=false

clear
echo "Comprobación de dependencias..."
echo ""

# Verificar si Python está instalado
if check_dependency "python3"; then
    python_installed=true
fi

# Verificar si Virtualenv está instalado
if check_dependency "virtualenv"; then
    virtualenv_installed=true
fi

# Verificar si Pip está instalado
if check_dependency "pip"; then
    pip_installed=true
fi

# Imprimir los resultados
print_checkbox "$python_installed" "Python"
print_checkbox "$pip_installed" "pip"
print_checkbox "$virtualenv_installed" "virtualenv"

echo ""

# Comprobar si falta alguna dependencia
if $python_installed && $pip_installed && $virtualenv_installed; then

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

fi