# Любимый фрукт: составь список любимых фруктов.
# Напиши серию независимых команд if для проверки наличия фруктов.
# Затем создай список с тремя любимыми фруктами favorite_fruits.
# Напиши пять команд if. Каждая команда должна проверять, входит ли фрукт в список
# Если фрукт входит в список, то надо писать следующее
# You really like ...!
fav_fruits = ['watermelon', 'banana', 'orange', 'grape', 'pomelo', 'guava', 'mango', 'pineapple']

if 'banana' and 'pomelo' in fav_fruits:
	print("Fruits available.")
if 'coconut' or 'orange' in fav_fruits:
	print("One item available.")
print()

favorite_fruits = ['lichi', 'peach', 'banana']

if 'peach' in favorite_fruits:
	print("You really like peach!")
if 'banana' in favorite_fruits:
	print("You really like banana!")
if 'orange' in favorite_fruits:
	print("You really like orange!")
if 'mango' in favorite_fruits:
	print("You really like mango!")
if 'lichi' in favorite_fruits:
	print("You really like lichi!")
print()
