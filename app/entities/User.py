from app.core import DatabaseUsers

class User:
    def __init__(self, user_id, password, rooms):
        self.user_id = user_id
        self.password = password
        self.rooms = rooms

    def is_user_in_room(self, room_name):
        if room_name in self.rooms:
            return True
        return False

    def add_room(self, room_name):
        DatabaseUsers.update_rooms_to_user(self.user_id, room_name)