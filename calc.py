def sum(a, b):
    return a + b


def difference(a, b):
    return a - b


def product(a, b):
    return a * b


def division(a, b):
    return a / b


def power(a, b):
    return a**b


def mod(a, b):
    return a % b


def floor_division(a, b):
    return a // b


def run():
    oper = operation()
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if oper == "+":
        return sum(a, b)
    elif oper == "-":
        return difference(a, b)
    elif oper == "*":
        return product(a, b)
    elif oper == "/":
        return division(a, b)
    elif oper == "//":
        return floor_division(a, b)


def operation():
    oper = input("Выберите операцию (Введите +, -, *, / или //): ")
    return oper


print(run())
