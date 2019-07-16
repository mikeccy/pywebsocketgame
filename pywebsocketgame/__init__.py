from websocket import create_connection

ws = None


def join_game():
    ws = create_connection("wss://p0d0cvu6q0.execute-api.us-east-1.amazonaws.com/dev/")
    return ws


def move_forward():
    if ws is None:
        print("please call join_game first")
        return
    ws.send('{"action": "sendMessage", "name": "mike2", "channelId": "General", "content": "hello world3!"}')
