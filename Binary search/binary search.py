import random


def binary_search_recursive(array, s_number, left, right):

    if left > right:
        return 'No number was found'

    mid = (left + right) // 2
    if s_number == array[mid]:
        return mid

    if s_number < array[mid]:
        return binary_search_recursive(array, s_number, left, mid - 1)
    else:
        return binary_search_recursive(array, s_number, mid + 1, right)


s_number = int(input('Введите число: '))
array = []

for i in range(15):
    array.append(random.randint(1, 40))

array.sort()

print("Searching for {}".format(s_number))
print(array)
print("Index of {}: {}".format(s_number, binary_search_recursive(array, s_number, 0, len(array))))
