# Частная производная по х
def calc_dx(function, x, y, h=0.00000001):
    return (function(x + h, y) - function(x - h, y)) / (2 * h)


# Частная производная по у
def calc_dy(function, x, y, h=0.00000001):
    return (function(x, y + h) - function(x, y - h)) / (2 * h)


# Поиск определителя матрицы Якоби
def calc_j(function1, function2, x, y):
    return calc_dx(function1, x, y) * calc_dy(function2, x, y) - calc_dx(function2, x, y) * calc_dy(function1, x, y)


# Поиск решений системы
def calc_system(function1, function2, start_x, start_y, accuracy):
    x_current = start_x
    y_current = start_y
    y_prev = y_current * 1000 + 10
    x_prev = x_current * 1000 + 10
    iterations = 0

    while max(abs(x_current - x_prev), abs(y_current - y_prev)) > accuracy:
        x_prev = x_current
        y_prev = y_current
        J = calc_j(function1, function2, x_prev, y_prev)
        A = function1(x_prev, y_prev) / J
        B = function2(x_prev, y_prev) / J
        x_current = x_prev - A * calc_dy(function2, x_prev, y_prev) + B * calc_dy(function1, x_prev, y_prev)
        y_current = y_prev + A * calc_dx(function2, x_prev, y_prev) - B * calc_dx(function1, x_prev, y_prev)
        iterations += 1
        if (iterations == 100):
            print("Расходится")
            exit()
    return x_current, y_current, abs(x_current - x_prev), abs(y_current - y_prev), iterations
