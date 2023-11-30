from src.custom_exception import RoomNotFoundException
from src.room import Room


class Hotel:
    def __init__(self, hotel_name: str):
        self._name = hotel_name
        self._rooms = [Room]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    def add_room(self, room: Room):
        self._rooms.append(room)

    def get_all_room(self):
        return self._rooms

    def get_room_by_room_nr(self, room_number: int):
        for room in self._rooms:
            if room.room_number == room_number:
                return room
        raise RoomNotFoundException(room_number)
