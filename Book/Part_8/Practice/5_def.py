"""
Сэндвичи:
Написать функцию, которая получает список компонентов сэндвича.
Функция должна иметь один параметр для любого количества значений,
переданных при вызове функции, и выводить описание заказанного сэндвича.
Вызвать функцию три раза с разным количеством аргументов.
"""
def make_sandwich(*components):
	print(components)

make_sandwich('bread', 'tomatoes cherry', 'cucumber', 'majonese')
make_sandwich('bread', 'cucumber', 'salad iceberg', 'onion', 'greens')
make_sandwich('bread', 'majonese', 'tomatoes', 'onion', 'ketchup')
print()

"""
Профиль:
Начать с копии программы с функцией build_profile(), но создать свои данные
для трёх личностей.
"""
def build_profile(first, last, **user_info):
	""" Строим словарь с информацией о пользователе. """
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info
	
user_profile = build_profile(
'yan',
'kolechov',
location='Tumen',
birthday='13 August 1972',
)
print(user_profile)

user_profile = build_profile(
'alex',
'luchik',
location='Krasnodar',
birthday='24 October 1967',
profession='driver',
)
print(user_profile)

user_profile = build_profile(
'yuliya',
'panarenko',
location='Ostov',
birthday='5 June 1995',
profession='graphic designer',
)
print(user_profile)
print()

"""
Автомобили:
Написать функцию для сохранения информации об автомобиле в словаре.
Функция всегда должна возвращать производителя и название модели,
но при этом она может получать произвольное количество именованных аргументов.
Вызвать функцию с передачей обязательной информации
и ещё двух пар имя-значение.
Вывести возвращаемый словарь и убедиться в том, что вся информация
была сохранена.
"""
def making_car(name, model, year, **car_info):
	car_info['brand'] = name
	car_info['car_model'] = model
	car_info['year_of_release'] = year
	return car_info
	
car_profile = making_car(
'Chevrolet',
'Impala',
'1967',
engine = 'V8',
color = 'Tuxedo Black',
available = True,
)
print(car_profile)

car_profile = making_car(
'Ford',
'Mustang',
'1967',
engine = 'V8',
color = 'Bloom Red',
available = False,
)
print(car_profile)

car_profile = making_car(
'Dodge',
'Charger',
'1967',
engine = 'Hemi V8',
color = 'Dark Blue with white lines',
available = True,
)
print(car_profile)
print()
