## Изменение, добавление и удаление элементов ##

### Изменение ###

"""
Чтобы изменить элемент в списке, нужно указать имя списка и индекс
в квадратных скобках. Затем указать новое значение для присвоения
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
print()

### Добавление в конец списка методом append() ###
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print()

# Методом append() можно добавлять элементы даже в пустой список
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('honda')
motorcycles.append('suzuki')
print(motorcycles)
print()

### Вставка элементов в любое место методом insert() ###
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print()

### Удаление элементов списка функцией del ###
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
print()

### Удаление элементов списка метода pop() ###

"""
Метод pop() удаляет элемент из списка, но позволяет с ним работать
в отличие от функции del, которая полность удаляет элемент.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
print()

# Так можно выводить сообщение, например о купленном мотоцикле
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print()

### Извлечение элементов из произвольной позиции списка ###
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print()

"""
Если удаляешь элемент, без дальнейшего использования, то del 
Если удаляешь элемент, с дальнейшим использованием, то pop()
"""

### Удаление элементов по значению ###
# Если позиция элемента не известна, то remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print()

"""
Метод remove() также может использоваться для работы со значением,
которое удаляется из списка.
Так, например, можно указать причину удаления.
"""

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

"""
Если есть вероятность, что значение повторно встречается в списке,
следует использовать цикл для определения того,
были ли удалены все дубликаты.
Циклы будут разобраны в Главе 7.
"""
