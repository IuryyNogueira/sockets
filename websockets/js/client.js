
const WebSocket = require("ws");

// Cria uma conexão com o servidor WebSocket
const ws = new WebSocket("ws://localhost:8080");

// Evento disparado quando a conexão é aberta
ws.on("open", function open() {
  console.log("Conectado ao servidor JS! \nPressione Ctrl+C para sair.");
});

// Captura o evento de interrupção (Ctrl+C) no terminal
process.on("SIGINT", () => {
  console.log("Desconectando...");
  ws.close(); // Fecha a conexão WebSocket
  process.exit(); // Encerra o processo
});
