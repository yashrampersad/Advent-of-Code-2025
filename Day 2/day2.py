def part1():

    intervals = []

    with open("Day 2/input.txt") as file:
        for line in file:
            for interval in line.split(","):
                if interval != "\n":
                    intervals.append([int(interval.split("-")[0]), int(interval.split("-")[1])])

    total = 0
    for start, end in intervals:
        for num in range(start, end+1):
            num = str(num)
            half1 = num[len(num)//2:]
            half2 = num[:len(num)//2]
            if half1 == half2:
                total += int(num)

    print(total)

def part2():

    intervals = []

    with open("Day 2/input.txt") as file:
        for line in file:
            for interval in line.split(","):
                if interval != "\n":
                    intervals.append([int(interval.split("-")[0]), int(interval.split("-")[1])])

    total = 0
    for start, end in intervals:
        for num in range(start, end+1):
            num = str(num)
            cache = num[0]
            ptr = 0
            i = 0
            while i < len(num):
                if ptr >= len(cache):
                    ptr = 0
                # print("comparing", num[i], cache[ptr])
                if num[i] != cache[ptr]:
                    cache = num[:len(cache)+1]
                    # print("mismatch, cache now", cache)
                    ptr = 0
                    i = 0
                else:
                    ptr += 1
                    i += 1
            if len(cache) != len(num) and len(num)%len(cache) == 0:
                total += int(num)

    print(total)

# num = "929929929"
# cache = num[0]
# ptr = 0
# i = 0
# while i < len(num):
#     if ptr >= len(cache):
#         ptr = 0
#     print("comparing", num[i], cache[ptr])
#     if num[i] != cache[ptr]:
#         cache = num[:len(cache)+1]
#         print("mismatch, cache now", cache)
#         ptr = 0
#         i = 0
#     else:
#         ptr += 1
#         i += 1
# if len(cache) != len(num) and len(num)%len(cache) == 0:
#     print(num, cache)

part2()

# for i in range (2,4):
#     print(i)

#19096724154 too low
#86945797859