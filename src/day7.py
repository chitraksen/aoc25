# need to pass list by value 😓
import copy

file_path = "data/day7"


def part1(data):
    """
    nothing fancy, just simulates all the splits and counts during the process
    """
    splits = 0
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            if el == "^" and data[i - 1][j] == "|":
                splits += 1
                data[i][j - 1] = "|"
                data[i][j + 1] = "|"
            elif data[i - 1][j] == "|":
                data[i][j] = "|"
    return splits


def part2(data):
    """
    we start with 1 timeline for the line below `S` and make the number
    "trickle-down" while splitting at the splitters. for first times, it trickles
    down the same value because so far it can be reached exactly as many ways
    as the previous line. we add up the different timelines in spots where
    multiple timelines can reach.
    """
    # replace first bar with 1 - exactly 1 timeline if grid ended here
    for i, el in enumerate(data[1]):
        if el == "|":
            data[1][i] = 1
    for i, row in enumerate(data):
        for j, el in enumerate(row):
            # check if we have a splitter and ray - ray is replaced by ints in this schema
            if el == "^" and isinstance(data[i - 1][j], int):
                # for splits we add up if something has already reached here
                if isinstance(data[i][j - 1], int):
                    data[i][j - 1] += data[i - 1][j]
                # and trickle down exact value if it's the first time reaching here
                else:
                    data[i][j - 1] = data[i - 1][j]
                # repeat for right hand split
                if isinstance(data[i][j + 1], int):
                    data[i][j + 1] += data[i - 1][j]
                else:
                    data[i][j + 1] = data[i - 1][j]
            # trickle down same value if ray exists and no split
            elif isinstance(data[i - 1][j], int):
                if isinstance(data[i][j], int):
                    data[i][j] += data[i - 1][j]
                else:
                    data[i][j] = data[i - 1][j]

    # count all the rays that reached the bottom row. each element will have the
    # number of different timelines that can end up there.
    total = 0
    for el in data[-1]:
        if isinstance(el, int):
            total += el
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = [list(line[:-1]) for line in file]
    for i, el in enumerate(data[0]):
        if el == "S":
            data[1][i] = "|"

    # print answers
    print("Part 1:", part1(copy.deepcopy(data)))
    print("Part 2:", part2(data))
