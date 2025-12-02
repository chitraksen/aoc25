file_path = "data/day1"

def part1(data):
    current_pos = 50
    pass_counter = 0
    for rotation in data:
        # effective rotations
        rotation_amt = int(rotation[1:]) % 100
        if rotation[0] == "R":
            current_pos += rotation_amt
        else:
            current_pos -= rotation_amt
        # reset to 0-99 value. works for both +ve & -ve
        current_pos = current_pos % 100
        # check if it ends up at 0
        if current_pos == 0:
            pass_counter += 1
    return pass_counter


def part2(data):
    current_pos = 50
    pass_counter = 0
    for rotation in data:
        # get effective rotations, but this time every circle counts as a pass too
        rotation_amt = int(rotation[1:])
        pass_counter += rotation_amt // 100
        rotation_amt %= 100
        old_pos = current_pos
        # don't need to do anything if no effective rotations
        if rotation_amt == 0:
            continue
        if rotation[0] == "R":
            current_pos += rotation_amt
        else:
            current_pos -= rotation_amt
        # check if it cross 0 during rotation
        # crossing 100 must mean it has crossed 0
        # crossing into -ve would only count as crossing 0 if it didn't start at 0
        if current_pos >= 100 or (old_pos > 0 and current_pos <= 0):
            pass_counter += 1
        # reset position
        current_pos %= 100
    return pass_counter


def entry():
    # read data
    with open(file_path) as file:
        data = [line[:-1] for line in file]

    # print answers
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
