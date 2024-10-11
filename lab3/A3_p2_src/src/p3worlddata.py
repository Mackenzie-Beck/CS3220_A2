import random

r1a, r1b, r1c, r2a, r2b, r2c = 'Room1_A', 'Room1_B', 'Room1_C', 'Room2_A', 'Room2_B', 'Room2_C'

p3world = {
    r1a: {r1b: 1, r2a: 1},
    r1b: {r1a: 1, r1c: 1},
    r1c: {r1b: 1, r2c: 1},
    r2a: {r1a: 1, r2b: 1},
    r2b: {r2a: 1, r2c: 1},
    r2c: {r1c: 1, r2b: 1}
}

def create_room_dict():
    """
    Create a dictionary where the key is a room object and the value is a coordinate.
    
    Returns:
    dict: A dictionary containing the room as the key and the coordinate as the value.
    """
    coordinates = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    rooms = [r1a, r1b, r1c, r2a, r2b, r2c]
    return {room: coord for room, coord in zip(rooms, coordinates)}




def get_random_rooms(num_rooms=4):
    """
    Returns a list of rooms randomly selected from the available rooms.
    
    Args:
    num_rooms (int): The number of rooms to select.
    
    Returns:
    list: A list of randomly selected rooms.
    """
    rooms = [r1a, r1b, r1c, r2a, r2b, r2c]
    return random.sample(rooms, num_rooms)
