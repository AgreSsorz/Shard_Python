"""
Посетители:
Начать с программы Ресторан.
Добавить атрибут number_served со значением по умолчанию 0;
Он представляет количество обслуженных посетителей.
Создать экземпляр с именем restaurant и вывести значение нового атрибута.
Изменить значение этого атрибута и снова вывести.

Добавить метод с именем set_number_served(), позволяющий задать количество
обслуженных посетителей.
Вызвать метод с новым числом и снова вывести значение.

Добавить метод с именем increment_number_served(), который увеличивает
количество обслуженных посетителей на заданную величину.
Вызвать этот метод с любым числом.
"""
class Restaurant():
	""" Создаём модель ресторана с помощью метода __init__. """
	def __init__(self, restaurant_name, cuisine_type):
		""" Инициализируем атрибуты после self. """
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0
	
	""" Создаём метод describe_restaurant. """
	def describe_restaurant(self):
		""" Описание ресторана. """
		print(f"Добро пожаловать в {self.name}!")
	
	""" Создаём метод open_restaurant. """	
	def open_restaurant(self):
		""" Указываем на открытие ресторана. """
		print(f"Ресторан {self.type}!")
		
	def set_number_served(self, visitors):
		""" Добавляем метод с возможностью изменять количество посетителей. """
		self.update_visitors = visitors
		print(f"Количество обслуженных посетителей: {self.update_visitors}")
	
	def increment_number_served(self, visitors):
		""" Добавляем метод, который увеличивает число посетителей. """
		self.update_visitors += visitors
		print(f"Количество обслуженных посетителей: {self.update_visitors}")

""" Создаём экземпляр ресторана Хачу Пури. """
my_restaurant = Restaurant('Ресторан Хачу Пури', 'открыт')

""" Выводим атрибуты. """
print(f"{my_restaurant.name} {my_restaurant.type}")
print()
print(f"Количество обслуженных посетителей: {my_restaurant.number_served}.")

my_restaurant.number_served = 23
print(f"Количество обслуженных посетителей: {my_restaurant.number_served}.")
print()

""" Выводим методы. """
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()

my_restaurant.set_number_served(44)
my_restaurant.set_number_served(86)
print()

my_restaurant.increment_number_served(100)
my_restaurant.increment_number_served(2341)
print()

"""
Попытки входа:
Добавить атрибут login_attempts в класс User из упражнения Пользователи.
Написать метод increment_login_attempts(), увеличивающий значение
login_attempts на 1.
Написать другой метод с именем reset_login_attempts(),
обнуляющий значение login_attempts.

Создать экземпляр класса User и вызвать increment_login_attempts() несколько раз
Вывести значение login_attempts, чтобы убедиться в том, что значение было
изменено правильно, а затем вызвать reset_login_attempts().

Снова вывести login_attempts и убедиться в том, что значение обнулилось.
"""

class User():
	""" Создаём модель пользователя с помощью метода __init__. """
	def __init__(self, first_name, last_name, birthday, location):
		""" Инициализируем атрибуты пользователя после self. """
		self.fname = first_name
		self.lname = last_name
		self.birth = birthday
		self.loc = location
		""" Попытки входа по умолчанию. """
		self.login_attempts = 0
	
	""" Создаём метод для вывода информации о пользователе. """
	def describe_user(self):
		print(f"Имя: {self.fname.title()} \nФамилия: {self.lname.title()}"
		f"\nГод рождения: {self.birth} \nГород проживания: {self.loc.title()}")

	""" Создаём метод для приветствия пользователя. """
	def greet_user(self):
		print(f"Добро пожаловать {self.fname.title()}!"
		f"\nПопыток входа: {self.login_attempts}")
	
	""" Создаём метод увеличивающий значение на 1. """	
	def increment_login_attempts(self):
		self.login_attempts += 1
		print(f"Попыток входа: {self.login_attempts}.")
		
	""" Создаём метод, обнуляющий попытки входа пользователя. """
	def reset_login_attempts(self):
		self.login_attempts = 0
		print(f"Попыток входа: {self.login_attempts}.")
		
""" Создаём экземпляры пользователей. """
user1 = User('юлия', 'смирнова', '14 марта 1964 года', 'санкт-петербург')

""" Вызываем методы для пользователя. """
user1.greet_user()
user1.describe_user()
print()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print()

user1.reset_login_attempts()
user1.increment_login_attempts()
print()
