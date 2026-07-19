## Использование команд if со списками ##
"""
В следующем примере с пиццерией, программа выводит сообщение каждый раз,
когда пицца снабжается топпингом в процессе приготовления.
"""
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
print()

"""
А если в пиццерии вдруг закончился зелёный перец,
то команда if в цикле for может правильно обработать эту ситуацию.
"""
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
print()

### Проверка наличия элементов в списке ###
"""
В обычной ситуации, мы заранее знаем, что в списке есть хотя бы один элемент.
Но скоро мы предоставим пользователю вводить информацию,
находящуюся в списке, поэтому мы уже не можем предполагать,
что при каждом выполнении цикла в списке есть хотя бы один элемент.
В такой ситуации перед выполнением цикла for будет полезно проверить,
а есть ли вообще в списке хоть один элемент.
Если список пуст, программа предлагает пользователю подтвердить,
что он хочет базовую пиццу без топпингов.
Если список не пуст, пицца готовится так же, как и раньше.
"""
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
print()

### Множественные списки ###
"""
Посетители способны заказать что угодно, если речь идёт о топпингах к пицце.
Проверим наличие нестандартных дополнений перед тем, как готовить пиццу.
Первый список содержит перечень доступных топпингов,
а второй содержит список топпингов, заказанных клиентом.
"""
available_toppings = [
'mushrooms', 'olives', 'green peppers',
'pineapple', 'extra cheese', 'pepperoni'
]

requested_toppings = [
'mushrooms', 'french fries', 'extra cheese'
]

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
print()
