import numpy as np
import bisection_method
import calc_utils
import data_io
import functions
import iterrations_method
import newton_method


def find_solution():
    print("а хочешь сам добавить функцию ?_?\n"
          "если да то введи 1")
    if int(input()) == 1:
        print("введи функцию")
        fn_num, function = functions.create_own_function()
    else:
        fn_num = data_io.get_function_num()
        function = lambda x: eval(functions.functions_name[fn_num])
    data_io.plot_function(function, -9, 9, -9, 9, 1)
    interval_type = data_io.get_interval_input_type()

    if interval_type == 1:
        a, b = data_io.get_interval(function)
    else:
        a, b = calc_utils.find_interval(function, 0.5)

    print("a = " + str(a) + ", " + "b = " + str(b))

    accuracy = data_io.ask_accuracy()

    if data_io.ask_methods() == 1:
        ans, iterations = bisection_method.calc(function, a, b, accuracy)
    else:
        ans, iterations = iterrations_method.calc(function, a, b, accuracy)

    print("Корень: " + str(ans) + " найден за " + str(iterations) + " итераций, f(x) = " + str(function(ans)))

    data_io.plot_function(function, a - 0.5, b + 0.5, function(a) - 0.5, function(b) + 0.5, 0.2)


def find_system():
    num1, num2 = data_io.get_system_function_num()
    function1 = lambda x, y: eval(functions.system_functions_name[num1])
    function2 = lambda x, y: eval(functions.system_functions_name[num2])

    data_io.plot_system(function1, function2)
    start_x, start_y = data_io.get_start()
    error = data_io.ask_accuracy()
    x, y, err_x, err_y, it = newton_method.calc_system(function1,
                                                       function2, start_x, start_y,
                                                       error)
    print("x = " + str(x) + ", y = " + str(y) + ", найден за " + str(it) + " итераций, вектор погрешностей: [" + str(
        err_x) + ", " + str(err_y) + "]")


if __name__ == "__main__":
    if data_io.ask_task() == 1:
        find_solution()
    else:
        find_system()
