## Возвращаемое значение ##
"""
Функция не обязана выводить результаты своей работы напрямую.
Вместо этого она может обработать данные, а затем вернуть значение
или набор сообщений.

Значение, возвращаемое функцией, называется возвращаемым значением.
Команда return передаёт значение из функции в точку программы,
в которой эта функция была вызвана.

Возвращаемые значения помогают переместить большую часть рутинной работы
в нашей программе в функции, чтобы упростить код программы.
"""

### Возвращение простого значения ###

"""
Получим имя и фамилию, и возвратим аккуратно отформатированное полное имя:
"""

def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print()

### Необязательные аргументы ###
"""
Иногда бывает удобно сделать аргумент необязательным, чтобы разработчик,
использующий функцию, мог передать дополнительную информацию только в том
случае, когда он этого хочет.

Стоит воспользоваться значением по умолчанию.

Расширим предыдущую функцию:
"""

def get_formatted_name(first_name, middle_name, last_name):
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
print()

"""
Укажем необязательный аргумент:
"""
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
print()

### Возвращение словаря ###
"""
Функция может вернуть любое значение, которое потребуется,
в том числе и более сложную структуру данных, будь то список или словарь.
"""

def build_person(first_name, last_name):
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)
print()

"""
Расширим функцию, чтобы она принимала возраст:
"""
def build_person(first_name, last_name, age=None):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
print()

### Использование функции в цикле while ###
def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break
		
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")
print()
