import random
import math
a = []
b = []
c = []
for i in range(3):
    a.append(random.randint(-1, 9))
    b.append(random.randint(-1, 9))
    c.append(random.randint(-1, 9))


field = [a, b, c]
print(field)
field_copy = field.copy()

key = ''
harvest = 0
BAGS = 2
bg = 0
for i in range(9):

    try:
        key = list(map(lambda x: int(x) - 1, input().split()))
    except BaseException:
        print('Некорректные входые данные, выход из программы....')
        break

    if field[key[0]][key[1]] >= 0:
        harvest += field[key[0]][key[1]]
        field[key[0]][key[1]] = 0
    else:
        break


for row in field_copy:
    print(*row)
if harvest / 10 >= BAGS:
    print(f'Урожай удался! Собрано {harvest} картофелин в {math.ceil(harvest / 10)} мешках ')
else:
    print('Урожай неудачный')