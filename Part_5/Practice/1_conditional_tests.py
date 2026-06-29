# Проверка условий: написать последовательность условий из 5 штук.

# создаю список из овощей и фруктов по пять штук
vegetables_and_fruits = ['carrot', 'potato', 'onion', 'green', 'redish', 'watermelon', 'pineapple', 'banana', 'orange', 'peach']
# делаю вывод содержимого списка
print(vegetables_and_fruits)
print()

# Первое условие
if 'carrot' in vegetables_and_fruits:
	print("Yay!")
else:
	print("Nope")	
print()

# Второе условие
if 'potato' and 'green' in vegetables_and_fruits:
	print("It's contained in list.")
print()
	
# Третье условие
if 'onion' and 'cucumber' in vegetables_and_fruits:
	print("It's contained in list.")
else:
	print("Cucumber not found in list.")
print()

# Четвёртое условие
if 'watermelon' or 'banana' in vegetables_and_fruits:
	print("Let's cook!")
print()

# Пятое условие	
if 'maracuya' or 'pineapple' in vegetables_and_fruits:
	print("Need more ingridients!")
else:
	print("Let's cook!")
