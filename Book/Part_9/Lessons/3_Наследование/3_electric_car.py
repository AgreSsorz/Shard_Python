## Наследование ##
"""
Работа над новым классом не обязана начинаться с нуля.
Можно воспользоваться наследованием.
Один класс, наследующий от другого, автоматически получает все атрибуты
и методы первого класса.
Исходный класс называется родителем, а новый класс — потомком.
Класс потомок наследует атрибуты и методы родителя, но при этом также может
определять собственные атрибуты и методы.
"""

### Метод __init()__ класса-потомка ###
"""
При написании нового класса на базе существующего класса часто приходится
вызывать метод __init()__ класса-родителя.
При этом происходит инициализация любых атрибутов, определённых в методе
__init()__ родителя, и эти атрибуты становятся доступными для класса-потомка.
"""
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

class ElectricCar(Car):
	""" Представляет аспекты машины, специфические для е-машин. """
	def __init__(self, make, model, year):
		""" Инициализируем атрибуты класса-родителя. """
		super().__init__(make, model, year)
		
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print()

### Определение атрибутов и методов класс-потомка ###
"""
После создания класса-потомка, наследующего от класса-родителя,
можно переходить к добавлению новых атрибутов и методов, необходимых для того,
чтобы потомок отличался от родителя.

Добавим атрибут, свойственный электромобилям:
"""

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

class ElectricCar(Car):
	""" Представляет аспекты машины, специфические для е-машин. """
	def __init__(self, make, model, year):
		""" Инициализируем атрибуты класса-родителя. """
		super().__init__(make, model, year)
		self.battery_size = 75
		
	def describe_battery(self):
		""" Выводим информацию о мощности аккумулятора. """
		print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
print()
### Переопределение методов класса-родителя ###
"""
Любой метод родительского класса, который в моделируемой ситуации делает не
то, что нужно, можно переопределить.
Для этого в классе-потомке определяется метод с тем же именем, что и у метода
класса-родителя. Python игнорирует метод родителя и обращает внимание
только на метод, определённый в потомке.

Допустим, в классе Car имеется метод fill_gas_tank().
Для электромобилей заправка бензином бессмысленна, поэтому этот метод
логично переопределить:

class ElectricCar():
...
	def fill_gas_tank(self):
		У электромобилей нет бензобака.
		print("This car doesn't need a gas tank!")
"""

### Экземпляры как атрибуты ###
"""
При моделировании явлений реального мира в программах классы нередко
дополняются всё большим количеством подробностей.
Списки атрибутов и методов растут, и через какое-то время файлы становятся
длинными и громоздкими.
В такой ситуации часть одного класса нередко можно записать в виде отдельного
класса. Большой код разбивается на меньшие классы, которые работают во
взаимодействии друг с другом.

Например, при дальнейшей доработке класса ElectricCar может оказаться,
что в нём появилось слишком много атрибутов и методов, относящихся к батарее.
В таком случае можно остановиться и переместить все эти атрибуты и методы
в отдельный класс с именем Battery.
Затем экземпляр Battery становится атрибутом класса ElectricCar:
"""
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
		
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
