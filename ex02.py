class Clothes():
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def tissue_required(self):
        pass

    @property
    def tissue_required_full(self):
        return str(f'Необходимо на пошив одежды всего: '
                   f'{round((self.size / 6.5 + 0.5) + (self.height * 2 / 0.3), 2)}')


class Coat(Clothes):
    def tissue_required(self):
        return str(f'Для пошива пальто необходимо: {round((self.size / 6.5 + 0.5), 2)}')


class Jacket(Clothes):
    def tissue_required(self):
        return str(f'Для пошива костюма необходимо: {round((self.height * 2 / 0.3), 2)}')

coat = Coat(44, 160)
jacket = Jacket(44, 160)
print(coat.tissue_required())
print(jacket.tissue_required())
print(coat.tissue_required_full)
