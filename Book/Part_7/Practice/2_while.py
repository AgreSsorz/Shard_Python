"""
Топпинг для пиццы:
написать цикл, который предлагает пользователю вводить дополнение для пиццы
до тех пор, пока не будет введено значение 'exit'.
При вводе каждого дополнения вывести сообщение о том,
что это дополнение включено в заказ.
"""

prompt = "What a topping do you want? "
prompt += "\nEnter 'exit' for leave program. "

while True:
	topping = input(prompt)
	
	if topping == 'exit':
		break
	else:
		print(f"{topping.title()} is included in the order.")
print()

"""
Билеты в кино:
кинотеатр установил несколько вариантов цены на билеты в зависимости от
возраста поситителя.
Для посетителей младше 3-х лет билет бесплатный.
Для посетителей от 3-х до 12 лет, билет стоит 10$.
Для посетителей больше 12 лет, билет стоит 15$.

Напиши цикл, который предлагает пользователю ввести свой возраст
и выводит цену билета.
"""
# Спрашиваем пользователя его возраст
prompt = "How old are you? "
prompt += "\nEnter 'exit' for leave program. "

# Начало цикла
while True:
	user_input = input(prompt)
	
	# Выходим из программы
	if user_input == 'exit':
		break
	# Преобразуем строку в числовое значение
	age = int(user_input)
	# Проверяем, может ли посетитель получить бесплатный билет
	if (age < 3):
		print("Here's your free ticket.")
	# Выдаём посетителю билет за 10 долларов
	elif (age > 3) and (age < 12):
		print("Your ticket costs $10.")
	# Выдаём посетителю билет за 15 долларов
	else:
		print("Your ticket costs $15.")
print()
