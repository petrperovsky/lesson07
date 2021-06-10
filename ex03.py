'''Вопреки формулировке задачи, я понял, что определяем не количество клеток, а количество ячеек клеток'''
class Cell():
    def __init__(self, number: int):
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        print(f'Невозможно уменьшить')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        if self.number > other.number:
            return Cell(self.number // other.number)
        print('Так делить нельзя')

    def make_order(self, cell_in_row):
        rows, tail = self.number // cell_in_row, self.number % cell_in_row
        return '\n'.join((['*' * cell_in_row] * rows) + (['*' * tail]if tail > 0 else []))
    def __str__(self):
        return (f'Клетка состоит из {self.number} компартментов')

c1 = Cell(11)
c2 = Cell(25)
print(c1 + c2)
print(c1 - c2)
print(c1 - c1)
print(c1 * c2)
print(c1 / c2)
print(c2 / c1)
print((c1 + c2).make_order(6))