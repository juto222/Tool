#!/bin/bash

echo "Installation des modules pour mon tool :"

# Vérifier si python3 est disponible
if ! command -v python3 &> /dev/null
then
    echo "Python3 n'est pas installé. Veuillez installer Python3 avant de continuer."
    exit 1
fi

# environnement virtuel
python3 -m venv Tool

# Activer l'environnement virtuel
source Tool/bin/activate

# Mettre à jour pip
python3 -m pip install --upgrade pip

# Installation des packet nécessaires
PACKAGES=("dnspython" "python-nmap" "auto-py-to-exe" "aiohttp" "requests" "pyautogui" "webbrowser")

for PACKAGE in "${PACKAGES[@]}"
do
    echo "Installation de $PACKAGE..."
    pip install "$PACKAGE"
    if [ $? -ne 0 ]; then
        echo "Erreur lors de l'installation de $PACKAGE. Vous pouvez essayer de le réinstaller manuellement."
        exit 1
    fi
done

echo -e "EN CAS D'ERREUR DE LIBRAIRIE, REINSTALLER LES MANNUELLEMENT JUSQU'À QUE ÇA MARCHE !!!!!"

echo -e "\n\nInstallation terminée ! Vous pouvez lancer main.py"
echo -e 'Pensez à faire "deactivate" à la fin de votre utilisation.'
