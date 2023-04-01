# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.

# 	Ввод: 1 2 3 2 3			Вывод: 2


# Решение мое: (не работает в некоторых случаях)

# def simple_solution(array: list):
# 	new_set = set(array)
# 	if len(array) - len(new_set) == 1:
# 		print('В списке всего одна пара ')
# 	if len(array) - len(new_set) == 2:
# 		print('В списке всего две пары ')
# 	if (len(array) - len(new_set)) % 2 == 1 and len(array) - len(new_set) != 1:
# 		print((len(array) - len(new_set)) // 2 + 1)
# 	if (len(array) - len(new_set)) % 2 == 0 and len(array) - len(new_set) != 2:
# 		print((len(array) - len(new_set)) // 2)

# len_array = int(input('Введите длину списка: '))
# array = []
# for i in range(len_array):
# 	array.append(input(f'Введите {i + 1}-й элемент массива '))

# print(simple_solution(array))


# Решение на семинаре

import random

def count_couple(input_arr: list):
	find_couple = 0
	number_dict = {}           # Создаем словарь
	for i in input_arr:		   # Кладем все числа из списка в словарь и присваем каждому чилу ключ "1", а если число встречается еще раз, увеличиваем значение ключа на +1
		if i in number_dict:
			number_dict[i] = number_dict[i] + 1	
		else:
			number_dict[i] = 1
	for i in number_dict.values():
		find_couple = (find_couple) + i // 2

	return find_couple



array = [random.randint(1, 10) for _ in range(15)]
print(array)

print(count_couple(array))