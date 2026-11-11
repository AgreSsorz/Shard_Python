"""
Импортирование класса Restaurant:
Взять последнюю версию класса Restaurant и сохранить её в модуле.
Создать экземпляр Restaurant и вызвать один из его методов.
"""
from rest_m import Restaurant

my_restaurant = Restaurant('Ресторан Хачу Пури', 'открыт')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()

"""
Импортирование класса Admin:
Сохранить классы User, Priveleges, Admin в одном модуле.
Создать экземпляр Admin и вызвать метод show_priveleges().
"""
from u_admin import User, Priveleges, Admin

admin = Admin('yuri', 'kravcov')
admin.greet_user()
admin.priveleges.show_priveleges()
print()
