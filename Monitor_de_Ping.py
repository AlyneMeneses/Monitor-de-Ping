
import socket
import ping3

def verificar_site(url):
    try: 
        # Obtendo o IP do site
        ip = socket.gethostbyname(url)
        print(f"Pingando {url} ({ip})...")

        # Enviando ping
        resposta = ping3.ping(ip, timeout=2)

        if resposta is not None:
            print(f"✅ Site online! Tempo de resposta: {round(resposta * 1000, 2)} ms")
        else:
            print("❌ O site não respondeu ao ping.")
    except Exception as e:
        print(f"Erro: {e}")

# Entrada do usuário
site = input("Digite a URL do site (ex: google.com): ")
verificar_site(site)
