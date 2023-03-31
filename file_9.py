number = int(input('Введите число: '))
base = 2
numberj = ''

while number > 0:
    numberj += str(number % base)
    number = number // base

numberj = numberj[::-1]


print(numberj)
