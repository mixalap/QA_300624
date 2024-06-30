# Python файл первый
import file_two

def func_one():
   print("Функция 1 выполнена")

def func_two():
   print("Функция 2 выполнена")

# print(f"Файл 1 __name__ значение: {__name__}")

if __name__ == "__main__":
   print("Файл 1 выполнен запуском напрямую.")
   file_two.func_three()
