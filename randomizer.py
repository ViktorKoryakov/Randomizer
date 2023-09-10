# [ IMPORTING ] 
import random

# [ TITLE ]
print("-"*30)
print("Настройте рандомайзер под себя")
print("-"*30)
print()

# [ DEFINE SETTINGS ]
first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))
times = int(input("Введите кол-во чисел: "))
if times > 1:
    repeating = bool(input("Не повторять числа? (True - да, False - нет): "))
print()

# [ yet another TITLE ]
print("-"*6)
print("Ответ:")
print("-"*6)
print()

# [ ANSWER ]
if times > 1:
    list = [] # DO NOT CHANGE
    for i in range(times):
        rand_num = random.randint(first_num, second_num)
        if repeating == True:
            while rand_num in list:
                rand_num = random.randint(first_num, second_num)
        list.append(rand_num)
    print(f"Рандомные числа... {list}")
else:
    print(f"Рандомное число... {random.randint(first_num, second_num)}")
    
