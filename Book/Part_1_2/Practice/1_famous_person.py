"""
Создать программу "Личное сообщение для Эрика"
name = "eric"
Hello, ... would you like to learn some Python today?
вывод имени в нижнем регистре
print(f"Hello, {name.lower()} would you like to learn some Python today?")
вывод имени в верхнем регистре
print(f"Hello, {name.upper()} would you like to learn some Python today?")
вывод имени с капитализацией начальных букв каждого слова
print(f"Hello, {name.title()} would you like to learn some Python today?")

Создать вывод цитаты с автором

print('Учитель своему ученику как то сказал, "Музыка, какой бы она не была - исцеляет, так что тебе должно быть всё равно на то, что тебе говорят слушать..."')

famous_person = "учитель"
message = f'{famous_person.title()} своему ученику как то сказал, "Музыка, какой бы она не была - исцеляет, так что тебе должно быть всё равно на то, что тебе говорят слушать..."'
print(message)
"""

name = " Ivan \t\n"
print(name)
# выводим имя с методом lstrip()
print(name.lstrip())
# выводим имя с методом rstrip()
print(name.rstrip())
# выводим имя с методом strip()
print(name.strip())
# выводим разом со всеми методами
name = name.lstrip().rstrip().strip()
print(name)
