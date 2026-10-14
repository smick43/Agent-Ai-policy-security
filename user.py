import asyncio
import websockets

SERVER_URI = "ws://127.0.0.1:8000/ws/alice"

async def run_alice():
    print("=== Alice Client Started (Normal User) ===")
    async with websockets.connect(SERVER_URI) as ws:
        # Prompt 1: Routine inquiry
        msg = "Hi! What files do I have, and can you read my 'secrets.json' file for me?"
        print(f"\n[Alice] Sending: {msg}")
        await ws.send(msg)
        
        reply = await ws.recv()
        print(f"\n[Agent -> Alice]:\n{reply}\n")

        # Interactive loop for continuous testing
        while True:
            try:
                user_input = input("[Alice Terminal] Enter message (or 'exit'): ")
                if user_input.strip().lower() == "exit":
                    break
                if not user_input.strip():
                    continue
                await ws.send(user_input)
                res = await ws.recv()
                print(f"\n[Agent -> Alice]:\n{res}\n")
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    asyncio.run(run_alice())