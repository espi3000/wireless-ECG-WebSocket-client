import websocket
import json

IP = input('Enter remote IP address: ')
PORT = input('Enter remote port: ')

def on_message(ws, message):
    print(json.loads(message)['ECG'])

ws = websocket.WebSocketApp(f'ws://{IP}:{PORT}', on_message=on_message)
ws.run_forever()