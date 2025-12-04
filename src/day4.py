file_path = "data/day4"


def findRemovals(data):
    total = 0
    rows, cols = len(data), len(data[0])
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == ".":
                continue
            count = 0
            for a in range(max(0, i - 1), min(rows, i + 2)):
                for b in range(max(0, j - 1), min(cols, j + 2)):
                    # avoid checking same cell
                    if a == i and b == j:
                        continue
                    # removals count as "present" while in-iteration
                    if data[a][b] in ("@", "x"):
                        count += 1
            if count < 4:
                total += 1
                data[i][j] = "x"
    return total, data


def part1(data):
    removals, _ = findRemovals(data)
    return removals


def part2(data):
    total = 0
    removals = 1
    while removals > 0:
        removals, new_data = findRemovals(data)
        # reset data with previous removals not showing up anymore
        data = [["." if ch == "x" else ch for ch in line] for line in new_data]
        total += removals
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = [list(line[:-1]) for line in file]

    # print answers
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
