from websocket import create_connection
import json


def join_game(name):
    connection = create_connection("wss://p0d0cvu6q0.execute-api.us-east-1.amazonaws.com/dev/")
    connection.send('{"action": "sendMessage", "name": "{}", "channelId": "General", "content": "join_game"}'.format(name))
    return connection


def forward(connection):
    connection.send('{"action": "sendMessage", "name": "name", "channelId": "General", "content": "forward"}')


def stop(connection):
    connection.send('{"action": "sendMessage", "name": "name", "channelId": "General", "content": "stop"}')


def find_giphymon(connection):
    connection.send('{"action": "sendMessage", "name": "name", "channelId": "General", "content": "find_giphymon"}')


def close_to_giphymon(connection):
    connection.send('{"action": "sendMessage", "name": "name", "channelId": "General", "content": "close_to_giphymon"}')
    while True:
        result = connection.recv()
        result = json.loads(result)
        if 'filterId' in result and result['name'] == 'closetogiphymonresponse':
            return result['content']


def capture_giphymon(connection):
    connection.send('{"action": "sendMessage", "name": "name", "channelId": "General", "content": "capture_giphymon"}')
