## Функции ##
"""
Простая функция, которая выводит приветствие.
"""
# Тело функции
def greet_user():
	print("Hello!")
# Вызов функции	
greet_user()
print()

### Передача информации функции ###
"""
Следующая функция выводит приветствие по имени.
"""
def greet_user(username):
	print(f"Hello, {username.title()}!")

greet_user('jesse')
print()	
