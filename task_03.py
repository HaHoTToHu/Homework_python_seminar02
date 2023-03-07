# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число: "))
pow_of_two = 1
number = 2
count = 0
while pow_of_two <= n:
    pow_of_two *= number
    if pow_of_two > n:
        break
    count += 1
    print(f"2^{count} = {pow_of_two}")