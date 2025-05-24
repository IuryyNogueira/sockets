import asyncio
import websockets

conectados = set() #caso eu venha utilizar 

async def broadcast(mensagem):
    if conectados:
        to_remove = set()
        for client in conectados:
            try:
                await client.send(mensagem)
            except websockets.ConnectionClosed:
                to_remove.add(client)
        conectados.difference_update(to_remove) 

# Cada cliente conectado
async def lidarCliente(websocket): 
    conectados.add(websocket)
    print(f"Cliente conectado: {websocket.remote_address}")

    await broadcast(f"Usuários conectados: {len(conectados)}")
    try:
        # não configurei no cliente para enviar mensagens
        # Mantém a conexão enquanto o cliente estiver conectado
        async for message in websocket:
            print(f"Mensagem recebida de {websocket.remote_address}: {message}")
            pass 
    except websockets.ConnectionClosed:
        pass
    finally:
        conectados.remove(websocket)
        print(f"Cliente desconectado: {websocket.remote_address}")


#iniciar o servidor
async def main():
    async with websockets.serve(lidarCliente, "localhost", 8765):
        print("Servidor WebSocket Python rodando em ws://localhost:8765")
        await asyncio.Future()  # Mantém o servidor rodando para sempre


#É uma forma de controlar o que roda automaticamente 
#e o que fica só disponível para uso.
#if seja executado apenas 
#se você rodar o script diretamente, e não se importar ele em outro lugar
if __name__ == "__main__":
    asyncio.run(main())
