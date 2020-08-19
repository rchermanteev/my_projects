import sys
import difflib


def task(ex):
    for i in range(len(ex)):
        for j in range(len(ex)):
            diff = difflib.ndiff(ex[i], ex[j])
            print(list(difflib.restore(diff, 1)))


example = sys.stdin.readlines()
example = [el.replace("\n", "") for el in example]

task(example)
