#1. На вход подается список из чисел. Вывести результат произведения всех положительный чисел.

numbers = [1, 5, 4, 7, 12, 8, 9, -6]
even_ones_numbers = list(filter(lambda x: x % 2 == 0 and x > 0, numbers))
count = 1

for i in even_ones_numbers:
    count *= i
    
print(count)
