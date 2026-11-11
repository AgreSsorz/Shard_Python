"""
Кубики:
Создать класс Die с одним атрибутом sides, который имеет значение 6.
Написать метод roll_die() для вывода случайного числа на кубике.
Создать экземпляр шестигранного кубика и смоделировать 10 бросков.
"""
from random import randint
class Die():
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        result = randint(1, self.sides)
        print(result)

""" Создаём десятигранный кубик и бросаем его пять раз. """    
ten_sided = Die(10)
print("Ты бросаешь десятигранный кубик пять раз: ")
for throw in range(5):
    ten_sided.roll_die()
print()
