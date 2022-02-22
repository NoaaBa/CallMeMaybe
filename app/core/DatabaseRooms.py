from app import Config
from app.entities import User
import pickle
import os


def add_room_to_db(name):
    if not find_room_in_db(name):
        # Checking if file is not empty.
        if os.path.getsize(Config.Links.ROOMS_DATA) != 0:
            list=[]
            file = open(Config.Links.ROOMS_DATA,'r')
            for line in file:
                list.append(line.strip())
            list.append(name)
            file.close()
            with open(Config.Links.ROOMS_DATA, "w") as file_writer:
                  for item in list:
                         file_writer.write('%s\n' % item)
            file_writer.close()
        else:
            with open(Config.Links.ROOMS_DATA, "w") as file_writer:
               file_writer.write(name)
            file_writer.close()
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

