# Сохранить три вида пиццы в списке и использовать цикл for для вывода всех
pizzaz = ['pepperoni', 'manhathan', 'four_cheese']
for pizza in pizzaz:
	print(pizza)
print()

# Сделать так, чтобы для каждой пиццы, выводилось сообщение I love ... pizza!
pizzaz = ['pepperoni', 'manhathan', 'four_cheese']
for pizza in pizzaz:
	print(f"I love {pizza} pizza!")
print()

# Добавить дополнительное сообщение в конец цикла for
pizzaz = ['pepperoni', 'manhathan', 'four_cheese']
for pizza in pizzaz:
	print(f"I love {pizza} pizza!")
print("\nI really love pizza!") # перенос строки с помощью \n
print()
