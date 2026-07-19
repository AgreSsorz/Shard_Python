## Работа с частью списка ##
"""
Помимо обращений к элементам списка через индексы, в Python можно 
работать с конкретным подмножеством элементов списка.
Это называется Сегментами.
"""
### Создание сегмента (slice) ###
# Чтобы создать сегмент на основе списка, надо задать индексы первого и 
# последнего элемента [first : second]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3])
print()
# Здесь выводится только имена трёх игроков из общего списка.

# Подмножество может включать любую часть списка.
# Если первый индекс сегмента не указан, отсчёт будет сначала списка.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[:4])
print()

"""
Если не указан второй индекс сегмента, то отсчёт будет до конца от 
первого указанного индекса сегмента.
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[2:])
print()

# Помни, что отрицательные индексы тоже работают.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[-3:])
print()

### Примечание ###
"""
В квадратные скобки, определяющие сегмент, можно поместить третье 
значение. Это значение, если оно присуствует, сообщает Python, сколько 
элементов следует пропускать при выборе элементов 
в заданном диапазоне.
"""
### Перебор содержимого сегмента ###
# Он осуществляется с помощью сегмента в цикле for.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print()	
# Таким образом, вместо перебора всех имён, мы ограничиваемся тремя.

### Копирование списка ###
"""
Часто разработчик создаёт новый список на основе старого, поэтому 
копирование списков, является нормальной процедурой.
"""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # копируем список на основе существующего
# new_list = old_list[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
print()
