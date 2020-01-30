#
# Task 2.
#


class MyZeroDivisionError(BaseException):
    pass


def div(arg1, arg2):
    if float(arg2) == 0.0:
        raise MyZeroDivisionError("Error: division by zero")
    return arg1 / arg2


try:
    res = div(10, 5)
    print(res)
    res = div(1, 0)
except MyZeroDivisionError as e:
    print(e)
