# Сегменты: добавь в конец одной из программ, написанных ранее, 
# фрагмент, который делает следующее:
# Выводит сообщение "The first three items in the list are:", а затем 
# использует сегмент для вывода первых трёх элементов из списка.
pizzaz = ['pepperoni', 'manhathan', 'four_cheese', 'pineapple heaven', 
'salsa', 'vegetable pizza', 'chili']
print(pizzaz)
print(f"The first three items in the list are: {pizzaz[:3]}")
print()

# Выводит сообщение "Three items from the middle of the list are:", а 
# затем использует сегмент для вывода первых трёх элементов из середины 
# списка.
print(f"Three items from the middle of the list are: {pizzaz[2:5]}")
print()

# Выводит сообщение "The last three items in the list are:", а затем 
# использует сегмент для вывода последних трёх элементов списка.
print(f"The last three items in the list are: {pizzaz[-3:]}")
print()

# Моя пицца, твоя пицца: создать копию списка с видами пиццы, присвоив 
# название friend_pizzaz. Затем сделать следующее:
# Добавить новую пиццу в исходник.
friend_pizzaz = pizzaz[:]
pizzaz.append('green pizza')
print()

# Добавить ещё одну пиццу в копию списка.
friend_pizzaz.append('burrito')

# Доказать, что существует два разных списка с помощью цикла for.
print("My favorite pizzaz are:")
for item in pizzaz:
	print(item.title())
print()

print("My friend's favorite pizzaz are:")
for item in friend_pizzaz:
	print(item.title())
print()
