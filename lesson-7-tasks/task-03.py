#
# Task 3.
#


class Cell:
    def __init__(self, cells_num):
        self._cells_num = cells_num

    def __add__(self, other):
        return Cell(self._cells_num + other._cells_num)

    def __sub__(self, other):
        if self._cells_num > other._cells_num:
            return Cell(self._cells_num - other._cells_num)
        raise Exception(f'Operation can not be performed')

    def __mul__(self, other):
        return Cell(self._cells_num * other._cells_num)

    def __truediv__(self, other):
        return Cell(self._cells_num // other._cells_num)

    def __str__(self):
        return f'Cell with {self._cells_num} cells'

    def make_order(self, cells_in_row):
        number_of_full_rows = self._cells_num // cells_in_row
        additional_row = self._cells_num % cells_in_row
        res = ''
        for i in range(1, number_of_full_rows + 1):
            if i > 1:
                res += '\\n'
            res += cells_in_row * '*'
        if additional_row > 0:
            res += '\\n' + additional_row * '*'
        else:
            res += additional_row * '*'
        return res


print(Cell(12).make_order(5))
print(Cell(15).make_order(5))

c1 = Cell(4)
c2 = Cell(3)

print(f'{c1 + c2}, {c1 - c2}, {c1 * c2}, {c1 / c2}')
