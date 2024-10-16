import nmap

nm = nmap.PortScanner()


def scan_network():

    print(r"""
                    _      ______          ______  
                   | |    / _____)   /\   |  ___ \ 
                    \ \  | /        /  \  | |   | |
                     \ \ | |       / /\ \ | |   | |
                 _____) )| \_____ | |__| || |   | |
                (______/  \______)|______||_|   |_|
          




                                   
""")
    print("********************************Bienvenue dans le scanner de réseau******************************")
    ip = input("Entrez l'adresse IP ou domaine à scanner : ")
    port_range = input("Entrez la plage de ports à scanner (ex: 0-1024) : ")

    print(f"Scanning {ip} sur les ports {port_range}...")
    nm.scan(ip, port_range)

    for host in nm.all_hosts():
        print(f"Host : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f'----------\nProtocole : {proto}')
            lport = nm[host][proto].keys()
            for port in lport:
                print(f'Port : {port}\tState : {nm[host][proto][port]["state"]}')