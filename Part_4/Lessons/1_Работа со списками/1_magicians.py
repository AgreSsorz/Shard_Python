## Работа со списками ##

### Перебор всего списка ###
# Цикл for нужен для перебора всего списка, даже с миллионом значений

# Выводим имена фокусников
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magicians)
print()

### Подробнее о циклах ###
# Циклы это первый шаг к автоматизации рутины.
# for magician in magicians
# Эта строка означает, что нужно взять первое значение из списка 
# magicians и сохранить его в переменной magician.
# Python берёт каждое значение из списка и кладёт его в переменную до тех 
# пор, пока элементы в списке не закончатся.
# Если после цикла for нет ничего, то программа завершается.

# Шпаргалка
# for название_переменной in название_списка
# for cat in cats

### Более сложные действия в циклах for ###
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
print()

# Тело цикла for может содержать сколько угодно строк кода
magicians = ['alice', 'david', 'carolina']
# Двоеточие в конце обозначает начало цикла
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	# вывод строки с переносом строки \n. Отступы и переносы важны 
	# для удобного чтения кода
	print(f"I can't wait to see your next trick, {magician.title()}.\n")
print()





