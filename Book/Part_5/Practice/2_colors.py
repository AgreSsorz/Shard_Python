# Цвета 1: представь, что в твоей игре был подбит вражеский корабль.
# Создай переменную с именем alien_color
# и присвой ей значение green, yellow или red.
alien_color = 'yellow'

# Напиши команду if для проверки того, что переменная содержит значение green.
# Если условие Истинно, то игрок получает 5 очков.
if 'green' in alien_color:
	print("+5 points")

# Напиши команду if, для проверки Истинного значения
if 'yellow' in alien_color:
	print("+15 points")

# Цвета 2: создай переменную с любым из трёх цветов и создай цепочку if-else.
alien_color = 'red'

if 'green' in alien_color:
	print("Nothing...")
else:
	print("You killed enemy.")

# Цвета 3: преобразуй предыдущую цепочку в if-elif-else.
# Дай игроку 5 очков за green, 10 очков за yellow и 15 за red.
alien_color = 'green'

if 'green' in alien_color:
	print("+5 points")
elif 'yellow' in alien_color:
	print("+10 points")
else:
	print("+15 points")
