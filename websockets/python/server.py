import asyncio
import websockets

connected = set()

# Função que lida com cada cliente conectado
async def handler(websocket):
    # Adiciona o cliente ao conjunto 
    connected.add(websocket)
    print(f"Cliente conectado: {websocket.remote_address}")
    try:
        # Mantém a conexão enquanto o cliente estiver conectado
        async for message in websocket:
            print(f"Mensagem recebida de {websocket.remote_address}: {message}")
            pass 
    except websockets.ConnectionClosed:
        pass
    finally:
        # Remove o cliente ao desconectar
        connected.remove(websocket)
        print(f"Cliente desconectado: {websocket.remote_address}")

# Função principal para iniciar o servidor
async def main():
    # Inicia o servidor WebSocket 
    async with websockets.serve(handler, "localhost", 8765):
        print("Servidor WebSocket Python rodando em ws://localhost:8765")
        await asyncio.Future()  # Mantém o servidor rodando para sempre

#Executa a função principal se o script for chamado diretamente
if __name__ == "__main__":
    asyncio.run(main())
