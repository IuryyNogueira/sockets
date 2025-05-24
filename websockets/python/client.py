import asyncio 
import websockets

async def main():
    uri = "ws://localhost:8765"  #servidor WebSocket

    async with websockets.connect(uri) as websocket:
        print("Conectado ao servidor! \nPressione Ctrl+C para sair.")
        try:
            while True:
                resposta = await websocket.recv()
                print(resposta) 
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("Desconectando...")

        # async with websockets.connect(uri) as websocket:
        # print("Conectado ao servidor!")
        # # Envia uma mensagem única para o servidor
        # await websocket.send("Olá, servidor!")
        # print("Mensagem enviada!")
        # # Pode receber resposta opcional
        # resposta = await websocket.recv()
        # print(f"Resposta do servidor: {resposta}")
if __name__ == "__main__":
    asyncio.run(main())