## Работа с классами и экземплярами ##
"""
Классы могут использоваться для моделирования реальных ситуаций.
После того, как класс будет написан, разработчик проводит большую часть времени
за работой с экземплярами, созданными на основе этого класса.

Одной из первых задач станет изменение атрибутов,
связанных с конкретным экземпляром.

Атрибуты экземпляра можно изменять напрямую или же написать методы,
изменяющие атрибуты по особым правилам.
"""

### Класс Car ###
""" Напишем класс, представляющий автомобиль. """
class Car():
	""" Простая модель автомобиля. """
	def __init__(self, make, model, year):
		""" Инициализируем атрибуты автомобиля. """
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
		""" Аккуратно возвращаем описание автомобиля. """
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()
		
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

""" Чтобы класс был более интересным, добавим атрибут,
который будет меняться со временем.
В нём будет храниться пробег машины в милях.
"""

### Назначение атрибуту значения по умолчанию ###
"""
Каждый атрибут класса должен иметь исходное значение, даже если оно равно 0
или пустой строке. В некоторых случаях это исходное значение есть смысл
задавать в теле метода __init__();
в таком случае передавать параметр для этого атрибута при создании объекта
не обязательно.

А вообще у метода __init__ есть две зоны передачи параметров:
class Car():
	def __init__(помещается то, что разное для каждого объекта):
		Здесь (ниже) помещается то, что является внутренним состоянием объекта
		и имеет фиксированное начальное значение (по умолчанию).
		self.make = make
		self.model = model
		self.year = year
		
		self.odometer_reading = 0
"""
class Car():
	def __init__(self, make, model, year):
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
	
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
print()

### Изменение значений атрибутов ###
"""
Значение атрибута можно изменить одним из трёх способов:
Изменить его прямо в экземпляре,
Задать значение при помощи метода
Или изменить его с приращением(прибавлением величины) при помощи метода.
"""

# Прямое изменение значения атрибута (используется крайне редко) #
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print()

# Изменение значения атрибута с использованием метода #
class Car():
	def __init__(self, make, model, year):
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
		""" Устанавливаем заданное значение на одометре. """
		self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(36)
my_new_car.read_odometer()

"""
Добавим некую проверку, которая гарантирует, что никто не сбросит
показатели одометра.
"""

class Car():
	def __init__(self, make, model, year):
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
		""" Устанавливаем заданное значение на одометре. """
		""" При попытке обратной подкрутки изменение отклоняется. """
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(28)
my_new_car.read_odometer()
""" Подкрутка милей в обратную сторону. """
my_new_car.update_odometer(10)
my_new_car.read_odometer()

# Изменение значения атрибута с приращением #
"""
Иногда значение атрибута требуется изменить с заданным приращением
(вместо того, чтобы присваивать атрибуту произвольное новое значение).

Допустим, мы купили поддержанное авто и проехали на ней 100 миль
с момента покупки.

Следующий метод получает величину приращения и прибавляет её
к текущим показателям:
"""
class Car():
	def __init__(self, make, model, year):
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
		""" Устанавливаем заданное значение на одометре. """
		""" При попытке обратной подкрутки изменение отклоняется. """
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self, miles):
		""" Увеличивает показания одометра с заданным приращением. """
		self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

"""
Подобные методы управляют обновлением внутренних значений экземпляров,
однако любой пользователь, имеющий доступ к программному коду,
сможет напрямую задать атрибуту любое значение.

Эффективная схема безопасности должна уделять особое внимание
таким подробностям, не ограничиваясь простейшими проверками.
"""
