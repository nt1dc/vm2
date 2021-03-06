import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

import functions


# Отрисовка графика
def plot_function(func, min_x, max_x, min_y, max_y, step):
    x = np.linspace(min_x, max_x, 10000)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    try:
        ax.plot(x, func.__call__(x), "g", linewidth=2.0)
    except Exception:
        print("ну ты ввел плохо функцию =/ ")
        exit(-1)
    ax.set(xlim=(min_x, max_x), xticks=np.arange(min_x, max_x, step),
           ylim=(min_y, max_y), yticks=np.arange(min_y, max_y, step))

    plt.show()


def get_function_num():
    while True:
        for i in range(len(functions.functions_name)):
            print(str(i) + " - " + functions.functions_name[i])
        try:
            function = int(input("Введи номер функции: "))
            if function in functions.functions_name:
                return function
        except ValueError:
            print("введи нормально")


def get_interval_input_type():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Введи 1, чтобы ввести интервал, 2, чтобы запустить поиск интервала: "))
        except ValueError:
            print("Введите 1 или 2")
    return type


def get_interval(function):
    while True:
        try:
            a, b = map(float, input("Введи границы интервала через пробел: ").split())
            if a > b:
                a, b = b, a
            elif a == b:
                raise ArithmeticError
            elif function(a) * function(b) >= 0:
                raise AttributeError
            break
        except ValueError:
            print("Границы интервала должны быть числами, введёнными через пробел.")
        except ArithmeticError:
            print("Границы интервала не могут быть равны.")
        except AttributeError:
            print("Интервал содержит ноль или обе точки одного знака.")
    return a, b


def ask_continue():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Введите 1, чтобы найти следующий интервал, 2, чтобы выбрать этот интервал: "))
        except ValueError:
            print("Введите 1 или 2")
    return type


def ask_methods():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(
                input("Введите 1, чтобы выбрать метод половинного деления, 2 чтобы выбрать метод простой итерации: "))
        except ValueError:
            print("Введите 1 или 2")
    return type


def ask_accuracy():
    while True:
        try:
            number = float(input("Введите точность: "))
            if (number > 0):
                return number
            print("Число должно быть положительным")
        except ValueError:
            print("Введите число")


def ask_task():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Введите 1, чтобы выбрать одно уравнение, 2, чтобы выбрать систему уравнений: "))
        except ValueError:
            print("Введите 1 или 2")
    return type


# ------Системы----

# Построение графика системы
def plot_system(function1, function2):
    x, y = sp.symbols("x y")
    sp.plot_implicit(sp.Or(sp.Eq(function1(x, y), 0), sp.Eq(
        function2(x, y), 0)))


# Выбор функций для системы
def get_system_function_num():
    while True:
        for i in range(len(functions.system_functions_name)):
            print(str(i) + " - " + functions.system_functions_name[i])
        try:
            function1 = int(input("Введите номер первой функции: "))
            function2 = int(input("Введите второй первой функции: "))
            if function1 in functions.system_functions_name and function2 in functions.system_functions_name and function1 != function2:
                return function1, function2
            print("Числа должны быть разными и из представленных")

        except ValueError:
            print("Должен быть числом")


# Получение начального приближения
def get_start():
    while True:
        try:
            a, b = map(float, input("Введите начальное приближение через пробел: ").split())
            break
        except ValueError:
            print("Начальное приближение должно быть числами, введенными через пробел.")
    return a, b
