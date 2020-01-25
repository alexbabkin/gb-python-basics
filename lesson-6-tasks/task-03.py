#
# Task 3
#


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    # it is not necessary to have this method, but let's implement it
    def get_income(self):
        return self._income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        income = self.get_income()
        return income['wage'] + income['bonus']


pos = Position('Alexander', 'Babkin', 'engineer', {'wage': 100000, 'bonus': 50000})
print(f'Full name is {pos.get_fullname()}')
print(f'Total income is {pos.get_total_income()}')
