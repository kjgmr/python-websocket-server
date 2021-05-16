#!/usr/bin/env python3

import asyncio
import websockets
import csv

async def server(websocket, path):
    # Get received data from websocket
    data = await websocket.recv()

    # Send response back to client to acknowledge receiving message
    # await websocket.send("Thank you for your message: " + data)

    with open('multi-stream_q.csv', newline='\n') as f:
        reader = csv.reader(f, quotechar="'")
        for row in reader:
            await websocket.send(str(row))
            # print(row)

# Create websocket server
start_server = websockets.serve(server, "localhost", 6789)

# Start and run websocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()