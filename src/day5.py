file_path = "data/day5"


def expandRanges(ranges):
    """
    converts list of str of format "start-end" to list of tuples of format (start, end)
    """
    range_list = []
    for r in ranges:
        div = r.find("-")
        start, end = int(r[:div]), int(r[div + 1 :])
        range_list.append((start, end))
    # de-duplicate before returning
    return list(set(range_list))


def simplifyRanges(ranges):
    """
    simplifies ranges of format (start, end) to minimum bounds that cover original list
    """
    changed = False
    for r1 in ranges:
        for r2 in ranges:
            if r1 == r2:
                continue
            # check if there is another range with any overlap
            if r1[1] >= r2[0] and r1[0] <= r2[1]:
                # if we find overlap, remove both elements, and add the "super-range"
                ranges.remove(r1)
                ranges.remove(r2)
                ranges.append((min(r1[0], r2[0]), max(r1[1], r2[1])))
                changed = True
                break
        if changed:
            break
    # keep simplifying till no more changes
    if changed:
        return simplifyRanges(ranges)
    else:
        return ranges


def part1(ranges, items):
    total = 0
    for item in items:
        for r in ranges:
            if r[0] <= int(item) <= r[1]:
                total += 1
                break
    return total


def part2(ranges):
    total = 0
    for r in ranges:
        total += r[1] - r[0] + 1
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = [line.strip() for line in file]
    div = data.index("")
    ranges = expandRanges(data[:div])
    # break ranges down into simplest definitions - works for both parts
    ranges = simplifyRanges(ranges)
    items = data[div + 1 :]

    # print answers
    print("Part 1:", part1(ranges, items))
    print("Part 2:", part2(ranges))
