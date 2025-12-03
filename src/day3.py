file_path = "data/day3"


def largestSubNumber(num: str, dig: int, cum: str = "") -> str:
    """
    finds largest `dig` digit number, from `num` and adds it to the cumulated `cum` string
    """
    # find largest digit in "valid" portion of string. if we want a 12 digit
    # sub-number we would want to check largest digit that's outside of the last
    # 11 digits. if-else manages -0 case which should include all digits.
    search_num = num[: -(dig - 1)] if dig > 1 else num

    for i in range(9, -1, -1):
        pos_i = search_num.find(str(i))
        if pos_i >= 0:
            # keep searching as long as we need at least 1 more digit
            if dig > 1:
                return largestSubNumber(num[pos_i + 1 :], dig - 1, cum + num[pos_i])
            else:
                return cum + num[pos_i]
    return ""


def part1(data):
    total = 0
    for bank in data:
        total += int(largestSubNumber(bank, 2))
    return total


def part2(data):
    total = 0
    for bank in data:
        total += int(largestSubNumber(bank, 12))
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = [line[:-1] for line in file]

    # print answers
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
