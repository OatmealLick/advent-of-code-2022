from functools import reduce
from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day3/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:][0]))


def solve(line):
    hs = defaultdict(int)
    c = (0, 0)
    cr = (0, 0)
    hs[c] += 2
    for i, d in enumerate(map(dir, line)):
        if i % 2 == 0:
            c = plus(c, d)
            hs[c] += 1
        else:
            cr = plus(cr, d)
            hs[cr] += 1
    return len(hs)


def plus(a, b):
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by

def dir(c):
    match c:
        case ">":
            return 1, 0
        case "<":
            return -1, 0
        case "^":
            return 0, 1
        case "v":
            return 0, -1 

if __name__ == "__main__":
    main()

