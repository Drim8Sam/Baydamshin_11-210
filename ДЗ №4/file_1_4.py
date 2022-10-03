import random

t = []
f = []
nm = []
number = input('Введите число(Для отмены введите q): ')
while number != 'q':
    Percentage = len(t) + len(f) + 2
    tr = len(t) + 1
    fa = len(f) + 1
    number = int(number)
    knumber = random.randint(0, 9)
    nm.append(knumber)
    if number == knumber:
        print('Вы угадали число!')
        t.append(number)
        print(f'Стастика угаданных чисел: {int((tr / Percentage) * 100)} % / 100 %')
        print(f'Стастика не угаданных чисел: {int((fa / Percentage) * 100)} % / 100 %')
        print(f'Ранее загаданные числа: {nm}')
    else:
        print(f'Вы не угадали число. Загаданное число - {knumber}')
        f.append(number)
        print(f'Ранее загаданные числа: {nm}')

    number = input('Давайте сыграем ещё раз? Введите число(Для отмены введите q): ')
