# Задача №39.

# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива.

# Пример:

# Ввод:                           Вывод:
#      7                                3 3 2 12

#      3 1 3 4 2 4 12

#      6

#      4 15 43 1 15 1                   (каждое число вводится с новой строки)


def cross_array(arr1, arr2):
    second_set = set(arr2)
    new_array = []
    for i in arr1:
        if i not in second_set:
            new_array.append(i)
    return new_array


len_first_array = int(input('Введите длину первого массива: '))
first_array = []

for i in range(len_first_array):
    first_array.append(input(f'Введите {i + 1}-й элемент первого массива: '))

len_second_array = int(input('Введите длину второго массива: '))
second_array = []

for i in range(len_second_array):
    second_array.append(input(f'Введите {i + 1}-й элемент второго массива: '))

print(cross_array(first_array, second_array))