## Перебор словаря ##
# Реальный словарь может содержать больше миллиона значений, поэтому необходимо
# уметь применять различные переборы пар "ключ-значение".
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
### Перебор всех пар "ключ-значение" ###
# Если нужно посмотреть все данные словаря, можно воспользоваться перебором
# в цикле for.
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}

# Создаём две переменные в цикле for и применяем метод items()
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")
print()
# Перебор всех пар "ключ-значение" хорош именно тогда, когда в словаре у нас
# хранится один тип данных.

favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
print()

### Перебор всех ключей в словаре ###
# Метод keys() применяют когда мы работаем со всеми ключами в словаре.
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

for name in favorite_languages.keys():
	print(name.title())
print()
# Метод keys() можно опустить, так как он используется по умолчанию
# при переборе словаря. Но иногда, требуется его использование,
# для упрощения чтения кода.

# В более сложном примере мы переберём все имена в словаре
# и выведем специальное сообщение для людей с одинаковым предпочтением в языке.
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		language = favorite_languages[name].title()
		print(f"\tHi {name.title()}, I see you love {language}!")
print()

# Метод keys() также можно использовать для проверки того,
# участвовал ли конкретный человек в опросе.
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")
print()

### Перебор ключей словаря в определённом порядке ###
# Для получения упорядоченной копии словаря, воспользуемся функцией sorted().
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")
print()

### Перебор всех значений в словаре ###
# Для этого используем метод values().
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())
print()

# Чтобы получить список выбранных языков без повторений,
# можно воспользоваться множеством set().
favorite_languages = {
	'jen': 'python',
	'sarah': 'javascript',
	'edward': 'rust',
	'phill': 'python',
	}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())
print()

# Множество можно построить следующим образом:
# languages = {'python', 'javascript', 'rust', 'python'}
