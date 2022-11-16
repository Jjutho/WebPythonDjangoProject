from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

def game_list(request):
    all_games = Game.objects.all()
    context = {'all_the_games': all_games}
    return render(request, 'game-list.html', context)

def game_list(request, **kwargs):
    game_id = kwargs['pk']
    that_one_game = Game.objects.get(id=game_id)
    context = {'that_one_computer', that_one_game}
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

