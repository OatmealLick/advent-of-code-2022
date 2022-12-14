from functools import reduce


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(f"2015/day1/{filename}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
        print(solve(lines[:]))


def solve(lines):
    line = lines[0]
    return reduce(lambda acc, x: (acc[0] + 1, acc[1] + (1 if x == '(' else -1)) if acc[1] >= 0 else acc, line, (0, 0))[0]


if __name__ == "__main__":
    main()
