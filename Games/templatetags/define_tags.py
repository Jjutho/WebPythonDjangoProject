import sys
sys.path.append('../Games')

from django import template
from Games.models import Comment

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

    return round(rating / len(comments), 1)