# Задача №1. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

coin_number = int(input ("Введите число монет: "))
zero, one = 0, 0
while zero + one < coin_number :
    n = int(input("Произвольный набор 0/1 ->"))
    if n == 0 : 
        zero += 1 
    else : 
        one += 1
print(f"Переверните {zero} монет/ы"if zero < one else f"Переверните {one} монет/ы")