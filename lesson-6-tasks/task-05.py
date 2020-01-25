#
# Task 5
#


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Будет изображена {self.title}')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Отрисовываем {self.title}')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Рисуем {self.title}')


lst = [Pen('Ручка'), Pencil('Карандаш'), Handle('Маркер')]
for s in lst:
    s.draw()
