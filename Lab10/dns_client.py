import socket

# Configurações do cliente DNS
host = "192.168.4.13"
port = 1234

# Criação do socket do cliente
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicita ao usuário o nome do destinatário
    nome_destinatario = input("Digite o nome do destinatário: ").lower()

    # Envia o nome do destinatário ao servidor DNS
    sock.sendto(nome_destinatario.encode(), (host, port))

    # Recebe a resposta do servidor DNS
    endereco_ip, endereco_dns = sock.recvfrom(1024)
    endereco_ip = endereco_ip.decode()

    # Verifica se o endereço IP foi encontrado ou não
    if endereco_ip != "Nome não encontrado na tabela DNS":
        print(f"Endereço IP do destinatário: {endereco_ip}")

        # Envia mensagens para o destinatário usando o endereço IP
        destinatario_porta = 60500  # Porta do destinatário (exemplo: 60500)
        mensagem = input("Digite a mensagem para enviar: ")
        sock.sendto(mensagem.encode(), (endereco_ip, destinatario_porta))
    else:
        print("Nome não encontrado na tabela DNS")
