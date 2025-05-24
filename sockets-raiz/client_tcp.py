import socket
import time

HOST = '127.0.0.1'  
PORT = 9000      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Conectado ao servidor TCP Python em {HOST}:{PORT}.\nPressione Ctrl+C para sair.')

    message = "Olá, servidor!"
    s.sendall(message.encode('utf-8'))
    
    try:
        while True:
            msg = input("Digite mensagem (ou 'sair'): ")
            if msg == 'sair':
                break
            s.sendall(msg.encode('utf-8'))

    except KeyboardInterrupt:
        print('Desconectando...')
