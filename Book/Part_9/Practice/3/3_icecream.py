"""
Киоск с мороженым:
Написать класс IceCreamStand, наследующий от класса Restaurant из прошлого
упражнения. Добавить атрибут flavors для хранения списка сортов мороженого.
Написать метод, который выводит этот список.
Создать экземпляр IceCreamStand и вызвать этот метод. 
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
        'choco ice',
        'blue ice',
        'slime ice',
        ]
        
    
    def show_flavors(self):
        for flavor in self.flavors:
            print(f"Follow flavors are available: {flavor.capitalize()}.")
        
Penguins_33 = IceCreamStand('33 Пингвина', 'мороженое')
Penguins_33.describe_restaurant()
Penguins_33.show_flavors()
