x = (float(input('Введите координату х: ')))y = (float(input('Введите координату у: ')))n = int(input('Введите размер круга: '))s = x * x + y * yif s < n * n:    print(f'Точка с координатами {x, y} находится в пределах окружности с радиусом {n}')elif s == n * n:    print(f'Точка с координатами {x, y} находится на границе окружности с радиусом {n}')else:    print(f'Точка с координатами {x, y} находится за пределами окружности с радиусом {n}')