# Создать список гостей на обед, неважно, живые или умершие. Минимум 3
guests = ['denis', 'oleg', 'caroline', 'yura', 'tolya', 'nina']

# Пригласить каждого на обед
print(f"I invite you {guests[0].title()} to lunch with me!")
print(f"I invite you {guests[1].title()} to lunch with me!")
print(f"I invite you {guests[2].title()} to lunch with me!")
print(f"I invite you {guests[3].title()} to lunch with me!")
print(f"I invite you {guests[4].title()} to lunch with me!")
print(f"I invite you {guests[5].title()} to lunch with me!")
print()

# Изменить список гостей
guests = ['denis', 'oleg', 'caroline', 'yura', 'tolya', 'nina']
print(f"{guests[2].title()} won't be able to come.")
guests[2] = 'roma'

print(f"I invite you {guests[0].title()} to lunch with me!")
print(f"I invite you {guests[1].title()} to lunch with me!")
print(f"I invite you {guests[2].title()} to lunch with me!")
print(f"I invite you {guests[3].title()} to lunch with me!")
print(f"I invite you {guests[4].title()} to lunch with me!")
print(f"I invite you {guests[5].title()} to lunch with me!")
print()

# Нужно добавить ещё три гостя
print("More guests are expected...")
guests.insert(0, 'mother')
guests.insert(4, 'father')
guests.append('sasha')
print(f"I invite you {guests[0].title()} to lunch with me!")
print(f"I invite you {guests[1].title()} to lunch with me!")
print(f"I invite you {guests[2].title()} to lunch with me!")
print(f"I invite you {guests[3].title()} to lunch with me!")
print(f"I invite you {guests[4].title()} to lunch with me!")
print(f"I invite you {guests[5].title()} to lunch with me!")
print(f"I invite you {guests[6].title()} to lunch with me!")
print(f"I invite you {guests[7].title()} to lunch with me!")
print(f"I invite you {guests[8].title()} to lunch with me!")
print()

# Нужно отказать всем гостям, кроме двух человек
print("Two guests are invited to lunch.")
guest_popping = guests.pop(1)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(2)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(1)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(2)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(-1)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(-2)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)

guest_popping = guests.pop(-1)
print(f"I'm so sorry, {guest_popping.title()}.")
# print(guests)
print()

# Вывести сообщение для двух оставшихся людей, что они приглашены
print(f"I invite you {guests[0].title()} to lunch with me!")
print(f"I invite you {guests[1].title()} to lunch with me!")
print()

# Удалить двух гостей из списка, чтобы тот стал пустым
del guests[0]
del guests[0]
print(guests, "No one...")
