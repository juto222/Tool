import random

def generate_ipv6():
    ip1 = random.randint(0,255)
    ip2 = random.randint(0,255)
    ip3 = random.randint(0,255)
    ip4 = random.randint(0,255)
    print(f"Votre nouvelle ip généré est {ip1}.{ip2}.{ip3}.{ip4}")