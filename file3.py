listt = []q = int(input('Введите кол-во чисел которые вы хотите ввести: '))for k in range(q):    g = int(input('Введите число: '))    listt.append(g)x = int(input('Введите число которое хотите найти: '))count = 0for i in listt:    if i == x:        print(f'Число {x} находится в списке под номером {listt.index(x) + 1}')        count += 1        breakif count == 0:    print('Число не найдено :(')