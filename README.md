# Sockets e WebSockets (Python & Node.js)

Este repositório demonstra, de forma didática e prática, como funcionam as comunicações em rede usando **sockets** e **WebSockets** em Python e JavaScript (Node.js).

---

## O que é um Socket?

Um **socket** é uma "porta virtual" que permite a comunicação entre dois programas (cliente e servidor), seja na mesma máquina ou em computadores diferentes, através da rede. Ele é a base para a troca de dados em tempo real na internet, sendo utilizado em protocolos como TCP e UDP.

- **Exemplo de uso:** chats, jogos online, transferência de arquivos, sistemas de monitoramento, etc.

---

## Diferença entre Socket e WebSocket

| Característica     | Socket TCP (puro)                | WebSocket                             |
| ------------------ | -------------------------------- | ------------------------------------- |
| Protocolo          | TCP (camada de transporte)       | TCP + Protocolo WebSocket (aplicação) |
| Comunicação        | Bidirecional, mas sem padrão web | Bidirecional, padrão web              |
| Uso em navegadores | Não (direto)                     | Sim (nativo em JS/browser)            |
| Handshake          | Simples (TCP)                    | Handshake HTTP especial               |
| Persistência       | Sim                              | Sim                                   |
| Aplicações         | Sistemas customizados, IoT, etc. | Chats web, jogos web, notificações    |

- **Socket TCP puro:** Comunicação de baixo nível, ideal para aplicações customizadas, geralmente fora do navegador.
- **WebSocket:** Protocolo de alto nível, criado para comunicação em tempo real na web, suportado nativamente por navegadores e frameworks modernos.

---

## Estrutura do Repositório

```
sockets-raiz/
  server_tcp.py      # Servidor TCP puro em Python
  client_tcp.py      # Cliente TCP puro em Python
  server_tcp.js      # Servidor TCP puro em Node.js
  client_tcp.js      # Cliente TCP puro em Node.js

websockets/
  python/
    server.py        # Servidor WebSocket em Python
    client.py        # Cliente WebSocket em Python
  js/
    server.js        # Servidor WebSocket em Node.js
    client.js        # Cliente WebSocket em Node.js
```

---

## Como usar

Cada subdiretório possui um README próprio com instruções detalhadas para rodar os exemplos em Python e Node.js, tanto para sockets puros quanto para WebSockets.

- Para sockets puros, não é necessário instalar bibliotecas externas.
- Para WebSockets, instale as dependências indicadas nos READMEs das pastas `python` e `js`.

---

## Por que aprender sobre Sockets e WebSockets?

- **Sockets** são a base da comunicação em rede, usados em sistemas embarcados, servidores de jogos, automação, etc.
- **WebSockets** permitem comunicação em tempo real na web, essenciais para chats, dashboards, jogos multiplayer, notificações e muito mais.

Entender ambos te dá flexibilidade para criar aplicações robustas, eficientes e modernas!

---

## Referências úteis

- [Documentação Python socket](https://docs.python.org/3/library/socket.html)
- [Documentação Node.js net](https://nodejs.org/api/net.html)
- [Documentação WebSocket (MDN)](https://developer.mozilla.org/pt-BR/docs/Web/API/WebSocket)
- [RFC 6455 - The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455)

---

> Sinta-se à vontade para explorar, modificar e experimentar os exemplos deste repositório!
