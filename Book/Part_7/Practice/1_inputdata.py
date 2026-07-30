"""
Прокат машин: написать программу, которая страшивает у пользователя,
какую машину он хотел бы напрокат.
Вывести сообщение с введёнными данными: Let me see if I can find you a Subaru.
"""
# Создаём список с машинами
cars = ['subaru', 'toyota', 'audi', 'dodge', 'pontiac']
# Спрашиваем пользователя, какую машину он хочет взять напрокат
msg_car = input("What do you like a car? Tell her: ")

# print(msg)
# Проверяем, есть ли названная машина в списке
if msg_car in cars:
	# Преобразуем название в нормальный регистр и выводим сообщение при наличии
	formatted_name = msg_car.title()
	print(f"\nLet me see if I can find you a {formatted_name}.")
else:
	# Выводим сообщение при отсутствии машины
	formatted_name = msg_car.title()
	print(f"{formatted_name} is unavailable.")

"""
Заказ стола: написать программу, которая страшивает у пользователя,
на сколько мест он хочет забронировать стол в ресторане.
Если введённое число больше 8, надо вывести сообщение об ожидании свободных.
Если меньше, то стол готов.
"""
# Уточним, сколько мест будет заказано.
table_order = input("How many places will be order? ")
# Преобразуем строку в число
table_order = int(table_order)
# Проверим, превышает ли число мест заданных параметров и выведем сообщения
if table_order > 8:
	print("\nAll tables are occupied.")
else:
	print("\nTable is done.")

"""
Числа кратные 10: запросить у пользователя число и сообщить,
кратно ли оно 10 или нет.
"""
# Спрашиваем пользователя его число
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
# Проверяем кратность
if number % 10 == 0:
	print(f"\nThe number {number} is even ten.")
else:
	print(f"\nThe number {number} is odd ten.")
