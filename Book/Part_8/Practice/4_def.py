"""
Сообщения:
Создать список с серией коротких сообщений.
Передать список функции show_messages(), которая выводит текст каждого
сообщения в списке.
"""

def show_messages(source_messages):
	for message in source_messages:
		msg = f"{message}"
		print(msg)

messages_serie = [
'Hello, User!',
'Welcome back to learning Python.',
'What did you do today?'
]
show_messages(messages_serie)
print()

"""
Отправка сообщений:
Начать следует с копии предыдущей программы.
Напиши функцию send_messages(), которая выводит каждое сообщение
и перемещает его в новый список с именем sent_messages.
После вызова функции нужно вывести оба списка, чтобы проверить,
что перемещение прошло успешно.
"""
def show_messages(source_messages):
	for message in source_messages:
		msg = f"{message}"
		print(msg)

def send_messages(source_messages):
	sent_messages = []
	
	while source_messages:
		current_message = source_messages.pop()
		print(f"Sending message: {current_message}")
		sent_messages.append(current_message)
	
	sent_messages.reverse()
	
	return sent_messages
# Вызов функции
print("Исходник до отправки:", messages_serie)
show_messages(messages_serie)

# Вызываем функцию и сохраняем результат
sent_messages = send_messages(messages_serie)

print("Исходник после отправки:", messages_serie)
print("Новый список:", sent_messages)

# Проверка
if messages_serie != sent_messages:
	print("Success sending!")
print()

"""
Архивированные сообщения:
Скопировать предыдущую функцию.
Вызвать функцию send_messages() для копии списка сообщений.
После вызова вывести оба списка, чтобы понять, остались ли в исходном списке
все сообщения.
"""

messages_serie = [
'Hello, User!',
'Welcome back to learning Python.',
'What did you do today?'
]

def send_messages(source_messages):
	sent_messages = []
	
	while source_messages:
		current_message = source_messages.pop()
		print(f"Sending message: {current_message}")
		sent_messages.append(current_message)
	
	sent_messages.reverse()
	
	return sent_messages
# Вызов функции
print("Исходник до отправки:", messages_serie)
show_messages(messages_serie)

# Вызываем функцию и сохраняем результат
sent_messages = send_messages(messages_serie[:])

print("Исходник со всеми смс:", messages_serie)
print("Новый список:", sent_messages)
