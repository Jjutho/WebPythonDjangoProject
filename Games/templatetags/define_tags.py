import sys
sys.path.append('../Games')

from django import template
from Games.models import Comment, Game

register = template.Library()

@register.simple_tag
def has_user_reviewed(game, user):
    comments = Comment.objects.filter(user=user, game=game)
    if not comments:
        return False
    else:
        return True

@register.simple_tag
def get_total_rating(game):
    comments = Comment.objects.filter(game=game)
    rating = 0

    for comment in comments:
        rating += comment.rating

    total_rating = round(rating / len(comments), 1)

    Game.objects.filter(pk=game.id).update(total_rating=total_rating)

    return total_rating
