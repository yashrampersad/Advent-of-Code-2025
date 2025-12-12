from itertools import combinations

with open("Day 9/input.txt") as file:
    tiles = [[int(num) for num in line.split(",")] for line in file]

pairs = list(combinations(tiles, 2))

def part1():
    areas = sorted((abs(x[0][0]-x[1][0])+1) * (abs(x[0][1] - x[1][1])+1) for x in pairs)
    print(areas[-1])

def part2():
    xintervals = []
    yintervals = []
    for i in range(len(tiles)-1):
        if tiles[i][0] == tiles[i+1][0]:
            yintervals.append([[sorted([tiles[i][1], tiles[i+1][1]])], tiles[i][0]])
        else:
            xintervals.append([[sorted([tiles[i][0], tiles[i+1][0]])], tiles[i][1]])
    print(xintervals)
    print(yintervals)


    # for pair in pairs:
    #     valid = True
    #     ax = pair[0][0]
    #     bx = pair[1][0]
    #     ay = pair[0][1]
    #     by = pair[1][1]
    #     for tile in tiles:
    #         if ax > bx:
    #             if ay > by:
    #                 if ax>tile[0]>bx and ay>tile[1]>by:
    #                     valid = False
    #             else:
    #                 if ax>tile[0]>bx and by>tile[1]>ay:
    #                     valid = False
    #         else:
    #             if ay > by:
    #                 if bx>tile[0]>ax and ay>tile[1]>by:
    #                     valid = False
    #             else:
    #                 if bx>tile[0]>ax and by>tile[1]>ay:
    #                     valid = False
    #     # xrange = abs(pair[0][0] - pair[1][0])
    #     # yrange = abs(pair[0][1] - pair[1][1])
    #     # for tile in tiles:
    #     #     if abs(pair[0][0] - tile[0]) < xrange and abs(pair[0][1] - tile[1]) < yrange:
    #     #         valid = False
    #     #         print(f"--{pair} not valids")
    #     if valid:
    #         # print(pair)
    #         print((abs(pair[0][0]-pair[1][0])+1) * (abs(pair[0][1] - pair[1][1])+1))
    #     else:
    #         print(pair)


part2()

