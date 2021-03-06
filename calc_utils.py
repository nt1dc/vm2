import data_io
import numpy as np


def find_div(function, h=0.000000001):
    return lambda x: (function(x + h) - function(x - h)) / (2 * h)


def find_interval(function, step):
    prev = -100
    for i in np.arange(-100, 100, step):
        if function(i) * function(prev) < 0:
            print("Найден интервал: [" + str(prev) + ", " + str(i) + "]")
            if data_io.ask_continue() == 2:
                return prev, i
        prev = i
    print("Интервал не найден")
    return data_io.get_interval(function)
