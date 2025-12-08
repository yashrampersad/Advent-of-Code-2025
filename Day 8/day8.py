import numpy as np
from itertools import combinations

with open("Day 8/input.txt") as file:
    points = [np.array([int(x[0]),int(x[1]),int(x[2])]) for x in [line.strip().split(",") for line in file]]
    
def mag(point): # magnitude
    return point[0]**2 + point[1]**2 + point[2]**2


set = list(combinations(points, 2))
a = sorted([[mag(x[0] - x[1]), x] for x in set])

def part1():

    circuits = []
    for i in range(1000):
        point1 = f"{a[i][1][0][0]} {a[i][1][0][1]} {a[i][1][0][2]}"
        point2 = f"{a[i][1][1][0]} {a[i][1][1][1]} {a[i][1][1][2]}"
        point1index = -1
        point2index = -1
        for j in range(len(circuits)):
            if point1 in circuits[j]:
                point1index = j
            if point2 in circuits[j]:
                point2index = j
        if point1index >= 0 and point2index >= 0:
            pass
            if point1index != point2index:
                circuits.append(circuits[point1index]+circuits[point2index])
                if point1index > point2index:
                    circuits.pop(point1index)
                    circuits.pop(point2index)
                else:
                    circuits.pop(point2index)
                    circuits.pop(point1index)
        elif point1index >= 0:
            circuits[point1index].append(point2)
        elif point2index >= 0:
            circuits[point2index].append(point1)
        else:
            circuits.append([point1, point2])

    # strpoints = [f"{point[0]} {point[1]} {point[2]}" for point in points]
    # indexes = []
    # for circuit in circuits:
    #     indexes.append([strpoints.index(point) for point in circuit])
    # print(indexes)

    nums = sorted([len(circuit) for circuit in circuits])
    print(nums[-1] * nums[-2] * nums[-3]) # top 3 because list sorts adcending order

def part2():

    circuits = []
    i = 0
    while len(circuits) == 0 or len(circuits[-1]) != len(points):
        point1 = f"{a[i][1][0][0]} {a[i][1][0][1]} {a[i][1][0][2]}"
        point2 = f"{a[i][1][1][0]} {a[i][1][1][1]} {a[i][1][1][2]}"
        point1index = -1
        point2index = -1
        for j in range(len(circuits)):
            if point1 in circuits[j]:
                point1index = j
            if point2 in circuits[j]:
                point2index = j
        if point1index >= 0 and point2index >= 0:
            pass
            if point1index != point2index:
                circuits.append(circuits[point1index]+circuits[point2index])
                if point1index > point2index:
                    circuits.pop(point1index)
                    circuits.pop(point2index)
                else:
                    circuits.pop(point2index)
                    circuits.pop(point1index)
        elif point1index >= 0:
            circuits[point1index].append(point2)
        elif point2index >= 0:
            circuits[point2index].append(point1)
        else:
            circuits.append([point1, point2])
        i += 1

    print(int(point1.split(" ")[0]) * int(point2.split(" ")[0]))

part1()
part2()
