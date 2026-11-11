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
