## Использование переменных в строках ##

first_name = "ada"
last_name = "lovelace"

# Тройные кавычки создают длинный комментарий.
"""
в python 3.5 склеивание происходило с помощью метода format(word1, word2)
! с python 3.6 склеиваем две строки в одну с помощью f-строк !
"""
full_name = f"{first_name} {last_name}"

print(full_name)
print()

# с помощью f-строк можно строить сложные предложения
first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"

message = f"Hello, {full_name.title()}!"

print(message)
print()

"""
пропуски (whitespace) нужны, чтобы пользователь легко читал выводимый текст
для включения в текст позиции табуляции используется комбинация символов \t
"""

print("Python")
print ("\tPython")

# разрывы строк добавляются с помощью \n
print("Languages:\n\tPython\n\tLua\n\tJavaScript\nC++")
