const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });

// Alfabeto para atribuir aos clientes
const alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
const availableletra = [...alfabeto];
const clientletra = new Map(); // ws -> letra

// Evento disparado quando um cliente se conecta
wss.on("connection", function connection(ws, req) {
  // Atribui uma letra disponível ao cliente
  let id = availableletra.shift();
  if (!id) {
    id = "?"; // Caso acabem as letras
  }
  clientletra.set(ws, id);

  // Obtém o endereço do cliente
  const clientAddress = req.socket.remoteAddress + ":" + req.socket.remotePort;
  console.log(`Cliente conectado: ${clientAddress} (id: ${id})`);

  // Quando o cliente desconecta
  ws.on("close", function close() {
    console.log(`Cliente desconectado: ${clientAddress} (id: ${id})`);
    // Libera a letra para outro cliente
    if (id !== "?") 
    {
      availableletra.push(id);
      // Mantém a ordem das letras
      availableletra.sort();
    }
    clientletra.delete(ws);
  });
});

console.log("Servidor WebSocket JS rodando em ws://localhost:8080");
