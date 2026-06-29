# Сохранить пять стран в списке, в случайном порядке, а не по алфавиту
countries = ['russia', 'china', 'egypt', 'australia', 'ukraine']

# Вывести список
print(countries)
print()

# Используй функцию sorted() для вывода списка в алфавитном порядке
print(sorted(countries))
print()

# Снова вывести список, чтобы показать, что порядок исходный
print(countries)
print()

# Используй функцию sorted() для вывода в обратном порядке
countries_sorted = sorted(countries, reverse=True)
print(countries_sorted)
print()

# Снова вывести список, чтобы показать, что порядок исходный
print(countries)
print()

# Выводим список с изменением порядка с помощью reverse()
countries.reverse()
print(countries)
print()

# Выводим список с исходным порядком с помощью reverse()
countries.reverse()
print(countries)
print()

# Сортируем список методом sort()
countries.sort()
print(countries)
print()

# Сортируем список методом sort() в обратном порядке
countries.sort(reverse=True)
print(countries)
print()

# Выводим количество гостей с помощью метода len()
guests = ['denis', 'oleg', 'caroline', 'yura', 'tolya', 'nina']
print(len(guests))
