"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

class Matrix:
    def __init__(self, arg_1, arg_2, arg_3):
        self.arg_1 = list(arg_1)
        self.arg_2 = list(arg_2)
        self.arg_3 = list(arg_3)
    def __str__(self):
        return (
            f"{obj_1.arg_1} \n"
            f"{obj_1.arg_2} \n"
            f"{obj_1.arg_3} \n")

    def __add__(self, other):
        return Matrix()


obj_1 = Matrix((1,2,3),(4,5,6),(7,8,9))
obj_2 = Matrix((1,2,3),(4,5,6),(7,8,9))
print(obj_1)
print(obj_2)

print(obj_1 + obj_2)
