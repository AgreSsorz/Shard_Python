""" Модуль с классом Car для файла 4_mycar.py """

class Car():
	""" Простая модель автомобиля. """
	def __init__(self, make, model, year):
		""" Инициализируем атрибуты автомобиля. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
	
	def get_descriptive_name(self):
		""" Аккуратно возвращаем описание автомобиля. """
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
	
	def read_odometer(self):
		""" Выводим пробег машины в милях. """
		print(f"This car has {self.odometer_reading} miles on it.")
	
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

class Battery():
	""" Простая модель аккумулятора электромобиля. """
	def __init__(self, battery_size=75):
		self.battery_size = battery_size
	
	def describe_battery(self):
		""" Выводим информацию о мощности аккумулятора. """
		print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
	""" Представляет аспекты машины, специфические для е-машин. """
	def __init__(self, make, model, year):
		""" Инициализируем атрибуты класса-родителя. """
		super().__init__(make, model, year)
		self.battery = Battery()
