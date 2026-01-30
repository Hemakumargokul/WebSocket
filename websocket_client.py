import asyncio
import websockets


async def main():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        print("Connected. Type messages, or just press Enter to quit.")
        try:
            while True:
                msg = input("You: ").strip()
                if not msg:
                    break
                await websocket.send(msg)
                reply = await websocket.recv()
                print(f"Server: {reply}")
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    asyncio.run(main())