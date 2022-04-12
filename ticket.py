from datetime import date


class Ticket:

    def __init__(self, id, film_name, date_projection, number_room, seat):
        self._id = id
        self._film_name = film_name
        self._date = date(date_projection[0], date_projection[1], date_projection[2])
        self._number_room = number_room
        self._seat = seat

    @property
    def id(self):
        return self._id
    @property
    def film_name(self):
        return self._film_name
    @property
    def date(self):
        return self._date
    @property
    def number_room(self):
        return self._number_room
    @property
    def seat(self):
        return self._seat
