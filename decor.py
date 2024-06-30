def decorator(func):
    def wraper(a,b):
        print("===============================")
        result = func(a,b)
        print(result)
        print("===============================")
        return result
    return wraper

def div_decor(func):
    def wraper(a, b):
        if b == 0:
            print("На ноль делить НЕЛЬЗЯ")
            raise ZeroDivisionError
        result = func(a,b)
        return result
    return wraper

@decorator
def func():
    print("Вызов функции")

@div_decor
@decorator
def func_div(a, b):
    return a / b

def func_div_no_decor(a, b):
    return a / b

func = decorator(div_decor(func_div_no_decor))
func(4,2)
func_div(4,2)
