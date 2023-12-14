import itertools
from itertools import permutations

cards = list(range(10))
combinations_2 = list(permutations(cards, r=2))
combinations_3 = list(permutations(cards, r=3))
filtered_combinations_2 = list()
filtered_combinations_3 = list()
counter_2 = 0
counter_3 = 0

for item in (combinations_2):
  item_digits_2 = int(f"{item[0]}{item[1]}")
  if item_digits_2 >= 10:
    filtered_combinations_2.append(item)
  if item_digits_2%18 == 0:
    counter_2 += 1

    
for item in (combinations_3):
  item_digits_3 = int(f"{item[0]}{item[1]}{item[2]}")
  if item_digits_3 >= 100:
    filtered_combinations_3.append(item)
  if item_digits_3%36 == 0:
    counter_3 += 1

print(f"Кількість комбінацій з двох цифр, що не починаються з нуля: {len(filtered_combinations_2)}")
print(f"Кількість комбінацій, що діляться на '18': {counter_2}")
print(f"Кількість комбінацій з трьох цифр, що не починаються з нуля: {len(filtered_combinations_3)}")
print(f"Кількість комбінацій, що діляться на '36': {counter_3}")
print(f"Вірогідність того, що комбінація з двох чисел ділиться на '18': {counter_2/len(filtered_combinations_2)}")
print(f"Вірогідність того, що комбінація з трьох чисел ділиться на '36': {counter_3/len(filtered_combinations_3)}")



