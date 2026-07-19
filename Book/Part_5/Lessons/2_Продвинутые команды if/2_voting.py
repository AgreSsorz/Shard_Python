## Продвинутые команды if ##
"""
Простейшая форма команды if состоит из одного условия и одного действия.
В первой строке размещается условие, а в блоке с отступом любое действие.
Если условие Истинно, то Python выполняет код в блоке после команды if,
а если Ложно, то этот код игнорируется.
"""
age = 19

if age >= 18:
	print("You are old enough to vote!")
print()
"""
Отступы в командах if играют ту же роль, что и в циклах for.
Если условие Истинно, то все строки с отступом после команды if выполняются,
а если Ложно, то блок с отступом игнорируется.
"""
age = 19

if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
print()
# Если значение age меньше 18, то программа ничего не выводит.

### Команды if-else или Простая цепочка команды if ###
"""
Если условие Истинно, то выполняется код после if,
а если условие Ложно, то выполняется код после else.
"""
age = 17

if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
print()

### Команды if-elif-else или Сложная цепочка команды if ###
"""
Нередко команде нужно проверить несколько ситуаций.
Как раз для такого случая, в Python есть конструкция if-elif-else.
Python выполняет только один блок в этой цепочке, проверяя по порядку.
"""
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission cost is $40.")
print()

# Лучше использовать вариант короче.
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}.")
print()
"""
Таким образом, если вдруг понадобится изменить выходное сообщение,
то нужно будет отредактировать только одно сообщение, вместо трёх.
"""
# Код может содержать множество блоков elif, если условий больше трёх.

### Отсутствие блока else ###
# Python не требует, чтобы цепочка if-elif завершалась else.
# Следовательно, Ложного значения в этой цепочке может и не быть.
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20	
print(f"Your admission cost is ${price}.")
print()

### Проверка нескольких условий ###
# Цепочки if-elif-else эффективны, но они подходят для проверки одного условия.
"""
Когда нам надо проверить несколько условий, лучше применять цепочки if-if-if,
но без elif или else.
"""
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")
print()

"""
# Итог:
# Если нужно, чтобы выполнялось одно условие, то используй if-elif-else.
# Если нужно, чтобы выполнялось несколько условий, то используй if-if-if.
"""
