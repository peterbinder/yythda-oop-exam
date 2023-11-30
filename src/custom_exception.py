class RoomNotFoundException(Exception):
    def __init__(self, room_number):
        super().__init__(f'Room with room number {room_number} is not found.')
