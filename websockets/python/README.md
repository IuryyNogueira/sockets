# WebSockets Python

Este diretório contém um exemplo de servidor e cliente WebSocket em Python.

## Requisitos

- Python 3.7+
- Biblioteca `websockets`

## Instalação

```bash
source venv/bin/activate
```

```bash
pip install websockets
```

## Como usar

### Servidor

```bash
python3 server.py
```

### Cliente

Em outro terminal:

```bash
python3 client.py
```

O cliente permanecerá conectado até você pressionar Ctrl+C.

---

O servidor exibirá mensagens quando clientes conectarem ou desconectarem.
