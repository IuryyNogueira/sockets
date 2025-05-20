import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 9000         # Porta do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # Associa o socket ao endereço e porta
    s.listen() # Coloca o socket em modo de escuta

    print(f'Servidor TCP Python rodando em {HOST}:{PORT}')
    while True:
        conn, addr = s.accept() # Aceita conexão
        print(f'Cliente conectado: {addr}')
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
        except Exception as e:
            print('Erro:', e)
        finally:
            print(f'Cliente desconectado: {addr}')
            conn.close()
