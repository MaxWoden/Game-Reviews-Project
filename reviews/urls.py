from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('best/', views.best_games, name='best_games'),
    path('add-game/', views.add_game, name='add_game'),
    path('register/', views.register, name='register'),
]