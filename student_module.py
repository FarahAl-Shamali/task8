from subject_module import Subject


class Student:
    s = Subject("anything", 0)

    def __init__(self, name, age, city):
        self.stuName = name
        self.age = age
        self.city = city

    def add_mark(self, mark):
        pass

    def get_all_marks(self):
        pass

    def Calc_average(self):
        pass
