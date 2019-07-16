from websocket import create_connection


def join_game():
    return create_connection("wss://p0d0cvu6q0.execute-api.us-east-1.amazonaws.com/dev/")


def move_forward(connection):
    if connection is None:
        print("please call join_game first")
        return
    connection.send('{"action": "sendMessage", "name": "mike2", "channelId": "General", "content": "hello world3!"}')
