class Links:
    KAFKA_HOSTS = ['localhost:9092']
    USERS_DATA = r"json_data/users.json"
    ROOMS_DATA = R"json_data/rooms.txt"


class Operations:
    EXIT = 0

    class Register:
        SIGNUP = 1
        SIGNIN = 2

    class Menu:
        ROOMS_LIST = 1
        CREATE_ROOM = 2
        JOIN_ROOM = 3
        ROOMS_YOU_IN = 4

    class Room:
        SEND_MESSAGE = 1
        READ_MESSAGES = 2
        EXIT_TO_MENU = 3
