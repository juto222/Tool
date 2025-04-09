#!/bin/bash

echo "Installation des modules pour mon tool:"

python3 -m venv Tool

source Tool/bin/activate


python3 -m pip install --upgrade pip

# Installation des packages
pip install dnspython python-nmap auto-py-to-exe aiohttp requests pyautogui


echo -e "EN CAS D'ERREUR DE LIBRAIRIE, REINSTALLER LES MANNUELLEMENT JUSQU'À QUE ÇA MARCHE !!!!!"

echo -e "\n\nInstallation finie ! Vous pouvez lancer main.py"
echo -e 'Pensez à faire "deactivate" à la fin de votre utilisation.'
