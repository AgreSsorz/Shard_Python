## Упорядочение списка ##

# Метод sort() позволяет сортировать список по алфавиту
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
print()

# sort(reverse=True) сортирует список в обратном порядке
# Порядок элементов меняется на постоянной основе в обоих случаях
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars)
print()

# Функция sorted() если требуется временная сортировка 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print()

print("\nHere is the sorted list:")
print(sorted(cars))
print()

# Здесь также можно применить обратную сортировку sorted(reverse=True)

# Метод reverse() выводит список в обратном порядке, но без сортировки
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
print()

# Метод len() позволяет определить длину списка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(len(cars))
print()

# Методом len() можно проверить список на возможные ошибки
