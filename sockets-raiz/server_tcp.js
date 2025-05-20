const net = require('net');

const HOST = '127.0.0.1';
const PORT = 9000;

const server = net.createServer((socket) => {
  const clientAddress = socket.remoteAddress + ':' + socket.remotePort;
  console.log('Cliente conectado:', clientAddress);

  socket.on('end', () => {
    console.log('Cliente desconectado:', clientAddress);
  });

  socket.on('error', (err) => {
    console.log('Erro:', err.message);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`Servidor TCP Node.js rodando em ${HOST}:${PORT}`);
});
