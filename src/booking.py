import uuid

from src.hotel import Hotel
from src.room import Room


class Booking:
    def __init__(self, hotel:Hotel):
        self._hotel = hotel
        self._booking_list = []

    @property
    def hotel(self):
        return self._hotel

    @property
    def booking_list(self):
        return self._booking_list

    @booking_list.setter
    def booking_list(self, booking_list):
        self._booking_list = booking_list

    def add_booking_item(self, booking_item):
        self._booking_list.append(booking_item)

    def delete_booking_item(self, booking_id ):
        for booking in self._booking_list:
            if booking.

class BookingItem:
    def __init__(self, room:Room, days:int):
        self._booking_id = str(uuid.uuid4())
        self._room = room
        self._days = days

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def room(self):
        return self._room

    @property
    def days(self):
        return self.days