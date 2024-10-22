import sys
import os

print("Installation des modules pour mon tool:")


if sys.platform.startswith("win"):
    os.system("pip install dnspython")
    os.system("pip install nmap")
