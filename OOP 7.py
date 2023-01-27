#Method resolution order = when python searches for methods or class
class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) #super() will pass the first last and pay arguments to developer class it calls the parent init method
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Aaima', 'Faisal', 50000, 'Python')
dev_2 = Developer('Sufyan', 'Asif', 20000, 'Java')

mgr_1 = Manager('Sue', 'Evans', 90000, [dev_1])

print(isinstance(mgr_1, Manager)) #asks for example here if manager 1 is an instance of manager
print(isinstance(mgr_1, Developer)) #gives false because manager and developer arent part of each other's inheritance
print(issubclass(Manager, Employee)) #asks if developer/Manager a subclass of employee