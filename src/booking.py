import uuid

from src.hotel import Hotel
from src.room import Room


class Booking:
    def __init__(self, hotel: Hotel):
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

    def is_room_available(self, from_date, to_date, room_number):
        for booking in self._booking_list:
            if booking.room.room_number == room_number and (booking.to_date < from_date or booking.to_date > to_date):
                return False
        return True

    def book_a_room(self, from_date, to_date, room_number):
        if self.is_room_available(from_date, to_date, room_number):
            book_item = BookingItem(room_number, from_date, to_date)
            self.add_booking_item(book_item)
            return book_item.get_book_price()

    def add_booking_item(self, booking_item):
        self._booking_list.append(booking_item)

    def delete_booking_item(self, booking_id):
        for booking in self._booking_list:
            if booking.booking_id == booking_id:
                return self._booking_list.remove(booking)


class BookingItem:
    def __init__(self, room: Room, from_date, to_date):
        self._booking_id = str(uuid.uuid4())
        self._room = room
        self._from_date = from_date
        self._to_date = to_date

    @property
    def booking_id(self):
        return self._booking_id

    @property
    def room(self):
        return self._room

    @property
    def from_date(self):
        return self._from_date

    @property
    def to_date(self):
        return self._to_date

    def get_book_price(self):
        return self._room.price * (self.to_date - self._from_date)
