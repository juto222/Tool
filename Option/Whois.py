import whois

def info_domaine():
    domain = input("Entrez le domaine à analyser : ")
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return str(e)
    info = info_domaine(domain)

    print(info)
