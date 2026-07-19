# Длинный комментарий

""" 
Люди: начинаем с уже известной программы (1_dicts.py).
Создаём два новых словаря, представляющих разных людей.
И сохранить все три словаря в списке с именем people.
Перебрать элементы списка людей.
В процессе перебора вывести всю информацию о каждом из людей.
"""

human_1 = {
	'first_name': 'howard',
	'last_name': 'lovecraft',
	'age': 46,
	'city': 'providence'
}

human_2 = {
	'first_name': 'edgar',
	'last_name': 'po',
	'age': 40,
	'city': 'boston'
}

human_3 = {
	'first_name': 'august',
	'last_name': 'derleth',
	'age': 62,
	'city': 'wisconsin'
}

people = [human_1, human_2, human_3]

for human in people:
	print(f"\nFirst name: {human['first_name'].title()}")
	print(f"Last name: {human['last_name'].title()}")
	print(f"Age: {human['age']}")
	print(f"Location: {human['city'].title()}")
	# print(human)
print()

"""
Домашние животные: создать несколько словарей с кличками животных.
В каждом словаре сохранить тип животного и его владельца.
Сохранить словари в списке pets.
Перебрать элементы списка, выводя всю информацию о каждом животном.
"""

vasya = {
	'name': 'vasya',
	'tipe': 'cat',
	'owner': 'roman',
}

jerry = {
	'name': 'jerry',
	'tipe': 'mouse',
	'owner': 'nikita',
}

spike = {
	'name': 'spike',
	'tipe': 'dog',
	'owner': 'maxim',
}

pets = [vasya, jerry, spike]

for animal in pets:
	print(f"\nИмя: {animal['name'].title()}" 
		+ f"\tТип животного: {animal['tipe']}" 
		+ f"\tВладелец: {animal['owner'].title()}")
print()
