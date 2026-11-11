"""
Администратор:
Написать класс Admin, наследующий от класса User.
Добавить атрибут privileges для хранения списка строк вида:
 "разрешено добавлять сообщения"
 "разрешено удалять пользователей"
 "разрешено банить пользователей"
 Написать метод show_privileges() для вывода набора привелегий админа.
 Создать экземпляр Admin и вызвать свой метод.
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

class Admin(User):
    def __init__(self, first_name, last_name, birthday, location):
        super().__init__(first_name, last_name, birthday, location)
        """ Добавляем атрибут со списком привелегий. """
        self.priveleges = [
        '\nразрешено добавлять сообщения',
        '\nразрешено удалять пользователей',
        '\nразрешено банить пользователей',
        '\nразрешено вносить правки',
        ]
    
    """ Создаём метод вывода привелегий. """
    def show_priveleges(self):
        """ Создаём пустую строку, объединяющую все привелегии из списка. """
        result = ''
        for privelege in self.priveleges:
            result = result + privelege
        print(f"У вас есть следующие привелегии: {result.title()}")
            
Yan = Admin('ян', 'смирнов', '14 марта 1964 года', 'томск')
Yan.greet_user()
Yan.describe_user()
Yan.show_priveleges()
