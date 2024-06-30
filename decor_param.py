"""
Часто на собеседованиях просят создать какой-то простой декоратор. 
Вы описали эту простую конструкцию с функцией и вложенной функцией. 
И далее вас спрашивают, а как реализовать параметризованный декоратор?
Т.е. тот, который может принимать на вход какие-то парамерты.
"""

def make_decorator(start_counter):
    def decorator(func):
        series = []
        count = start_counter

        def wrapper(*args, **kwargs):
            nonlocal count
            result = func(*args, **kwargs)
            series.append(result)
            print(f"Это {count} запуск функции {func.__name__}")
            print("series = {}".format(series))
            count += 1
            #return result
        return wrapper
    return decorator

@make_decorator(10)
def func1(a, b):
    c = a + b
    return c

func1(1, 1)
func1(2, b=1)
func1(a=2, b=2)