import sys


def parse_time(elem):
    if elem:
        hour, minute, seconds = elem.split(":")
        return int(seconds) + 60 * int(minute) + 60 * 60 * int(hour)


def parse(ex):
    return [(parse_time(el.split(" ")[0]), int(el.split(" ")[1].split("x")[1])) for el in ex]


with open("<PATH>") as f:
    example = f.read()


example = example[:-1].split("\n")

print(example[548], example[547])

arr = parse(example)

idxs = []

arr = list(enumerate(arr))

arr.sort(key=lambda x:x[1][1])

print(arr)


for i in range(1, len(arr)):
    if arr[i][1][0] - arr[i-1][1][0] >= 3:
        idxs.append(arr[i-1][0])

print([el+1 for el in sorted(idxs)])
