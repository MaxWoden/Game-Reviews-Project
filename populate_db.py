# populate_db.py
import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_reviews_site.settings')
django.setup()

from reviews.models import Game, Review
from django.contrib.auth.models import User
from django.core.files import File

def populate_database():
    print("Начинаю заполнение базы данных...")
    
    # Создаем суперпользователя
    admin, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin.set_password('admin123')
        admin.save()
        print("✅ Создан суперпользователь: admin / admin123")
    
    # Создаем тестового пользователя
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={
            'email': 'test@example.com',
            'is_active': True
        }
    )
    if created:
        user.set_password('test123')
        user.save()
        print("✅ Создан тестовый пользователь: testuser / test123")
    
    # Данные для игр
    games_data = [
        {
            'title': 'The Witcher 3: Wild Hunt',
            'description': 'Действие игры происходит в вымышленном фэнтезийном мире, основанном на славянской мифологии. Игрок управляет Геральтом из Ривии, охотником на чудовищ.',
            'release_date': date(2015, 5, 19),
            'developer': 'CD Projekt Red',
            'publisher': 'CD Projekt',
            'genre': 'RPG',
            'avg_rating': 9.7
        },
        {
            'title': 'Cyberpunk 2077',
            'description': 'Действие игры происходит в 2077 году в Найт-Сити, вымышленном мегаполисе в Калифорнии. Игрок управляет наёмником по имени Ви.',
            'release_date': date(2020, 12, 10),
            'developer': 'CD Projekt Red',
            'publisher': 'CD Projekt',
            'genre': 'Action RPG',
            'avg_rating': 7.5
        },
        {
            'title': 'Red Dead Redemption 2',
            'description': 'Действие игры происходит на Диком Западе в 1899 году. Игрок управляет Артуром Морганом, членом банды Ван дер Линде.',
            'release_date': date(2018, 10, 26),
            'developer': 'Rockstar Studios',
            'publisher': 'Rockstar Games',
            'genre': 'Action Adventure',
            'avg_rating': 9.8
        },
        {
            'title': 'Elden Ring',
            'description': 'Действие игры происходит в Межземье, фэнтезийном мире, созданном Хидэтакой Миядзаки и Джорджем Мартином.',
            'release_date': date(2022, 2, 25),
            'developer': 'FromSoftware',
            'publisher': 'Bandai Namco',
            'genre': 'Action RPG',
            'avg_rating': 9.5
        },
        {
            'title': 'God of War (2018)',
            'description': 'Кратос, бывший греческий бог войны, стал отцом и живет в мире скандинавских богов.',
            'release_date': date(2018, 4, 20),
            'developer': 'Santa Monica Studio',
            'publisher': 'Sony Interactive Entertainment',
            'genre': 'Action Adventure',
            'avg_rating': 9.4
        }
    ]
    
    # Создаем игры
    created_games = []
    for game_data in games_data:
        game, created = Game.objects.get_or_create(
            title=game_data['title'],
            defaults=game_data
        )
        if created:
            created_games.append(game)
            print(f"✅ Создана игра: {game.title}")
    
    # Создаем отзывы
    reviews_data = [
        ("Лучшая RPG всех времен! Сюжет, персонажи, мир - все на высшем уровне.", 10),
        ("Хорошая игра, но было много багов при релизе. Сейчас стало лучше.", 8),
        ("Шедевр! Графика, история, геймплей - все идеально.", 10),
        ("Очень сложная, но невероятно увлекательная игра.", 9),
        ("Эмоциональная история отцов и сыновей. Великолепно!", 10),
        ("Отличный боевой геймплей и интересный мир.", 9),
        ("Мне понравилась свобода действий и проработанный мир.", 9),
        ("Хардкорная игра для настоящих ценителей жанра.", 8),
    ]
    
    users = User.objects.all()
    for i, game in enumerate(Game.objects.all()):
        for j in range(2):  # по 2 отзыва на игру
            review_idx = (i * 2 + j) % len(reviews_data)
            content, rating = reviews_data[review_idx]
            author = users[j % len(users)]  # чередуем авторов
            
            review, created = Review.objects.get_or_create(
                game=game,
                author=author,
                defaults={
                    'rating': rating,
                    'content': f"{content} ({game.title})"
                }
            )
            if created:
                print(f"   📝 Отзыв от {author.username}: {rating}/10")
    
    # Обновляем средние рейтинги
    for game in Game.objects.all():
        game.update_avg_rating()
    
    print(f"\n🎮 Итог:")
    print(f"   👥 Пользователей: {User.objects.count()}")
    print(f"   🎮 Игр: {Game.objects.count()}")
    print(f"   📝 Отзывов: {Review.objects.count()}")
    print("\n🔑 Данные для входа:")
    print("   Админ: admin / admin123")
    print("   Пользователь: testuser / test123")
    print("\n🌐 Сайт: http://localhost:8000")

if __name__ == '__main__':
    populate_database()