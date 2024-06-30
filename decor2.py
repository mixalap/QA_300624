"""Декторатор нужно писать так, чтобы он был как можно более универсальный. 
Чтоб в него можно было оборачивать как можно больше всяких функций.
"""
def decorator(func):
    def wraper(a, b): #что если аргументов больше
        print("Операции внутри декоратора:")
        result = func(a,b)
        print("Завершение работы декоратора")
        return result
    return wraper 

# *args, **kwargs 
def decorator(func):
    def wraper(*args, **kwargs):
        print("Операции внутри декоратора:")
        print("*args", args)
        print("**kwargs", kwargs)
        result = func(*args, **kwargs)
        print("Завершение работы декоратора")
        return result
    return wraper   

@decorator
def func(a, b, c, d):
    print("Операция внутри func:")
    return a + b + c + d

print(f'Результат: {func(1, 1, 1, 1)}')
print("---------------------")
print(f'Результат: {func(2, b=1, c=1, d=1)}')
print("---------------------")
print(f'Результат: {func(a =1, b=1, c=1, d=1)}')
print("---------------------")