#
# Task 3.
#


def sum_of_2_maxs(param1, param2, param3):
    args_list = [param1, param2, param3]
    max_1 = max(args_list)
    args_list.remove(max_1)
    max_2 = max(args_list)
    return max_1 + max_2


# Description of the task doesn't say anything about the types of the function arguments
# so check this function with int's, floats and strings (with default comparator)

print(sum_of_2_maxs(3, 6, 0))
print(sum_of_2_maxs(1.3, 4.4, 6.4))
print(sum_of_2_maxs('str1', 'str2', 'str3'))
