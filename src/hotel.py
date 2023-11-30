from src.custom_exception import RoomNotFoundException
from src.room import Room


class Hotel:
    def __init__(self, hotel_name: str, rooms: [Room]):
        self._name = hotel_name
        self._rooms = rooms

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms

    def add_room(self, room: Room):
        self._rooms.append(room)

    def get_room_by_room_nr(self, room_number: int):
        for room in self._rooms:
            if room.room_number == room_number:
                return room
        raise RoomNotFoundException(room_number)
