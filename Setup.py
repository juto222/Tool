import os
import subprocess
import sys
import platform

import subprocess
import os

def install_python_windows():
    try:
        # Vérifie si winget est installé
        subprocess.run("winget --version", check=True, shell=True)
        print("Winget est disponible, installation de Python en cours...")
        
        # Installer Python avec winget
        subprocess.run("winget install Python.Python.3", shell=True)
        print("Python a été installé avec succès.")

    except subprocess.CalledProcessError:
        print("Winget n'est pas disponible. Assurez-vous que Winget est installé ou utilisez un autre outil comme Chocolatey.")

if __name__ == "__main__":
    install_python_windows()


def add_python_to_path():
    python_path = sys.executable
    path_variable = os.environ['PATH']

    if python_path not in path_variable:
        subprocess.run(f'setx PATH "{path_variable};{python_path}"', shell=True)
        print("Python a été ajouté au PATH.")
    else:
        print("Python est déjà dans le PATH.")

if __name__ == "__main__":
    add_python_to_path()


def install_nmap():
    os_system = platform.system()
    
    if os_system == "Windows":
        print("Installation de Nmap pour Windows...")
        subprocess.run("winget install Nmap.Nmap", shell=True)  # Assurez-vous que winget est installé
    elif os_system == "Linux":
        print("Installation de Nmap pour Linux...")
        subprocess.run("sudo apt-get install nmap -y", shell=True)
    elif os_system == "Darwin":
        print("Installation de Nmap pour macOS...")
        subprocess.run("brew install nmap", shell=True)  # Si Homebrew est installé

    print("Nmap installé avec succès !")

if __name__ == "__main__":
    install_nmap()


print("Installation des modules pour mon tool:")

os.system("pip install dnspython")
os.system("pip install python-nmap")
