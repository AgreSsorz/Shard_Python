"""
Привелегии:
Написать класс Priveleges.
Класс должен содержать всего один атрибут priveleges со списком строк
из упражнения 3_admin.py
Переместить метод show_priveleges() в этот класс.
Создать экземпляр Priveleges как атрибут класса Admin.
Создать новый экземпляр Admin и использовать свой метод
для вывода списка привелегий.
"""
class User():
	""" Создаём модель пользователя с помощью метода __init__. """
	def __init__(self, first_name, last_name):
		""" Инициализируем атрибуты пользователя после self. """
		self.fname = first_name
		self.lname = last_name
		
		""" Попытки входа по умолчанию. """
		self.login_attempts = 0
	
	""" Создаём метод для вывода информации о пользователе. """
	def describe_user(self):
		print(f"Имя: {self.fname.title()} \nФамилия: {self.lname.title()}")

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

class Priveleges():
    def __init__(self, priveleges=None):
        if priveleges is None:
            self.priveleges = [
        '\nразрешено добавлять сообщения',
        '\nразрешено удалять пользователей',
        '\nразрешено банить пользователей',
        '\nразрешено вносить правки',
        ]
        
        else:
            self.priveleges = priveleges
        
    """ Создаём метод вывода привелегий. """
    def show_priveleges(self):
        """ Создаём пустую строку, объединяющую все привелегии из списка. """
        result = ''
        for privelege in self.priveleges:
            result = result + privelege + "; "
        print(f"Привелегии администратора: " + result)

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priveleges = Priveleges()

Yan = Admin('ян', 'смирнов')
Yan.greet_user()
Yan.describe_user()
Yan.priveleges.show_priveleges()
