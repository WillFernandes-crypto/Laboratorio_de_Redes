import random
import time
from socket import *

# Endereço do servidor e porta
serverAddress = ('127.0.0.1', 50000)

# Número de pings a enviar
numPings = 10

# Cria o socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define o tempo limite para 1 segundo
clientSocket.settimeout(2)

# Contadores para estatísticas
sentPings = 0
receivedPings = 0

# Lista para armazenar os tempos de RTT
rttTimes = []

# Envia os pings
while sentPings < numPings:
    # Incrementa o número de sequência
    sequenceNumber = sentPings + 1

    # Obtém o tempo atual
    sentTime = time.time()

    # Formata a mensagem do ping
    message = f'Ping {sequenceNumber} {sentTime}'

    try:
        # Envia a mensagem para o servidor
        clientSocket.sendto(message.encode(), serverAddress)

        # Recebe a resposta do servidor
        response, _ = clientSocket.recvfrom(1024)


        # Obtém o tempo de recebimento
        receivedTime = time.time()

        # Calcula o tempo de RTT
        rtt = receivedTime - sentTime
        rttTimes.append(rtt)

        # Incrementa o número de pacotes recebidos
        receivedPings += 1

        # Imprime a resposta do servidor
        print(response.decode())

    except timeout:
        # Se ocorrer um timeout, considera o pacote perdido
        print('Request timeout')

    # Incrementa o número de pacotes enviados
    sentPings += 1

# Fecha o socket do cliente
clientSocket.close()

# Cálculos finais
if receivedPings > 0:
    minRtt = min(rttTimes)
    maxRtt = max(rttTimes)
    avgRtt = sum(rttTimes) / len(rttTimes)
    packetLossRate = (1 - receivedPings / numPings) * 100

    print(f'\nPing statistics:')
    print(f'  Packets sent: {numPings}')
    print(f'  Packets received: {receivedPings}')
    print(f'  Packet loss rate: {packetLossRate:.2f}%')
    print(f'  Minimum RTT: {minRtt:.6f} seconds')
    print(f'  Maximum RTT: {maxRtt:.6f} seconds')
    print(f'  Average RTT: {avgRtt:.6f} seconds')
else:
    print('No packets received.')
