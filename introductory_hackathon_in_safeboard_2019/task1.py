# example = """10:00 87
# 10:01 81
# 10:02 94
# 10:03 141
# 10:04 116
# 10:05 79
# 10:06 139"""
import sys


def parse_str_to_list(ex_str):
    arr = [el.split(" ") for el in ex_str]
    for el in arr:
        el[1] = int(el[1].split("\\")[0])
    return arr


def find_better(input_list):
    test = input_list.copy()
    max_el = max(test, key=lambda x: x[1])
    min_el = max_el
    while min_el[0] >= max_el[0]:
        test.remove(min_el)
        min_el = min(test, key=lambda x: x[1])

    return min_el, max_el


def prety_output(ex_tuple):
    arr = []
    arr.append(ex_tuple[0][0])
    arr.append(ex_tuple[1][0])
    arr.append(str(ex_tuple[1][1] - ex_tuple[0][1]))
    return " ".join(arr)


example = sys.stdin.readlines()
print(example)


arr = parse_str_to_list(example)
print(prety_output(find_better(arr)))
