# Hello, Admin: создать список из пяти или более пользователей,
# который включает имя admin.
# Представь, что ты пишешь код, который выводит приветственное сообщение
# для каждого пользователя после входа на сайт.
# Перебери элементы списка и выведи сообщение для каждого пользователя:
	# Hello, Admin! Would you like to see a status report?
	# Hello, User! Thank you for logging in again.
users = [
'denis', 'daniil', 'caroline', 'admin', 'ivan', 'oleg', 'victor'
]

for user in users:
	if 'admin' in user:
		print("Hello, Admin! Would you like to see a status report?")
	else:
		print(f"Hello, {user.title()}! Thank you for logging in again.")

print()

# Без пользователей: добавь команду if, которая проверит, что список не пуст.
# Если список пуст, то вывод смс We need to find some users!
# Удали из списка все имена пользователей и убедись в том,
# что программа выводит правильное сообщение.

users = []


if user in users:
	print("Hello, Users!")
else:
	print("We need to find some users!")

print()

# Проверка имён пользователей: 
# Создать список current_users, содержащий пять и более имён.
# Создать другой список new_users с предыдущими именами + два новых.
# Перебрать список new_users и если найдутся похожие имена,
# посоветовать пользователю выбрать другое имя.
# Если имя доступно, вывести соответствующее сообщение.
# Проследить за тем, чтобы был соблюдён регистр символов.
# (для этого создаётся копия current_users) для проверки нижнего регистра.
