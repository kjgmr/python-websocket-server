import csv

with open('multi-stream_q.csv', newline='\n') as f:
    reader = csv.reader(f, quotechar="'")
    for row in reader:
        # await websocket.send(row)
        print(row)