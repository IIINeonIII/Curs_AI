class Citizen(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_details(self):
        print(f'{self.first_name} {self.last_name}')


class Teacher(Citizen):  # subclasa mosteneste superclasa
    def __init__(self, first_name, last_name, subject):
        super().__init__(first_name, last_name)
        self.subject = subject

    def print_details(self): #metoda reimplementata
        super().print_details()
        print(self.subject)


class Student(Citizen):
    def __init__(self, first_name, last_name, group):
        super().__init__(first_name, last_name)
        self.group = group




teacher = Teacher('ion', 'popescu', 'python')
teacher.print_details()