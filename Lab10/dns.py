import socket

# Tabela de mapeamento de nomes para endereços IP
tabela_dns = {
    "alice": "192.168.0.100",
    "bob": "192.168.0.101",
    "charlie": "192.168.0.102"
}

# Configurações do servidor DNS
host = "192.168.4.13"
port = 1234

# Criação do socket do servidor
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print("Servidor DNS rodando...")

while True:
    # Recebe o nome do cliente
    nome_cliente, endereco_cliente = sock.recvfrom(1024)
    nome_cliente = nome_cliente.decode().lower()

    # Verifica se o nome está na tabela DNS
    if nome_cliente in tabela_dns:
        endereco_ip = tabela_dns[nome_cliente]
        sock.sendto(endereco_ip.encode(), endereco_cliente)
        print(f"Endereço IP enviado para o cliente: {endereco_ip}")
    else:
        sock.sendto("Nome não encontrado na tabela DNS".encode(), endereco_cliente)
        print("Nome não encontrado na tabela DNS")
