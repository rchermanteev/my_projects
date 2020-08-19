def iterate_spare_number(sec, len_num):
    if sec == 1:
        sec = len_num
        len_num += 1
        return sec, len_num
    elif sec > 1:
        return sec - 1, len_num


def construct_spare_number(position):
    first_1 = 0
    second_1 = 1
    len_number = 2
    sequential_number = 1
    while sequential_number != position and position != 0:
        second_1, len_number = iterate_spare_number(second_1, len_number)
        sequential_number += 1
    return first_1, second_1, len_number


def get_result(position):
    mod = 35184372089371
    fir, sec, len_num = construct_spare_number(position)
    return (2**(len_num - 1 - fir) + 2**(len_num - 1 - sec)) % mod


number_banks = int(input())

for _ in range(number_banks):
    k = int(input())
    print(get_result(k))
