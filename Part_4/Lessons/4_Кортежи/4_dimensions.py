## Кортежи (tuples) ##
# Если кратко, то это неизменяемые списки.
# Кортеж выглядит как список, за исключением одного момента, у изменяемого списка скобки квадратные, а у неизменяемого, скобки круглые.
# После определения кортежа, мы также можем обращаться к его элементам 
# по индексам.
dimensions = (200, 50)
print(dimensions[0]) # обращение к индексу такое же, как у списка.
print(dimensions[1])
# dimensions[0] = 250 # вызовет ошибку
# Кортеж может состоять из одного элемента.
my_t = (3,)

### Перебор всех значений в кортеже ###
# Для перебора используется цикл for, как в случае со списками.
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)
print()

### Замена кортежа ###
# Элементы кортежа неизменяемы, но можно присвоить новое имя переменной, в которой хранится кортеж.
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimensions)
print()

dimensions = (400, 100)	
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
print()

	
