import class_introducing

class Employee:
    raise_amount = 1.06
    num_of_persons = 5
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_persons += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employees.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

# emp_1 = 'Joe-Doe-45600'
emp_2 = 'Marselus-Martin-50500'
emp_3 = 'Stimac-Mark-60000'

print(class_introducing.emp_1.__dict__)
Employee.set_raise_amount(1.09)

print(Employee.raise_amount)
print(Employee.num_of_persons)
