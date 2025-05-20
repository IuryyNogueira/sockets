import asyncio # programação assíncrona 
import websockets

async def main():
    uri = "ws://localhost:8765"  # Endereço do servidor WebSocket

    # Conecta ao servidor WebSocket
    async with websockets.connect(uri) as websocket:
        print("Conectado ao servidor Python! \nPressione Ctrl+C para sair.")
        try:
            # Mantém a conexão aberta até o usuário pressionar Ctrl+C
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            #pressionar Ctrl+C, desconecta
            print("Desconectando...")

# Executa a função principal se o script for chamado diretamente
if __name__ == "__main__":
    asyncio.run(main()) 