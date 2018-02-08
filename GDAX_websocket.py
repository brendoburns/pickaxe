
import requests
import gdax
import websockets
from websocket import create_connection, WebSocketConnectionClosedException


ws = websocket.WebSocket()
ws.connect('wss://ws-feed-public.sandbox.gdax.com')

