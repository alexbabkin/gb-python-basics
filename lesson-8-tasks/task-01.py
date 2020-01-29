#
# Task 1.
#


class MyDate:
    # по условию задачи нужен конструктор,
    # но не понятно зачем...
    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def to_number(cls, data_str):
        day, month, year = list(map(int, data_str.split('-')))
        cls.validate(day, month, year)
        day_str = f'0{day}' if day < 10 else f'{day}'
        month_str = f'0{month}' if month < 10 else f'{month}'
        year_str = str(year)
        return int(day_str + month_str + year_str)

    @staticmethod
    def validate(day, month, year):
        # year is always ok, even if < 0
        if month < 1 or month > 12:
            raise ValueError("Month is not correct")
        if day < 1 or day > 31:
            raise ValueError("Day is not correct")


print(MyDate.to_number('12-01-2020'))
print(MyDate.to_number('12-91-2020'))
