# Import additional libraries
import uuid

# import program classes
from room import Room
from film import Film
from projection import Projection
from user import User

# Create the seats for the room
seats = [i + j for j in '0123456789' for i in 'abcdefgh']


room1 = Room(uuid.uuid1(), 1, seats)
film1 = Film('El abogado del diablo')
projection1 = Projection(uuid.uuid1(), film1.name, (2022, 4, 9), room1)
user1 = User('Pablo Gaitan')

# Show the available tickets
for k in projection1.tickets:
    print(f'id: {k.id}\nFilm name: {k.film_name}\nDate: {k.date}\nSeat: {k.seat}\n')

# Select and buy the ticket for the seat
ticket_id = input('Please, put a available seat for complete the buy: ')
user1.buy_ticket(projection1, ticket_id)

print(f'Now, {user1.name} have: {user1.tickets} tickets')