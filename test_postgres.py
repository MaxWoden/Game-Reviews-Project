# test_postgres.py
import psycopg2
from psycopg2 import OperationalError

print("Тестирование подключения к PostgreSQL...")
print("=" * 50)

# Параметры подключения (должны совпадать с settings.py)
db_params = {
    'host': 'localhost',
    'database': 'game_reviews_db',
    'user': 'postgres',
    'password': 'b89G28Kau',  # Поменяйте на ваш пароль!
    'port': '5432'
}

try:
    # Пробуем подключиться
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    
    # Выполняем тестовый запрос
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    
    print(f"✅ Успешное подключение к PostgreSQL!")
    print(f"📊 Версия PostgreSQL: {db_version[0]}")
    
    # Проверим существующие базы данных
    cursor.execute("SELECT datname FROM pg_database;")
    databases = cursor.fetchall()
    
    print(f"\n📁 Доступные базы данных:")
    for db in databases:
        if db[0] == db_params['database']:
            print(f"  ✅ {db[0]} (используется)")
        else:
            print(f"  • {db[0]}")
    
    cursor.close()
    connection.close()
    
except OperationalError as e:
    print(f"❌ Ошибка подключения: {e}")
    print("\nВозможные проблемы:")
    print("1. Неправильный пароль")
    print("2. База данных не существует")
    print("3. Пользователь не имеет прав")
    
    # Предложение создать БД
    print("\nПопробуйте создать базу данных:")
    print(f"CREATE DATABASE {db_params['database']};")
    
except Exception as e:
    print(f"❌ Неожиданная ошибка: {e}")

print("\n" + "=" * 50)