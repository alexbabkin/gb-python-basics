#
# Task 3.
#


def sum_of_2_maxs_1(param1, param2, param3):
    # this approach can be used in case of more than 3 parameters (another implementation required)
    args_list = [param1, param2, param3]
    max_1 = max(args_list)
    args_list.remove(max_1)
    max_2 = max(args_list)
    return max_1 + max_2


def sum_of_2_maxs_2(param1, param2, param3):
    args_list = [param1, param2, param3]
    args_list.remove(min(args_list))
    # cannot use sum(lst) because of non-number inputs case
    return args_list[0] + args_list[1]

# Description of the task doesn't say anything about the types of the function arguments
# so check this function with int's, floats and strings (with default comparator)


print(f'sum_of_2_maxs_1(3, 6, 0) = {sum_of_2_maxs_1(3, 6, 0)}')
print(f'sum_of_2_maxs_1(1.3, 4.4, 6.4) = {sum_of_2_maxs_1(1.3, 4.4, 6.4)}')
print(f'sum_of_2_maxs_1(\'str1\', \'str2\', \'str3\') = {sum_of_2_maxs_1("str1", "str2", "str3")}')

print(f'sum_of_2_maxs_2(3, 6, 0) = {sum_of_2_maxs_2(3, 6, 0)}')
print(f'sum_of_2_maxs_2(1.3, 4.4, 6.4) = {sum_of_2_maxs_2(1.3, 4.4, 6.4)}')
print(f'sum_of_2_maxs_2(\'str1\', \'str2\', \'str3\') = {sum_of_2_maxs_2("str1", "str2", "str3")}')
