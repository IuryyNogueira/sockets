# Sockets TCP puros (Python e Node.js)

Este diretório contém exemplos simples de servidor e cliente TCP usando apenas sockets, sem WebSocket.

## Arquivos

- `server_tcp.py` — Servidor TCP em Python
- `client_tcp.py` — Cliente TCP em Python
- `server_tcp.js` — Servidor TCP em Node.js
- `client_tcp.js` — Cliente TCP em Node.js

## Como usar

### Python

1. Abra um terminal e navegue até a pasta `sockets-raiz`:
   ```bash
   cd ~/sockets/sockets-raiz
   ```
2. Inicie o servidor:
   ```bash
   python3 server_tcp.py
   ```
3. Em outro terminal, inicie o cliente:
   ```bash
   python3 client_tcp.py
   ```

### Node.js

1. Abra um terminal e navegue até a pasta `sockets-raiz`:
   ```bash
   cd ~/sockets/sockets-raiz
   ```
2. Inicie o servidor:
   ```bash
   node server_tcp.js
   ```
3. Em outro terminal, inicie o cliente:
   ```bash
   node client_tcp.js
   ```

## O que acontece?

- O servidor mostra no terminal quando um cliente conecta e desconecta.
- O cliente permanece conectado até você pressionar `Ctrl+C`.

## Observações

- Os exemplos usam o endereço `127.0.0.1` (localhost) e a porta `9000` por padrão.
- Você pode rodar clientes e servidores Python e Node.js ao mesmo tempo, se quiser.
- Não é necessário instalar bibliotecas externas para os exemplos TCP puros.
