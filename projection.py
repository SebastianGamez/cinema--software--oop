from ticket import Ticket
import uuid


class Projection:
    def __init__(self, id, film_name, date, room):
        self._id = id
        self._film_name = film_name
        self._date = date
        self._number_room = room.number
        self._tickets = [Ticket(uuid.uuid1(), film_name, date, room.number, seat) for seat in room.seats]

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
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        self._tickets = tickets
