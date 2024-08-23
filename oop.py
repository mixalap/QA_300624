class Student:
    # Атрибут класса:
    default_course = 'Python Developer'

    # Инициализатор класса:
    def __init__(self, name, surname, age):
        # Атрибуты экземпляра класса:
        self.name = name
        self.surname = surname
        self._age = age
        self.__passport = '123123'
        self.course = Student.default_course + '!!!'

    # Метод экземпляра:
    def get_full_name(self):
        return f'{self.name} {self.surname}' 

    def multipassort(self):
        return self.__passport

    # Метод класса:
    @classmethod
    def get_default_course(cls):
        return cls.default_course

    # Статический метод:
    @staticmethod
    def get_greeting():
        return 'Привет, студент курса ' + Student.default_course

    @property
    def is_lucky(self):
        return len(self.name + self.surname) == self._age


class Student2():
    # Атрибут класса:
    default_course = 'Python Developer2'


class Student3(Student, Student2):
    pass
