## Вложение ##
"""
Иногда бывает, что нужно сохранить множество словарей в списке
или сохранить список как значение элемента словаря.
Создание такого рода структуры, называется вложением.
Таким образом, можно вложить множество словарей в список или в другой словарь.
"""
### Список словарей ###
"""
Можно создать список пришельцев, в котором каждый элемент представляет собой
словарь с информацией о пришельце.
"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
print()
"""
В реальном проекте, пришельцев может быть очень много,
поэтому воспользуемся автоматической генерацией до 30 штук.
Создаём пустой список пришельцев.
"""
aliens = []

# Создание 30 пришельцев зелёного цвета.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Вывод первых пяти пришельцев.
for alien in aliens[:5]:
	print(alien)
print("...")

# Вывод количества созданных пришельцев.
print(f"Total number of aliens: {len(aliens)}")

print()
"""
У всех пришельцев одинаковые параметры, но Python считает их уникальными.
Поэтому мы можем изменять атрибуты каждого пришельца по отдельности.
"""
# Создание пустого списка с пришельцами.
aliens = []

# Создание 30 зелёных пришельцев.
for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Добавим блок if для 10 очков за пришельца.
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	
	# Добавим блок elif для 15 очков за пришельца.
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

# Вывод первых 5 пришельцев.
for alien in aliens[0:5]:
	print(alien)
print("...")

print()
"""
Решение с хранением словаря внутри списка достаточно часто встречается тогда,
когда каждый словарь содержит разные атрибуты одного объекта.
"""
### Список в словаре ###
"""
Вместо того, чтобы помещать словарь в список, иногда бывает удобно поместить
список в словарь.

В следующем примере для каждой пиццы сохраняются два вида информации,
основа и список топпингов.
А при выводе будет получен список топпингов.
"""
# Сохраним информацию о заказанной пицце.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

# Описание заказа.
print(f"You ordered a {pizza['crust']}-crust pizza " 
	"with following toppings:")

for topping in pizza['toppings']:
	# print(topping)
	print("\t" + topping)
print()
"""
Вложение списка в словарь может применять каждый раз, когда с одним
ключом словаря должно быть связано более одного значения.
"""
# Дополним один из предыдущих примеров.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
	
for name, languages in favorite_languages.items():
	# Добавим проверку количества выбранных языков.
	if len(languages) == 1:
		print(f"{name.title()}'s favorite language "
			f"is {languages[0].title()}.")
	else:
		print(f"\n{name.title()}'s favorite languages are: "
			f"{languages[0].title()}, {languages[1].title()}.") 
	# print(f"\n{name.title()}'s favorite languages are:")
	
	# for language in languages:
		# print(f"\t{language.title()}")
print()

### Словарь в словаре (чёткая иерархия информации) ###
"""
Словарь также можно вложить в другой словарь, но в таких случаях
код быстро усложняется.

В следующем примере о каждом пользователе хранится три вида информации.
Это имя, фамилия и место жительства.
Чтобы получить доступ к этой информации, нужно перебрать имена пользователей
и словарь с информацией, связанной с каждым именем.
"""
users = {
	'ainstein': {
		'first': 'albert',
		'last': 'ainstein',
		'location': 'princeton',
	},
	
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}

# Делаем перебор данных из словаря.
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")
print()
