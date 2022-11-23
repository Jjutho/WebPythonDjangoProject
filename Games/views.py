from django.shortcuts import render, redirect

from .forms import GameForm, CommentForm
from .models import Game, Comment, Vote

def game_list(request):
    all_games = Game.objects.all()
    context = {'all_the_games': all_games}
    return render(request, 'game-list.html', context)

def game_detail(request, **kwargs):
    game_id = kwargs['pk']
    game = Game.objects.get(id=game_id)
    comments = Comment.objects.filter(game=game)

    context = {
        'that_one_game': game,
        'comments_for_that_one_game': comments,
        'comment_form': CommentForm,
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.instance.user = request.user
        form.instance.game = game
        if form.is_valid():
            form.save()
            return redirect('game-detail', pk=game_id)
        else:
            print(form.errors)

    return render(request, 'game-detail.html', context)

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
        else:
            pass
        return redirect('game-list')
    else:
        form = GameForm()
        context = {'form': form}
        return render(request, 'game-create.html', context)

def game_delete(request, **kwargs):
    game_id = kwargs['pk']
    that_one_game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        that_one_game.delete()
        return redirect('game-list')
    else:
        context = {'that_one_game': that_one_game}
        return render(request, 'game-delete.html', context)

def comment_delete(request, **kwargs):
    comment_id = kwargs['ck']
    game_id = kwargs['pk']
    comment = Comment.objects.get(id=comment_id)
    if request.user.username == comment.user.username:
        comment.delete()
        return redirect('game-detail', pk=game_id)

def comment_vote(request, pk: str, ck: int, up_or_down: str):
    comment_id = int(ck)
    comment = Comment.objects.get(id=comment_id)
    user = request.user

    if Vote.objects.filter(comment=comment_id, user=request.user).exists():
        existing_vote = Vote.objects.get(comment=comment_id, user=request.user)
        if up_or_down == 'up':
            if existing_vote.up_or_down == 'U':
                existing_vote.delete()
            elif existing_vote.up_or_down == 'D':
                existing_vote.change_vote('U')
                existing_vote.save()
        elif up_or_down == 'down':
            if existing_vote.up_or_down == 'U':
                existing_vote.change_vote('D')
                existing_vote.save()
            elif existing_vote.up_or_down == 'D':
                existing_vote.delete()
    else:
        comment.vote(user, up_or_down)

    return redirect('game-detail', pk=pk)
