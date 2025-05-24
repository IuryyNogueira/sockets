import socket
import selectors

HOST = '127.0.0.1'
PORT = 9000

sel = selectors.DefaultSelector()

def aceitar_conexao(sock):
    conn, addr = sock.accept()
    print(f"Cliente conectado: {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, ler_cliente)

def ler_cliente(conn):
    try:
        data = conn.recv(1024)
        if data:
            print(f"Recebido de {conn.getpeername()}: {data.decode('utf-8')}\n")
        else:
            print(f"Cliente desconectado: {conn.getpeername()}")
            sel.unregister(conn)
            conn.close()
    except Exception as e:
        print(f"Erro com {conn.getpeername()}: {e}")
        sel.unregister(conn)
        conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORT))
    servidor.listen()
    servidor.setblocking(False) # Define o socket como não bloqueante

    
    sel.register(servidor, selectors.EVENT_READ, aceitar_conexao)

    print(f"Servidor TCP com selectors rodando em {HOST}:{PORT}\n")

    # Loop principal do servidor
    while True:
        eventos = sel.select(timeout=None)
        for chave, mascara in eventos:
            callback = chave.data  # Pode ser aceitar_conexao ou ler_cliente
            callback(chave.fileobj)
