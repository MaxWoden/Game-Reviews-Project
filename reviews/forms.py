from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, Game

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'}),
        }
        labels = {
            'rating': 'Оценка (от 1 до 10)',
            'content': 'Текст отзыва',
        }

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'logo', 'release_date', 'developer', 'publisher', 'genre']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'developer': forms.TextInput(attrs={'class': 'form-control'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
        }