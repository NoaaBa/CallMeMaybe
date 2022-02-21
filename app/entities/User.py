class User:
    def __init__(self, user_id, password, rooms):
        self.user_id = user_id
        self.password = password
        self.rooms = rooms

    def is_user_in_room(self, room_name):
        if room_name in self.rooms:
            return True
        return False
