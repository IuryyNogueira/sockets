const net = require('net'); // Importa o módulo net do Node.js para criar um cliente TCP

const HOST = '127.0.0.1';
const PORT = 9000;

const client = new net.Socket();

client.connect(PORT, HOST, () => {
  console.log(`Conectado ao servidor TCP Node.js\nem ${HOST}:${PORT}.\nPressione Ctrl+C para sair.`);
});

process.on('SIGINT', () => { // Intercepta o sinal Ctrl+C
  console.log('Desconectando...');
  client.end();
  process.exit();
});

client.on('close', () => { // Evento disparado quando a conexão é fechada
  console.log('Conexão encerrada.');
});
