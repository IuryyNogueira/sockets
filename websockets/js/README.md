# WebSockets JavaScript (Node.js)

Este diretório contém um exemplo de servidor e cliente WebSocket em Node.js.

## Requisitos

- Node.js
- Biblioteca `ws`

## Instalação

```bash
npm install
```

## Como usar

### Servidor

```bash
node server.js
```

### Cliente

Em outro terminal:

```bash
node client.js
```

O cliente permanecerá conectado até você pressionar Ctrl+C.

---

O servidor exibirá mensagens quando clientes conectarem ou desconectarem, e atribuirá uma letra do alfabeto para cada cliente.
