from app import Config
from app.entities.User import User
import json
import os


def add_user_to_db(username, password):
    if not find_user_in_db(username):
        user = User(username, password, None)
        if os.path.getsize(Config.Links.USERS_DATA) != 0:
            data = []
            with open(Config.Links.USERS_DATA, "r") as file:
                data.append(json.load(file))
                data.append(user.__dict__)
        else:
            data = user.__dict__
        print(data)
        with open(Config.Links.USERS_DATA, "w") as file:
            json.dump(data, file)
        file.close()
        return True
    return False


def find_user_in_db(username):
    file = open(Config.Links.USERS_DATA, "r")
    for line in file.readlines():
        if username in line:
            file.close()
            return True
    file.close()
    return False


def transform_user(username):
    data = dict()
    with open(Config.Links.USERS_DATA, "r") as file:
        data = json.load(file)
    file.close()
    for user in data:
        if username in user['user_id']:
            new_user = User(user['user_id'], user['password'], user['rooms'])
            return new_user
    return False


def update_rooms_to_user(username, room):
    data = dict()
    with open(Config.Links.USERS_DATA, "r") as file:
        data = json.load(file)
    file.close()
    for user in data:
        if username in user['user_id']:
            user['rooms'] = room