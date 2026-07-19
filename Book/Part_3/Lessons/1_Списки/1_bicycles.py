## Списки ##

"""
Список представляет из себя набор элементов, в определённом порядке
В списке может находиться любая информация, не связанная друг с другом
Имена для списков, лучше создавать в мн.ч: names, cars
В Python список обозначается двумя квадратными скобками [ ]
Элементы в списках разделяются запятыми
"""

# Далее простой пример списка с велосипедами
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print()

# Обращение к элементам списка, осуществляется с помощью индекса
# Обращение к первому элементу списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print()

# Также можно использовать строковые методы из главы 2
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print()

# Индексы начинаются с 0, а не с 1
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print()

# Также есть возможность обратиться к последнему элементу списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
print()

## Использование отдельных элементов списка ##
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
