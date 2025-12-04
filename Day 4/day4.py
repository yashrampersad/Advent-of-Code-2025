import numpy as np
from scipy.signal import convolve2d
import time

map = []

with open("Day 4/input.txt") as file:
    for line in file:
        row = []
        for char in line:
            if char != "\n":
                row.append(char)
        map.append(row)

def part1():
    total = 0
    for i, row in enumerate(map):
        for j, square in enumerate(row):
            if square == "@":
                adj = 0
                for y in range(-1,2):
                    for x in range(-1,2):
                        if 0 <= i+y < len(map) and 0 <= x+j < len(map[0]) and (x != 0 or y != 0) and map[i+y][x+j] == "@":
                            adj += 1
                if adj < 4:
                    total += 1

    print(total)

def part2():
    map = []
    with open("Day 4/input.txt") as file:
        for line in file:
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            map.append(row)

    grand_total = 0
    total = -1

    while total != 0:
        total = 0
        for i, row in enumerate(map):
            for j, square in enumerate(row):
                if square == "@":
                    adj = 0
                    for y in range(-1,2):
                        for x in range(-1,2):
                            if 0 <= i+y < len(map) and 0 <= x+j < len(map[0]) and (x != 0 or y != 0) and map[i+y][x+j] == "@":
                                adj += 1
                    if adj < 4:
                        total += 1
                        map[i][j] = "."
        grand_total += total

    print(grand_total)
    

def part2optimised():
    map = []
    with open("Day 4/input.txt") as file:
        for line in file:
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            map.append(row)

    inp = (np.array(map) == "@").astype(int)

    kernel = np.array([[1,1,1],
                    [1,0,1],
                    [1,1,1]])

    grandtotal = 0
    total = -1
    while total != 0:
        total = 0
        result = convolve2d(inp, kernel, mode="same", boundary="fill", fillvalue=0) * inp
        result = result * inp
        result = (result >= 4).astype(int)
        total = np.sum(inp) - np.sum(result)
        grandtotal += total
        inp = result
    print(grandtotal)            

start = time.time()
part2()
end = time.time()
two = end-start

start = time.time()
part2optimised()
end = time.time()
twoopt = end-start

print(two, twoopt)
