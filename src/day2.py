file_path = "data/day2"


def part1(data):
    total = 0
    for id_range in data:
        for i in range(id_range[0], id_range[1] + 1):
            i_str = str(i)
            length = len(i_str)
            # can only be invalid if it has even number of digits
            if length % 2 != 0:
                continue
            # check both parts equal for invalidity
            if (i_str[: length // 2]) == (i_str[length // 2 :]):
                total += i
    return total


def part2(data):
    total = 0
    for id_range in data:
        for i in range(id_range[0], id_range[1] + 1):
            i_str = str(i)
            length = len(i_str)
            # go through all j subdivisions of string
            for j in range(2, length + 1):
                # string should divide into j equal parts
                if length % j != 0:
                    continue
                # check if all divisions are equal
                if i_str == i_str[: (length // j)] * j:
                    total += i
                    break
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = (file.readline()).strip().split(",")
    data = [tuple(map(int, item.split("-"))) for item in data]

    # print answers
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
