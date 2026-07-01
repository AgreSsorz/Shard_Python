# Считаем до 20 с помощью цикла for
# for value in range(1, 21):
	# print(value)
# print()

# Создать список чисел от 1 до 50_000 и воспользоваться циклом for для вывода
# fifty_thousands = list(range(1, 50_001))
# for number in fifty_thousands:
	# print(number)
# print()	

# Суммирование миллиона чисел: создать список чисел от 1 до 50000,
# затем воспользоваться функциями min() и max()
# и убедиться в том, что список заканчивается 50000.
# Вызвать функцию sum() и посмотреть как Python справится.
# fifty_thousands = list(range(1, 50_001))
# print(min(fifty_thousands))
# print(max(fifty_thousands))
# print(sum(fifty_thousands))

# Нечётные числа: воспользоваться третьим аргументом range()
# для создания списка нечётных чисел от 1 до 20.
# Вывести все числа списка с помощью цикла for
numbers_nechot = list(range(1, 21, 3))
for value in numbers_nechot:
	print(value)
print()

# Тройки: создать список чисел, кратных 3 от 3 до 30.
# Вывести числа с помощью цикла for
kratnos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for value in kratnos:
	print(value)
print()

# Кубы: сделать возведение в куб чисел от 1 до 10 и вывести с помощью for
cubes = []
for value in range(1, 11):
	cubes.append(value ** 3)
print(cubes)
print()

# Генератор кубов: для создания первых 10 кубов.
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
