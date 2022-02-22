import app.entities.User
from app import MenuOperations
from app import Config
from app.entities import User


def run():
    user = MenuOperations.register_screen()
    if type(user) is app.entities.User.User:
        # User was able to register.
        while (MenuOperations.menu_screen(user)) != Config.Operations.EXIT:
            continue
