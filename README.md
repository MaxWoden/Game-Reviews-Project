🎮 Game Reviews - Проект сайта отзывов об играх

Выполненные требования проекта

# 1. Основные страницы (реализовано):

1. Главная страница - Список всех игр с логотипами, названиями и средними рейтингами
2. Страница игры - Полное описание игры + список отзывов (автор, текст, оценка)
3. Лучшие игры - Топ-5 игр с самой высокой оценкой

# 2. Дополнительные функции (реализовано сверх требований):

1. Аутентификация - Регистрация и вход (стандартная + через GitHub OAuth)
2. Добавление игр - Форма для добавления новых игр (для авторизованных)
3. Динамические рейтинги - Средний рейтинг рассчитывается автоматически
4. Адаптивный дизайн - Работает на всех устройствах
5. Админ-панель - Полное управление контентом через Django Admin
6. Добавлена библиотека ipython

# Database Schema

## Tables

### Game
| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Primary key |
| title | Char(200) | Game title |
| description | Text | Game description |
| logo | Image | Game logo image |
| release_date | Date | Release date |
| developer | Char(100) | Developer company |
| publisher | Char(100) | Publisher company |
| genre | Char(50) | Game genre |
| avg_rating | Decimal(3,2) | Average rating (calculated) |
| created_date | DateTime | Creation timestamp |

### Review
| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Primary key |
| game_id | Integer (FK → Game.id) | Associated game |
| author_id | Integer (FK → User.id) | Review author |
| rating | Integer(1-10) | Rating score |
| content | Text | Review text |
| created_date | DateTime | Creation timestamp |
| updated_date | DateTime | Last update timestamp |

### User (Django built-in)
| Column | Type | Description |
|--------|------|-------------|
| id | Integer (PK) | Primary key |
| username | Char(150) | Username |
| email | Email | Email address |
| password | Char(128) | Hashed password |
| date_joined | DateTime | Registration date |
| is_staff | Boolean | Staff status |
| is_superuser | Boolean | Superuser status |

# 3. Связи:

1. Game (1) → Review (N) - Одна игра может иметь много отзывов
2. User (1) → Review (N) - Один пользователь может оставить много отзывов
3. User → Game - Пользователи могут добавлять игры

# 4. Инструкция для запуска используя docker:

1. Клонирование проекта
   git clone https://github.com/MaxWoden/Game-Reviews-Project.git
   cd game_reviews_site

2. Запуск проекта
   docker-compose up --build



