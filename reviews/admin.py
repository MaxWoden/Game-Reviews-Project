from django.contrib import admin
from .models import Game, Review

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'developer', 'avg_rating', 'created_date')
    list_filter = ('genre', 'created_date')
    search_fields = ('title', 'developer', 'description')
    readonly_fields = ('avg_rating', 'created_date')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'description', 'logo', 'genre')
        }),
        ('Детали', {
            'fields': ('release_date', 'developer', 'publisher')
        }),
        ('Статистика', {
            'fields': ('avg_rating', 'created_date')
        }),
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('game', 'author', 'rating', 'created_date')
    list_filter = ('rating', 'created_date')
    search_fields = ('content', 'game__title', 'author__username')
    readonly_fields = ('created_date', 'updated_date')