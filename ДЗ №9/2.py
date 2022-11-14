# 2. На вход подаются числа a и k, где а - число в десятичном представлении, а k - cтепень двойки, на которое нужно разделить а Выведите результат такого деления, используя битовые операции.

number = int(input())
degree_of_two = int(input())

for i in range(degree_of_two):
    number = number >> 1

print(number)
