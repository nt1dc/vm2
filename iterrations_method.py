import calc_utils

# Метод простой итерации
def calc(function, a, b, error):
    dev_a = calc_utils.find_div(function)(a)
    dev_b = calc_utils.find_div(function)(b)

    print("Производная в точке A: " + str(dev_a))
    print("Производная в точке B: " + str(dev_b))

    lyambd_a = -(1 / dev_a)
    lyambd_b = - (1 / dev_b)

    print("Лямбда А = " + str(lyambd_a))
    print("Лямбда B = " + str(lyambd_b))

    if (dev_a > dev_b):
        lyambd = lyambd_a
    else:
        lyambd = lyambd_b

    fi = lambda x: x + lyambd * function(x)

    fi_s = calc_utils.find_div(fi)

    fi_s_a = fi_s(a)
    fi_s_b = fi_s(b)

    print("Производная фи в А: " + str(fi_s_a))
    print("Производная фи в B: " + str(fi_s_b))

    if (abs(fi_s(a)) > 1 or abs(fi_s(b)) > 1):
        print("Не удовлетворяет достаточному условию сходимости")
    else:
        print("Удовлетворяет достаточному условию сходимости")

    x_current = a
    x_prev = a * 1000 + 10

    iterations = 0

    # Поиск корней

    while (abs(x_prev - x_current) > error) or (abs(function(x_current)) > error):
        # (abs(x_prev - x_current) > error) and abs(function(x_current)) > error) and

        x_prev = x_current
        x_current = x_prev + lyambd * function(x_prev)
        print(x_current, x_prev, function(x_current))
        iterations += 1
        if (iterations > 1000):
            print("Алгоритм расходится")
            exit()

    return x_current, iterations
