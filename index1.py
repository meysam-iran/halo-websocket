# Import the websockets and asyncio modules
import websockets
import asyncio

# Define an async function that handles the websocket connection
async def echo(websocket, path):
    # Receive a message from the client
    message = await websocket.recv()
    # Print the message to the console
    print(f"Received: {message}")
    # Send the same message back to the client
    await websocket.send(message)
    # Print a confirmation to the console
    print(f"Sent: {message}")

# Create a websocket server using the echo function
start_server = websockets.serve(echo, "localhost", 8765)

# Run the server using the asyncio event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
