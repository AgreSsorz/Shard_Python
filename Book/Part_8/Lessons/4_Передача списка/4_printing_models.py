## Передача списка ##
"""
Часто при вызове функции удобно передать список имён, чисел или более сложных
вещей, типа словарей.
При передаче списка функция получает прямой доступ ко всему его содержимому.


Допустим, выведем приветствие для каждого пользователя из списка.
"""

def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
		
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
print()

### Изменение списка в функции ###
"""
Если мы передаём список функции, код функции сможет изменить список.
Все изменения, внесённые в список в теле функции, закрепляются,
что позволяет эффективно работать со списком даже при больших объёмах данных.
"""
# Код без функции
# Список 3д моделей, которые необходимо напечатать.
unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
completed_models = []

# Цикл, печатающий каждую модель по очереди.
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)
	
# Вывод всех готовых моделей.
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
print()

# Код с применением функций.
"""
Первая функция занимается печатью, а вторая выводит сводку с готовыми моделями.
"""
def print_models(unprinted_designs, completed_models):
	"""
	Иммитируем печать моделей, пока список не станет пустым.
	И каждая модель после печати перемещается в completed_models.
	"""
	while unprinted_designs:
		current_designs = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""
	Выводим информацию обо всех напечатанных моделях.
	"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pedant', 'dodecahedron']
completed_designs = []

print(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()

### Запрет изменения списка в функции ###
"""
Иногда нужно предотвратить изменение списка в функции.
Допустим, у нас имеется список моделей для печати и мы пишем функцию
для перемещения их в список готовых моделей.

Возможно, даже после печати всех моделей исходный список нужно оставить
для отчётности.
Но поскольку все имена моделей были перенесены из списка unprinted_designs,
остался только пустой список. Исходник утерян.

Проблема решается с помощью передачи функции копии списка вместо оригинала.
В этом случае все изменения, вносимые функцией в список, будут распространяться
только на копию, а оригинал списка останется неизменным.

Чтобы передать функции копию списка, следует сделать так:
имя_функции(имя списка[:])

Синтаксис сегмента [:] создаёт копию списка для передачи функции.

Если удаление элементов из списка unprinted_designs нежелательно,
то функцию print_models() можно вызвать так:
print_models(unprinted_designs[:], completed_models)
"""
