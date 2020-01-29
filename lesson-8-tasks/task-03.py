#
# Task 3.
#


class NonNumError(BaseException):
    pass


# don't want to use additional try...except here
def to_num(s):
    if s[0] in ('+', '-'):
        s = s[1:]
    if s.count('.') > 1:
        raise NonNumError('Error: input is not a number')
    for p in s.split('.'):
        if not p.isdigit():
            raise NonNumError('Error: input is not a number')
    return float(s)


nums = []
while True:
    user_input = input('Введите следующее значение: ')
    if user_input == 'stop':
        break
    try:
        num = to_num(user_input)
        nums.append(num)
    except NonNumError as e:
        print(e)

print(nums)
