import random


list_of_people = ['Мансур', 'Роман', 'Амир', 'Ренат', 'Антон', 'Максим', 'Даниил', 'Андрей', 'Диана', 'Настя', 'Даша', 'Кристина', 'Сабина', 'Марина', 'Егор', 'Анвар', 'Арина', 'Катя', 'Миша', 'Ирина']
first_group = []
second_group = []
third_group = []
using_name = []


for i in range(20):
    first_group.append(random.choice(list_of_people))
    second_group.append(random.choice(list_of_people))
    third_group.append(random.choice(list_of_people))


print('1 группа:')
first_count = 1
for i in sorted(first_group):
    print(first_count, '-', i)
    first_count += 1

print(' ')
print('2 группа:')
second_count = 1
for i in sorted(second_group):
    print(second_count, '-', i)
    second_count += 1

print(' ')
print('3 группа:')
third_count = 1
for i in sorted(third_group):
    print(third_count, '-', i)
    third_count += 1


for name in first_group:
    if name in first_group and name in second_group and name in third_group and name not in using_name:
        print(f'Имя {name} встречается в каждой группе, а именно: ')
        print(f'В 1 группе: {first_group.count(name)} раз(а).')
        print(f'Во 2 группе: {second_group.count(name)} раз(а).')
        print(f'В 3 группе: {third_group.count(name)} раз(а)')
        print(f'Итого: {second_group.count(name) + first_group.count(name) + third_group.count(name)} раз(а)')
        print(' ')
        using_name.append(name)

    elif name not in first_group and name not in second_group and name not in third_group:
        print(f'Имя {name} не встречается ни в одной группе')

for name in second_group:
    if name in first_group and name in second_group and name in third_group and name not in using_name:
        print(f'Имя {name} встречается в каждой группе, а именно: ')
        print(f'В 1 группе: {first_group.count(name)} раз(а).')
        print(f'Во 2 группе: {second_group.count(name)} раз(а).')
        print(f'В 3 группе: {third_group.count(name)} раз(а)')
        print(f'Итого: {second_group.count(name) + first_group.count(name) + third_group.count(name)} раз(а)')
        using_name.append(name)

    elif name not in first_group and name not in second_group and name not in third_group:
        print(f'Имя {name} не встречается ни в одной группе')

for name in third_group:
    if name in first_group and name in second_group and name in third_group and name not in using_name:
        print(f'Имя {name} встречается в каждой группе, а именно: ')
        print(f'В 1 группе: {first_group.count(name)} раз(а).')
        print(f'Во 2 группе: {second_group.count(name)} раз(а).')
        print(f'В 3 группе: {third_group.count(name)} раз(а)')
        print(f'Итого: {second_group.count(name) + first_group.count(name) + third_group.count(name)} раз(а)')
        using_name.append(name)

    elif name not in first_group and name not in second_group and name not in third_group:
        print(f'Имя {name} не встречается ни в одной группе')
        
