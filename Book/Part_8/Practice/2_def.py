"""
Футболка:
написать функцию make_shirt(), которая получает размер футболки и текст,
который должен быть напечатан на ней.

Функция должна выводить сообщение с размером и текстом.

Вызвать функцию с использованием позиционных аргументов.

Вызвать функцию с использованием именованных аргументов.
"""

def name_shirt(size_shirt, text_shirt):
	print(f"\nI have a shirt {size_shirt.upper()} size with text: {text_shirt}.")

name_shirt('l', 'I like my shirt!')
print()

def name_shirt(text_shirt, size_shirt='m'):
	print(f"\nI have a shirt {size_shirt.upper()} size with text: {text_shirt}.")

name_shirt(text_shirt='I like my shirt!')
print()

"""
Большие футболки:
изменить текущую функцию, чтобы по умолчанию футболки имели размер L и на них
выводился текст: I love Python!
"""

def name_shirt(text_shirt='I love Python!', size_shirt='xxl'):
	print(f"\nI have a shirt {size_shirt.upper()} size with text: {text_shirt}.")

name_shirt()
print()
