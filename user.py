class User:

    def __init__(self, name):
        self._name = name
        self._tickets = []

    @property
    def name(self):
        return self._name

    @property
    def tickets(self):
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        self._tickets = tickets

    def buy_ticket(self, projection, ticket_seat):
        for ticket in projection.tickets:
            if ticket.seat == ticket_seat:
                self.tickets.append(ticket)
                projection.tickets.remove(ticket)

