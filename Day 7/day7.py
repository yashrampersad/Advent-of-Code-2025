with open("Day 7/input.txt") as file:
    map = [[char for char in line.strip()] for line in file]

def part1():
    beams = [] # holds indexes of beams on a current layer
    beams.append(map[0].index("S"))
    total = 0
    for i in range(1, len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^" and j in beams: # collision occured
                total += 1
                beams.remove(j)
                # split beam into +-1 if not there already
                if j-1 not in beams:
                    beams.append(j-1)
                if j+1 not in beams:
                    beams.append(j+1)

    print(total)

def part2():
    beams = {}
    beams[map[0].index("S")] = 1
    for i in range(1, len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^" and j in beams and beams[j] > 0: # collision occured
                num = beams[j]
                beams[j] = 0
                if j+1 not in beams:
                    beams[j+1] = num
                else:
                    beams[j+1] += num
                if j-1 not in beams:
                    beams[j-1] = num
                else:
                    beams[j-1] += num

    print(sum(beams.values()))

part2()