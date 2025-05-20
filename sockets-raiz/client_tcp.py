import socket
import time

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 9000         # Porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Conectado ao servidor TCP Python em {HOST}:{PORT}.\nPressione Ctrl+C para sair.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Desconectando...')
