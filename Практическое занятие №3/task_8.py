# Вычисление корня из n с заданной точностью
n = int(input('Введите число: '))
m = int(input('Заданная точность: '))

print(f'{n ** (1 / 2):.{m}f}')