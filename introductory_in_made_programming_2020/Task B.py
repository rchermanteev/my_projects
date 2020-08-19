def get_result(points):
    result = 0

    for first_point in points:
        for second_point in points:
            if first_point[0] != second_point[0] and first_point[1] != second_point[1]:

                third_point = (first_point[0], second_point[1])
                fourth_point = (second_point[0], first_point[1])
                if third_point in points:
                    if fourth_point in points:
                        result += 1
    return result // 4


number_banks = int(input())

for _ in range(number_banks):
    points = set()
    count = int(input())
    for point in range(count):
        points.add(tuple([int(coord) for coord in input().strip().split()]))

    print(get_result(points))
