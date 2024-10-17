import sys
import os
import main


print("Installation des modules pour mon tool:")


if sys.platform.startswith("win"):
    os.system("pip install -r requirements.txt")
    os.system("python main.py")

elif sys.platform.startswith("linux"):
    os.system("python3 -m pip3 install -r requirements.txt")
    os.system("python3 main.py")



