# универсальное решение для подсчёта суммы всех чисел и длин всех строк:
# Что должно быть подсчитано:
# - Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# - Все строки (не важно, являются они ключами или значениям или ещё чем-то)
# - Весь подсчёт должен выполняться одним вызовом функции.
# - Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
# - Т.к. каждая структура м. содержать в себе ещё несколько элементов, м. использовать параметр *args
# - Для определения типа данного используйте функцию isinstance.


# построчный подсчёт:
# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

# a = [1, 2, 3]
# print(sum(a))
# b = {'a': 4, 'b': 5}
# print(len('a') + 4 + len('b') + 5)
# c = (6, {'cube': 7, 'drum': 8})
# print(6+len('cube') + 7 + len('drum') + 8)
# d = "Hello"
# print(len(d))
# e = ((), [{(2, 'Urban', ('Urban2', 35))}])
# print(2 + len('Urban') + len('Urban2') + 35)
# f = 6 + 11 + 29 + 5 + 48
# print(f)

# функциональное программирование

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    sum_ = 0
    if isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_ += calculate_structure_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        sum_ += data_structure
    elif isinstance(data_structure, str):
        sum_ += len(data_structure)
    return sum_


result = calculate_structure_sum(data_structure)
print(result)
