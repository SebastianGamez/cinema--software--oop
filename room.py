class Room:
    def __init__(self, id, number, seats):
        self._id = str(id)
        self._number = number
        self._seats = seats

    @property
    def id(self):
        return self._id

    @property
    def number(self):
        return self._number

    @property
    def seats(self):
        return self._seats
