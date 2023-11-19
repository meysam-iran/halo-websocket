# Import the websockets and asyncio modules
import websockets
import asyncio

# Define an async function that creates the websocket connection
async def hello():
    # Connect to the websocket server using the wss URL
    uri = "wss://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = "Hello, world!"
        await websocket.send(message)
        # Print the message to the console
        print(f"Sent: {message}")

        # Receive a message from the server
        response = await websocket.recv()
        # Print the response to the console
        print(f"Received: {response}")

# Run the client using the asyncio event loop
asyncio.get_event_loop().run_until_complete(hello())
