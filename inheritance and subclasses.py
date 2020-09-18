class Employee:
    raise_amount = 1.06
    num_of_persons = 5

    def __init__(self, first, last, status, pay):
        self.first = first
        self.last = last
        self.status = status
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_persons += 1

    def fullname(self):
        return '{}-{}-{}'.format(self.first, self.last, self.status)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, status, pay, programming_language):
        super().__init__(first, last, status, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, status, pay, employees=None):
        super().__init__(first, last, status, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp (self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp (self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Vitalii', 'Hlapshun', 'Hui', 50000, 'PHP')
dev_2 = Developer('Mii', 'General', 'Full_Stack_Developer', 40000, 'Java')

mgr_1 = Manager('Sorokin', 'Olexii', 'Pots', 120000, [dev_1])

emp_1 = Employee('Viktor', 'Boyarchuk', 'Python_Dev', 90000)

print(dev_1.email)
print(dev_2.email)

print(mgr_1.fullname())
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.remove_emp(dev_2)
mgr_1.print_emp()


print(Developer.num_of_persons)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_1.programming_language)
