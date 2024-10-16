import ipaddress

def convertir():

    print(r"""
                          __                             ______   ______   ______   __ 
                         /  |                  _  _     / __   | / __   | / __   | /  |
                        /_/ |   ___  ___  ___ ( \( \   | | //| || | //| || | //| |/_/ |
                          | |  (___)(___)(___) ) )) )  | |// | || |// | || |// | |  | |
                          | |                 (_/(_/   |  /__| ||  /__| ||  /__| |  | |
                          |_|                           \_____/  \_____/  \_____/   |_|
          


      

                                                               
    """)
    ipv6_hex = input("Entrez une adresse IPv6 en hexadécimal (ex: 20010db8000000000000000000000001) : ")

    try:
        ipv6_normal = ipaddress.IPv6Address(ipv6_hex)
        print("Adresse IPv6 au format normal :", ipv6_normal)
    except ValueError:
        print("Erreur : Adresse IPv6 invalide.")

