def calc(function, a, b, accuracy):
    x_current = (a + b) / 2
    a_current = a
    b_current = b
    iterations = 0
    while (abs(a - b) > accuracy) and (abs(function.__call__(x_current)) > accuracy) and function.__call__ != 0:
        x_current = (a_current + b_current) / 2
        if function.__call__(a_current) * function.__call__(x_current) > 0:
            a_current = x_current
        else:
            b_current = x_current
        iterations = iterations + 1
    x_current = (a_current + b_current) / 2
    return x_current, iterations
