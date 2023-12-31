from abc import ABC, abstractmethod


class Room(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

    @property
    @abstractmethod
    def room_number(self):
        pass


class SingleBedRoom(Room):

    def __init__(self, room_number):
        self._price = 100
        self._room_number = room_number

    @property
    def price(self):
        return self._price

    @property
    def room_number(self):
        return self._room_number


class DoubleBedRoom(Room):

    def __init__(self, room_number):
        self._price = 150
        self._room_number = room_number

    @property
    def price(self):
        return self._price

    @property
    def room_number(self):
        return self._room_number
