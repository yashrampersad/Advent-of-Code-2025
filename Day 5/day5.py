ranges = []
foods = []

with open("Day 5/input.txt") as file:
    addingranges = True
    for line in file:
        if line == "\n":
            addingranges = False
        elif addingranges:
            ranges.append([int(x) for x in line.split("-")])
        else:
            foods.append(int(line))

def part1():
    fresh = 0
    for food in foods:
        for range in ranges:
            if range[0] <= food <= range[1]:
                fresh += 1
                break

    print(fresh)

def part2():
    # ranges is a 2d array of all ranges eg. [[3,5], [10,14], [16,20], [12,18]]

    ranges.sort()

    # merge overlapping intervals
    done = False
    i = 0
    while not done:
        range1 = ranges[i]
        range2 = ranges[i+1]
        if range1[1]+1 >= range2[0]: # overlap
            if range1[1] > range2[1]:
                newrange = range1
            else:
                newrange = [range1[0], range2[1]]
            ranges.pop(i)
            ranges.pop(i)
            ranges.insert(i, newrange)
        else:
            i += 1
        if i >= len(ranges)-1:
            done = True

    # calculate total of interval differences
    total = 0
    for range in ranges:
        total += (range[1] - range[0]) + 1
    print(total)

part2()