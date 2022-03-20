import numpy as np

functions_name = {
    0: "x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907",
    1: "x ** 2 - 3 * x - 2",
    2: "np.sin(x) - np.cos(x) + 0.2 * x"
}

system_functions_name = {
    0: "x ** 2 + y ** 2 - 4",
    1: "x ** 3 + y - 1",
    2: "x ** 2 - y - 3"
}


def create_own_function():
    while True:
        try:
            zxc = input()
            zxc = zxc.replace("sin", "np.sin")
            zxc = zxc.replace("cos", "np.cos")
            zxc = zxc.replace("tg", "np.tg")
            zxc = zxc.replace("ctg", "np.ctg")
            temp = lambda x: eval(zxc)
            temp.__call__(1)
            functions_name[len(functions_name)] = zxc
            return len(functions_name) - 1, temp
        except Exception:
            print("давай по новой, миша, все *****!\n "
                  "вот тебе пример x ** 3 + 2.28 * (x ** 2) - 1.934 * x - 3.907\n"
                  "ну или  sin(x) - cos(x) + 0.2 * x ")
