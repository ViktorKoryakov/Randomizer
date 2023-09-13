# [ IMPORTING ] 
import random

# [ TITLE ]
print(f"{'-'*30} \nНастройте рандомайзер под себя \n{'-'*30}")
print()

# [ SETTINGS ]
first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
times = int(input("Введите кол-во чисел: "))
if times > 1:
    repeating = bool(input("Повторять числа? (True - да, False - нет): "))
print()

# [ yet another TITLE ]
print(f"{'-'*6} \nОтвет: \n{'-'*6}")

# [ ANSWER ]
if times > 1:
    list = [] # DO NOT CHANGE
    for i in range(times):
        rand_num = random.randint(first_num, second_num)
        if repeating == (not False):
            while rand_num in list:
                rand_num = random.randint(first_num, second_num)
        list.append(rand_num)
    print(f"Рандомные числа... {list}")
else:
    print(f"Рандомное число... {random.randint(first_num, second_num)}")
