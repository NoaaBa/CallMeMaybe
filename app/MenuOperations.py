from app.core import DatabaseUsers
from app.core import DatabaseRooms
from app import Config
from app.core import KafkaOperations

def register_screen(username, password):
    user_input = input(f"REGISTER\n\n{Config.Operations.Register.SIGNUP}) Signup\n{Config.Operations.Register.SIGNIN}) Signin\n{Config.Operations.EXIT}) Exit")
    if user_input == Config.Operations.Register.SIGNUP:
        if not DatabaseUsers.add_user_to_db(username, password):
            print("Error adding the user, could be that the username already exists.")
            return False
    elif user_input == Config.Operations.Register.SIGNIN:
        if not DatabaseUsers.find_user_in_db(username):
            print("Username doesn't exist.")
            return False
    else:
        return Config.Operations.EXIT
    return True


def menu_screen():
    user_input = input(
        f"MENU\n\n{Config.Operations.Menu.ROOMS_LIST}) Get list of rooms.\n{Config.Operations.Menu.CREATE_ROOM}) Create a room.\n"
        f"{Config.Operations.Menu.JOIN_ROOM}) Join a room.\n{Config.Operations.Menu.ROOMS_YOU_IN}) Get the list of "
        f"rooms that you're in.\n{Config.Operations.EXIT}) Exit menu.")
    if user_input == Config.Operations.Menu.ROOMS_LIST:
        print(DatabaseRooms.get_list_of_rooms())
    elif user_input == Config.Operations.Menu.CREATE_ROOM:
        room_name = input("Enter room name: ")
        if not DatabaseRooms.add_room_to_db(room_name):
            print("Error creating the room, could be that the room already exists.")
            return False
    elif user_input == Config.Operations.Menu.JOIN_ROOM:
        room_name = input("Enter room name: ")
        if not DatabaseRooms.find_room_in_db(room_name):
            print("Couldn't find the room.")
            return False
        room_screen()
    elif user_input == Config.Operations.Menu.ROOMS_YOU_IN:
        KafkaOperations.get_consumer_groups()
    else:
        return Config.Operations.EXIT
    return True


def room_screen():
    room_name = input("Enter room name: ")
    user_input = input(f"ROOM MANAGER\n\n{Config.Operations.Room.SEND_MESSAGE}) Send message.\n"
                       f"{Config.Operations.Room.READ_MESSAGES}) Read room messages."
                       f"{Config.Operations.Room.EXIT_TO_MENU}) Exit to menu.")
    if user_input == Config.Operations.Room.SEND_MESSAGE:
        KafkaOperations.send_message_in_room(room_name)
    elif user_input == Config.Operations.Room.READ_MESSAGES:
        KafkaOperations.read_messages_in_room(room_name)
    else:
        return

