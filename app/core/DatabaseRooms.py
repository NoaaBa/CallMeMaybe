from app import Config
from app.entities.Room import Room
import json


def add_room_to_db(name):
    if not find_room_in_db(name):
        room = Room(name, 0)
        with open(Config.Links.ROOMS_DATA, "r") as file:
            data = json.load(file)
            data.append(room)

        with open(Config.Links.ROOMS_DATA, "w") as file:
            json.dump(data, file)
        file.close()
        return True
    return False


def find_room_in_db(name):
    file = open(Config.Links.ROOMS_DATA, "r")
    for line in file.readlines():
        if name in line:
            file.close()
            return True
    file.close()
    return False


def get_list_of_rooms():
    with open(Config.Links.ROOMS_DATA, "r") as file:
        return file.readlines()
