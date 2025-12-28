from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

class Game(models.Model):
    GENRE_CHOICES = [
        ('RPG', 'Ролевые игры'),
        ('FPS', 'Шутеры'),
        ('STR', 'Стратегии'),
        ('ADV', 'Приключения'),
        ('SIM', 'Симуляторы'),
        ('SPT', 'Спортивные'),
        ('IND', 'Инди'),
        ('MMO', 'ММО'),
        ('MOB', 'MOBA'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Название игры")
    description = models.TextField(verbose_name="Описание игры")
    logo = models.ImageField(upload_to='game_logos/', blank=True, null=True, verbose_name="Логотип")
    release_date = models.DateField(verbose_name="Дата выхода")
    developer = models.CharField(max_length=100, verbose_name="Разработчик")
    publisher = models.CharField(max_length=100, verbose_name="Издатель", blank=True)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, verbose_name="Жанр")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    avg_rating = models.FloatField(default=0.0, verbose_name="Средний рейтинг")
    
    def update_avg_rating(self):
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.avg_rating = round(avg if avg else 0.0, 1)
        self.save()
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('game_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews', verbose_name="Игра")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Авор")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Оценка (1-10)"
    )
    content = models.TextField(verbose_name="Текст отзыва")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.game.update_avg_rating()
    
    def delete(self, *args, **kwargs):
        game = self.game
        super().delete(*args, **kwargs)
        game.update_avg_rating()
    
    def __str__(self):
        return f"Отзыв на {self.game.title} от {self.author.username}"
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        unique_together = ['game', 'author']