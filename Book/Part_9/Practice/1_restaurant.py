"""
Ресторан:
Создать класс с именем Restaurant.
Метод __init__() должен содержать два атрибута restaurant_name и cuisine_type.
Создать метод describe_restaurant(), который выводит два атрибута,
и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.

На основе этого класса создать экземпляр с именем restaurant.
Вывести два атрибута по отдельности, затем оба метода. 
"""

class Restaurant():
	""" Создаём модель ресторана с помощью метода __init__. """
	def __init__(self, restaurant_name, cuisine_type):
		""" Инициализируем атрибуты после self. """
		self.name = restaurant_name
		self.type = cuisine_type
	
	""" Создаём метод describe_restaurant. """
	def describe_restaurant(self):
		""" Описание ресторана. """
		print(f"Добро пожаловать в {self.name}!")
	
	""" Создаём метод open_restaurant. """	
	def open_restaurant(self):
		""" Указываем на открытие ресторана. """
		print(f"Ресторан {self.type}!")

""" Создаём экземпляр ресторана Хачу Пури. """
my_restaurant = Restaurant('Ресторан Хачу Пури', 'открыт')

""" Выводим атрибуты. """
print(f"{my_restaurant.name} {my_restaurant.type}")

""" Выводим методы. """
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()

"""
Три ресторана:
Начинаем с предыдущего класса Restaurant.
Создать три разных экземпляра и вызвать для каждого метод describe_restaurant.
"""
class Restaurant():
	""" Создаём модель ресторана с помощью метода __init__. """
	def __init__(self, restaurant_name, cuisine_type):
		""" Инициализируем атрибуты после self. """
		self.name = restaurant_name
		self.type = cuisine_type
	
	""" Создаём метод describe_restaurant. """
	def describe_restaurant(self):
		""" Описание ресторана. """
		print(f"Добро пожаловать в {self.name}!")
	
	""" Создаём метод open_restaurant. """	
	def open_restaurant(self):
		""" Указываем на открытие ресторана. """
		print(f"Ресторан {self.type}!")
		
""" Ресторан грузинской кухни Сулугуни. """
restaurant_1 = Restaurant('Ресторан грузинской кухни Сулугуни', 'открыт')
restaurant_2 = Restaurant('Ресторан японской кухни Харакири', 'открыт')
restaurant_3 = Restaurant('Ресторан мексиканской кухни Кактусито', 'открыт')

""" Вызываем метод describe_restaurant() для каждого экземпляра. """
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
print()

"""
Пользователи:
Создать класс с именем User.
Создать два атрибута first_name и last_name, а затем ещё несколько атрибутов.
Написать метод describe_user(), который выводит сводку с информацией
о пользователе.
Создать ещё один метод greet_user(), который выводит персональное приветствие
для пользователя.

Создать несколько экземпляров разных пользователей.
Вызвать оба метода для каждого пользователя.
"""
class User():
	""" Создаём модель пользователя с помощью метода __init__. """
	def __init__(self, first_name, last_name, birthday, location):
		""" Инициализируем атрибуты пользователя после self. """
		self.fname = first_name
		self.lname = last_name
		self.birth = birthday
		self.loc = location
	
	""" Создаём метод для вывода информации о пользователе. """
	def describe_user(self):
		print(f"Имя: {self.fname.title()} \nФамилия: {self.lname.title()}"
		f"\nГод рождения: {self.birth} \nГород проживания: {self.loc.title()}")

	""" Создаём метод для приветствия пользователя. """
	def greet_user(self):
		print(f"Добро пожаловать {self.fname.title()}!")
		
""" Создаём экземпляры пользователей. """
user1 = User('юлия', 'смирнова', '14 марта 1964 года', 'санкт-петербург')
user2 = User('антон', 'логинов', '24 Апреля 1999 года', 'томск')
user3 = User('вероника', 'никитина', '3 Октября 2003 года', 'красноярск')

""" Вызываем оба метода для каждого пользователя. """
user1.greet_user()
user1.describe_user()
print()

user2.greet_user()
user2.describe_user()
print()

user3.greet_user()
user3.describe_user()
print()
