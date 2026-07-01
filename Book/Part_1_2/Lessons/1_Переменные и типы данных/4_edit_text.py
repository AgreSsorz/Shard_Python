## Оформление строк ##

# Пропуски (whitespace) нужны, чтобы пользователь легко читал выводимый текст
# для включения в текст позиции табуляции используется комбинация символов \t
print("Python")
print ("\tPython")

# Разрывы строк добавляются с помощью \n
print("Languages:\n\tPython\n\tLua\n\tJavaScript\nC++")

# Удаление пропусков
# Python может искать лишние пропуски у левого и правого края строки
# lstrip() для левого края; rstrip() для правого края;
# strip() удаляет пробельные символы и разрывы строк
favorite_language = " python "

print(favorite_language)
# убираем пропуск справа и записываем значение в ту же переменную
favorite_language = favorite_language.rstrip()
# выводим новое значение старой переменной
print(favorite_language)
