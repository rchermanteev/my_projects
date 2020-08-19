from math import comb

# №100.txt - Ошибка WA

def get_sum(layers):
    res = 0
    for i, x in enumerate(layers):
        binominal_coefficients = [comb(len(x) - 1, i) for i in range(len(x))]
        for element, coefficient in zip(x, binominal_coefficients):
            res += element * coefficient * 2 ** (max_depth - 1 - i)

    return res


number_banks = int(input())

for _ in range(number_banks):
    max_depth = int(input())
    layers = []
    for _ in range(max_depth):
        layers.append([int(el) for el in input().split()])

    res = get_sum(layers)
    number_way = 2 ** (max_depth - 1)

    while res % 2 == 0 and number_way != 1:
        res /= 2
        number_way /= 2

    print(f"{int(res)} {int(number_way)}")
