from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Avg, Count
from .models import Game, Review
from .forms import ReviewForm, RegisterForm, GameForm

def home(request):
    games = Game.objects.all().order_by('-created_date')
    context = {
        'games': games,
        'page_title': 'Главная - Все игры',
    }
    return render(request, 'reviews/home.html', context)

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all().order_by('-created_date')
    
    user_review = None
    if request.user.is_authenticated:
        try:
            user_review = Review.objects.get(game=game, author=request.user)
        except Review.DoesNotExist:
            user_review = None
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            if user_review:
                user_review.rating = form.cleaned_data['rating']
                user_review.content = form.cleaned_data['content']
                user_review.save()
                messages.success(request, 'Ваш отзыв обновлен!')
            else:
                review = form.save(commit=False)
                review.game = game
                review.author = request.user
                review.save()
                messages.success(request, 'Ваш отзыв добавлен!')
            return redirect('game_detail', game_id=game.id)
    else:
        if user_review:
            form = ReviewForm(instance=user_review)
        else:
            form = ReviewForm()
    
    context = {
        'game': game,
        'reviews': reviews,
        'form': form,
        'user_review': user_review,
        'page_title': f'{game.title} - Отзывы',
    }
    return render(request, 'reviews/game_detail.html', context)

def best_games(request):
    best_games = Game.objects.annotate(
        review_count=Count('reviews')
    ).filter(review_count__gte=3).order_by('-avg_rating')[:5]
    
    if len(best_games) < 3:
        best_games = Game.objects.filter(avg_rating__gt=0).order_by('-avg_rating')[:5]
    
    context = {
        'best_games': best_games,
        'page_title': 'Лучшие игры',
    }
    return render(request, 'reviews/best_games.html', context)

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            messages.success(request, f'Игра "{game.title}" успешно добавлена!')
            return redirect('home')
    else:
        form = GameForm()
    
    context = {
        'form': form,
        'page_title': 'Добавить новую игру',
    }
    return render(request, 'reviews/add_game.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # ИСПРАВЛЕНИЕ: указываем бэкенд явно
            from django.contrib.auth import login
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'reviews/register.html', {'form': form})