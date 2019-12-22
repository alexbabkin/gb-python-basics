#
# Task 2.
#

input_seconds = int(input('Введите количество секунд: '))

hours = input_seconds // 3600
minutes = (input_seconds - hours * 3600) // 60
seconds = input_seconds - hours * 3600 - minutes * 60

hours_str = str(hours)
if hours < 10:
    hours_str = '0' + hours_str

minutes_str = str(minutes)
if minutes < 10:
    minutes_str = '0' + minutes_str

seconds_str = str(seconds)
if seconds < 10:
    seconds_str = '0' + seconds_str

print(f'{hours_str}:{minutes_str}:{seconds_str}')
