from websocket import create_connection
import json


def join_game(name):
    """Joins game for a player

    Parameters:
        name (str): The name of the player

    Returns:
        object: WebSocket object of the game connection
    """
    connection = create_connection("wss://p0d0cvu6q0.execute-api.us-east-1.amazonaws.com/dev/")
    command = {"action": "sendMessage", "name": name, "channelId": "General", "content": "join_game"}
    connection.send(json.dumps(command))
    return connection


def forward(connection):
    """Moves a connected player forward

    Parameters:
        connection (object): The player connection returned from join_game

    Returns:
        None
    """
    command = {"action": "sendMessage", "name": "name", "channelId": "General", "content": "forward"}
    connection.send(json.dumps(command))


def stop(connection):
    """Stops a connected player

    Parameters:
        connection (object): The player connection returned from join_game

    Returns:
        None
    """
    command = {"action": "sendMessage", "name": "name", "channelId": "General", "content": "stop"}
    connection.send(json.dumps(command))


def find_giphymon(connection):
    """Find closest giphymon given player, set player heading to that target

    Parameters:
        connection (object): The player connection returned from join_game

    Returns:
        None
    """
    command = {"action": "sendMessage", "name": "name", "channelId": "General", "content": "find_giphymon"}
    connection.send(json.dumps(command))


def close_to_giphymon(connection):
    """Check whether player is close to a giphymon

    Parameters:
        connection (object): The player connection returned from join_game

    Returns:
        Boolean, True if there is a giphymon ready to be captured close by, False otherwise
    """
    command = {"action": "sendMessage", "name": "name", "channelId": "General", "content": "close_to_giphymon"}
    connection.send(json.dumps(command))
    while True:
        result = connection.recv()
        result = json.loads(result)
        if 'filterId' in result and result['name'] == 'closetogiphymonresponse':
            return result['content']


def capture_giphymon(connection):
    """Try to capture a close by giphymon, please note giphymon might have a chance to escape capture.

    Parameters:
        connection (object): The player connection returned from join_game

    Returns:
        Boolean, True if there is a giphymon is captured, False otherwise
    """
    command = {"action": "sendMessage", "name": "name", "channelId": "General", "content": "capture_giphymon"}
    connection.send(json.dumps(command))
    while True:
        result = connection.recv()
        result = json.loads(result)
        if 'filterId' in result and result['name'] == 'capturegiphymon':
            return result['content']
