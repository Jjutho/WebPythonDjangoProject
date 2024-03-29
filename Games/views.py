from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Shoppingcart.models import ShoppingCart
from .forms import GameForm, GameEditForm, CommentForm, SearchForm
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
        if request.POST['action'] == 'comment':
            form = CommentForm(request.POST)
            form.instance.user = request.user
            form.instance.game = game
            if form.is_valid():
                form.save()
                return redirect('game-detail', pk=game_id)
            else:
                print(form.errors)
        elif request.POST['action'] == 'add-to-cart':
            ShoppingCart.add_item(request.user, game)

    return render(request, 'game-detail.html', context)

@staff_member_required
def game_create(request):
    form = GameForm()
    context = {'form': form}
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('game-list')
        else:
            print(form.errors)

    return render(request, 'game-create.html', context)

@staff_member_required
def game_edit(request, **kwargs):
    game_id = kwargs['pk']
    game = Game.objects.get(id=game_id)

    form = GameEditForm()
    context = {
        'form': form,
        'that_one_game': game
    }

    if request.method == 'POST':
        form = GameEditForm(request.POST or None, request.FILES, instance=game)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('game-detail', pk=game_id)
        else:
            print(form.errors)

    return render(request, 'game-edit.html', context)

@staff_member_required
def game_delete(request, **kwargs):
    game_id = kwargs['pk']
    that_one_game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        that_one_game.delete()
        return redirect('game-list')
    else:
        context = {'that_one_game': that_one_game}
        return render(request, 'game-delete.html', context)

@login_required()
def comment_delete(request, **kwargs):
    comment_id = kwargs['ck']
    game_id = kwargs['pk']
    comment = Comment.objects.get(id=comment_id)
    if request.user.username == comment.user.username or request.user.is_staff:
        comment.delete()
        return redirect('game-detail', pk=game_id)

@login_required()
def comment_report(request, **kwargs):
    comment_id = kwargs['ck']
    game_id = kwargs['pk']
    comment = Comment.objects.get(id=comment_id)
    comment.report()
    comment.save()
    return redirect('game-detail', pk=game_id)

@staff_member_required
def comment_approval(request, **kwargs):
    comment_id = kwargs['ck']
    game_id = kwargs['pk']
    comment = Comment.objects.get(id=comment_id)
    comment.approve()
    comment.save()
    return redirect('game-detail', pk=game_id)

@login_required()
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


def game_search(request):
    if request.method == 'POST':

        games_found = Game.objects.filter(
            creator__contains=request.POST['creator'],
            title__contains=request.POST['title'],
            genre__contains=request.POST['genre'],
            age_rating__contains=request.POST['age_rating'],
            total_rating__gte=request.POST['total_rating']
        )

        if not games_found:
            show_results = False
        else:
            show_results = True
        form_in_function_based_view = SearchForm()
        context = {
            'form': form_in_function_based_view,
            'game_found': games_found,
            'show_results': show_results
        }
        return render(request, 'game-search.html', context)

    else:
        form_in_function_based_view = SearchForm()
        context = {'form': form_in_function_based_view,
                   'show_results': False}
        return render(request, 'game-search.html', context)
