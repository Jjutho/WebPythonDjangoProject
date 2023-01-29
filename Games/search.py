import datetime
from django.core.exceptions import ObjectDoesNotExist
from Games.models import Game


print('----- get() -----')
game = Game.objects.get(id=3)
print('id=3', game)

try:
    game = Game.objects.get(id=9999)
except ObjectDoesNotExist:
    print('id=9999, Book not found')
    book = None
print('id=9999', game)

print('----- filter() -----')
games = Game.objects.filter(id__gt=2)

if games: # Pruefen, ob mindestens 1 Objekt gefunden ist
    print(len(games), 'yes game found')
else:
    print(len(games), 'no game found')

print('----- exclude() -----')
games = Game.objects.exclude(creator__endswith='Cat')
print('Game found:')
for game in games:
    print(repr(games))

print('----- verketten -----')
books = Game.objects.filter(creator__endswith='Cat')\
    .filter(date_published__gt=datetime.date(2015,2,15))
print('Game found:')
for game in games:
    print(repr(game))
