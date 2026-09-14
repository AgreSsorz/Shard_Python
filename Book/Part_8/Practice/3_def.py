"""
Названия городов:
написать функцию city_country(), которая получает название города и страну.
Функция должна возвращать строку в формате Santiago, Chile.
Вызвать функцию для трёх пар город-страна и вывести возвращённое значение.
"""

def city_country(name_city, country):
	string_name = f"{name_city} {country}"
	return string_name.title()
	
msg = city_country('tomsk', 'russia')
print(msg)
print()

"""
Альбом:
написать функцию make_album(), которая строит словарь с описанием музыкального
альбома. Функция должна получать имя исполнителя и название альбома
и возвращать словарь, содержащий эти два вида информации.

Использовать функцию для создания трёх словарей, представляющих разные альбомы.
Вывести все возвращаемые значения, чтобы показать правильность сохранения инфы.

Добавить в make_album() дополнительный параметр для сохранения
количества дорожек в альбоме, по умолчанию значение None.
Если в строку вызова включено значение количества дорожек, то добавить
это значение в словарь альбома.
Создать один вызов подобной функции.
"""

def make_album(group_name, album_name):
	album = {'group': group_name, 'album': album_name}
	return album
	
album = make_album('shadow of intent', 'elegy')
print(album)

album = make_album('sagath', 'кровь из носа')
print(album)

album = make_album('б.а.у.', 'советский союз')
print(album)
print()

def make_album(group_name, album_name, songs=None):
	album = {'group': group_name, 'album': album_name}
	if songs:
		album['songs'] = songs
	return album

album = make_album('shadow of intent', 'elegy', songs=9)
print(album)
print()

"""
Пользовательские альбомы:
начать с программы Альбом. Написать цикл while, в котором пользователь вводит
исполнителя и название альбома.
Затем в цикле вызывается функция make_album() для введённых пользователей
и выводится созданный словарь.
Нужно предусмотреть признак завершения в цикле while.
"""
# Нормальный вывод #
def make_album(group_name, album_name):
	album = f"{group_name} {album_name}"
	return album.title()
	
while True:
	print("\nPlease enter Group name: ")
	print("(enter 'q' at any time to quit)")
	
	group_name = input("Group name: ")
	if group_name == 'q':
		break
		
	album_name = input("Album name: ")
	if album_name == 'q':
		break
	
	formatted_album = make_album(group_name, album_name)
	print(f"\nYour favorite album is, {formatted_album}!")
print()

# Вывод в виде словаря #
def make_album(group_name, album_name):
	album = {'group': group_name, 'album': album_name}
	return album

while True:
	print("\nPlease enter Group name: ")
	print("(enter 'q' at any time to quit)")
	
	group_name = input("Group name: ")
	if group_name == 'q':
		break
		
	album_name = input("Album name: ")
	if album_name == 'q':
		break
	
	formatted_album = make_album(group_name, album_name)
	print(f"\nYour favorite album is, {formatted_album}!")
print()
