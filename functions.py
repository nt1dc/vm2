functions_name = {
    0: "x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907",
    1: "x ** 2 - 3 * x - 2",
    2: "np.sin(x) - np.cos(x) + 0.2 * x"
}


def get_function(num):
    return lambda x: eval(functions_name[num])


def get_system_function(num):
    if num == 1:
        return lambda x, y: x ** 2 + y ** 2 - 4
    if num == 2:
        return lambda x, y: x ** 3 + y - 1
    if num == 3:
        return lambda x, y: x ** 2 - y - 3


def get_system_function_name(num):
    if num == 1:
        return "x^2 + y^2 - 4"
    if num == 2:
        return "x^3 + y - 1"
    if num == 3:
        return "x^2 - y - 3"


def create_own_function():
    while True:
        try:
            zxc = input()
            temp = lambda x: eval(zxc)
            temp.__call__(1)
            functions_name[len(functions_name)] = zxc
            return len(functions_name) - 1, temp
        except Exception:
            print("давай по новой, миша, все *****!\n "
                  "вот тебе пример x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907 ")
