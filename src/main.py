from datetime import datetime

from src.booking import Booking
from src.hotel import Hotel
from src.room import SingleBedRoom, DoubleBedRoom


def start_booking(booking):
    room_number = int(input("Please add the room number "))
    from_date = datetime.strptime(input("Please add the from-date (yyyy-mm-dd): "), '%Y-%m-%d')
    to_date = datetime.strptime(input("Please add the to-date (yyyy-mm-dd): "), '%Y-%m-%d')
    booking.book_a_room(from_date, to_date, room_number)


def start_cancellation(booking):
    booking_number = int(input('Please add the booking number for canceling'))
    booking.delete_booking_item(booking_number)


def list_booking(booking):
    for booking_item in booking.booking_item_list:
        booking_item.print_details()


def create_rooms():
    return [SingleBedRoom(201), SingleBedRoom(202), DoubleBedRoom(203)]


def create_bookings(booking):
    booking.book_a_room(
        datetime.strptime('2023-06-01', '%Y-%m-%d'),
        datetime.strptime('2023-06-07', '%Y-%m-%d'), 201)

    booking.book_a_room(
        datetime.strptime('2023-06-01', '%Y-%m-%d'),
        datetime.strptime('2023-06-07', '%Y-%m-%d'), 202)

    booking.book_a_room(
        datetime.strptime('2023-06-01', '%Y-%m-%d'),
        datetime.strptime('2023-06-07', '%Y-%m-%d'), 203)

    booking.book_a_room(
        datetime.strptime('2023-07-01', '%Y-%m-%d'),
        datetime.strptime('2023-07-07', '%Y-%m-%d'), 201)

    booking.book_a_room(
        datetime.strptime('2023-07-01', '%Y-%m-%d'),
        datetime.strptime('2023-07-07', '%Y-%m-%d'), 202)


if __name__ == '__main__':

    hotel = Hotel('GDE Exam Hotel', create_rooms())

    booking = Booking(hotel)

    create_bookings(booking)

    while True:

        selected_option = int(
            input('Please select from the menu:\n1. Booking\n2.Cancel booking\n3. List bookings\n4. Exit'))

        if selected_option == 1:
            start_booking(booking)
        elif selected_option == 2:
            start_cancellation(booking)
        elif selected_option == 3:
            list_booking(booking)
        elif selected_option == 4:
            break
        else:
            print('Invalid input')
