file_path = "data/day6"


def divideNumbers(data):
    """
    change data format to make every operation a single row. last element of
    each row will have the operator. all numbers will retain respective
    whitespaces, but operators won't.
    """

    divs = []
    counter = 0
    # figure out spacing from last row - operator is always at pos 0 of new col
    for ch in data[-1]:
        if ch in ("+", "*"):
            divs.append(counter)
        counter += 1

    # divide data based on operator spacing. for each div, go through all rows
    # and find element based on that div.
    split_data = []
    for i in range(len(divs)):
        curr_split = []
        for row in data:
            if i != len(divs) - 1:
                curr_split.append(row[divs[i] : divs[i + 1] - 1])
            else:
                curr_split.append(row[divs[i] :])
        split_data.append(curr_split)
    # strip operator whitespaces - not required anywhere
    for i in range(len(split_data)):
        split_data[i][-1] = split_data[i][-1].strip()
    return split_data


def part1(data):
    total = 0
    for row in data:
        op = row[-1]
        if op == "+":
            subtotal = 0
        else:
            subtotal = 1
        for el in row[:-1]:
            if op == "+":
                subtotal += int(el.strip())
            else:
                subtotal *= int(el.strip())
        total += subtotal
    return total


def part2(data):
    total = 0
    for row in data:
        op = row[-1]
        if op == "+":
            subtotal = 0
        else:
            subtotal = 1
        # figure out new "vertical" numbers using size of elements
        el_size = len(row[0])
        # start counting on right hand side, concatenating i'th digit from each number
        for i in range(-1, -el_size - 1, -1):
            curr_num = ""
            for el in row[:-1]:
                if el[i] == " ":
                    continue
                else:
                    # string concat
                    curr_num += el[i]
            if op == "+":
                subtotal += int(curr_num)
            else:
                subtotal *= int(curr_num)
        total += subtotal
    return total


def entry():
    # read data
    with open(file_path) as file:
        data = [line[:-1] for line in file]
    data = divideNumbers(data)

    # print answers
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
