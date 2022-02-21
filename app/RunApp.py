from app import MenuOperations
from app import Config


def run():
    username = input("Enter username: ")
    password = input("Enter password: ")
    while (MenuOperations.register_screen(username, password)) != Config.Operations.EXIT:
        # User was able to register.
        while (MenuOperations.menu_screen()) != Config.Operations.EXIT:
            continue
