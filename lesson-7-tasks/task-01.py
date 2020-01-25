#
# Task 1.
#


class Matrix:
    def __init__(self, lst):
        input_is_correct = True
        dem = len(lst[0])
        for row in lst:
            if len(row) != dem:
                print('Incorrect input')
                input_is_correct = False
                break
        if input_is_correct:
            self._table = lst
        else:
            self._table = [[]]

    def get_dimension(self):
        if len(self._table) == 0:
            return 0, 0
        return len(self._table), len(self._table[0])

    def __str__(self):
        res = ''
        for row in self._table:
            for e in row:
                res += f'{e} '
            res += '\n'
        return res

    def __add__(self, other):
        if self.get_dimension() != other.get_dimension():
            raise Exception('dimensions do not match')
        if self.get_dimension() == (0, 0):
            return Matrix([[]])
        res = []
        for self_row, other_row in zip(self._table, other._table):
            res_row = list(map(lambda e1, e2: e1 + e2, self_row, other_row))
            res.append(res_row)
        return Matrix(res)


m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2]])
print(m1)

m1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(m1)

print(f'{Matrix([[1, 1], [1, 1]]) + Matrix([[2, 2], [2, 2]])}')
