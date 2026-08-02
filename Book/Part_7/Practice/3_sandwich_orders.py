"""
Сэндвичи:
создать список с именем sandwich_orders и заполнить его названиями сэндвичей.

Создать пустой список с именем finished_sandwiches.

В цикле перебрать элементы первого списка и вывести сообщение
для каждого элемента.

После этого, каждый элемент списка, перемещается в список finished_sandwiches.

Вывести сообщение с перечислением всех готовых сэндвичей.
"""
# Список с пятью популярными сэндвичами
# sandwich_orders = [
	# 'club sandwich',
	# 'sandwich with bacon, lettuce and tomato',
	# 'reuben',
	# 'philly cheeseteak',
	# 'cubano',
# ]
# print(sandwich_orders)

# Пустой список с готовыми сэндвичами
# finished_sandwiches = []
# Перебор первого списка, добавление элементов во второй и вывод сообщения
# while sandwich_orders:
	# sandwich = sandwich_orders.pop()
	# finished_sandwiches.append(sandwich)
	
	# print(f"I made your {sandwich.title()}.")
	
# Вывод готовых сэндвичей
# print("\nSandwiches done:")
# for sandwich in finished_sandwiches:
	# print(sandwich.title())
# print()

"""
Без пастрами:
используя список sandwich_orders, проследи, чтобы значение 'pastrami',
встречалось как минимум три раза.

Добавь в начале программы код для вывода сообщения о том,
что пастрами больше нет и напиши цикл для удаления всех таких значений
из этого списка.
Убедись в том, что значение 'pastrami' отстутствует в списке finished_sandwich
"""

sandwich_orders = [
	'pastrami',
	'club sandwich',
	'sandwich with bacon, lettuce and tomato',
	'pastrami',
	'reuben',
	'philly cheeseteak',
	'pastrami',
	'cubano',
]

print(sandwich_orders)

print("\nNo more Pastrami!")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:
	print(sandwich)
print()

"""
Отпуск мечты:
написать программу-опрос, в которой мы спрашиваем имя пользователя
и место, где бы он хотел отдохнуть.
Включить блок кода для вывода результатов опроса.
"""

responses = {}

# Установка флага продолжения опроса
polling_active = True

while polling_active:
	# Запрос имени и ответа пользователя
	name = input("\nWhat is your name? ")
	response = input("Where will you go in vacation? ")
	
	# Ответ сохраняется в словаре
	responses[name] = response
	
	# Проверка продолжения опроса
	repeat = input("Would you like to let another person respond?(yes/no) ")
	if repeat == 'no':
		polling_active = False

# Опрос завершён, вывести результаты
print("\n| --- | Poll Results | --- |")
for name, response in responses.items():
	print(f"{name} would you like to vacation in {response.title()}.")
print()
