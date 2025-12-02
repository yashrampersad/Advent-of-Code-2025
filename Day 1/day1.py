instructions = []

with open("Day 1/input.txt") as file:
    for line in file:
        instructions.append([line[0], int(line[1:])])

def part1():
    total = 0
    current = 50
    for instruction in instructions:
        if instruction[0] == "L":
            current -= instruction[1]
        else:
            current += instruction[1]
        current = current % 100
        if current == 0:
            total += 1

    print(total)

def part2():
    # total = 0
    # current = 50
    # for instruction in instructions:
    #     prev = current
    #     if instruction[0] == "L":
    #         current -= instruction[1]
    #     else:
    #         current += instruction[1]
    #     print(prev, current)
    #     if prev * current < 0:
    #         # print("click")
    #         # print ("adding ", abs(current // 100))
    #         total += abs(current // 100)
    #     elif current == 0 or current == 100:
    #         # print("click")
    #         total += 1
    #     elif abs(current) > 100:
    #         # print("click")
    #         # print ("adding ", abs(current // 100))
    #         total += abs(current // 100)
    #     current = current % 100
    # print(total)

    total = 0
    current = 50
    for instruction in instructions:
        prev = current
        if instruction[0] == "L":
            current -= instruction[1]
        else:
            current += instruction[1]
        print(prev, instruction[0], current)
        if current < 0 and current % 100 == 0:
            print("adding ", abs(current // 100)+1)
            total += abs(current // 100) + 1
        elif (prev==0 and current <=-100):
            print("adding ", abs(current // 100)-1)
            total += abs(current // 100)-1
        elif (current < 0 and prev != 0) or current >= 100:
            print("adding ", abs(current // 100))
            total += abs(current // 100)
        if current == 0:
            print("adding 1")
            total += 1
        current = current % 100

    print(total)

# def part3():
#     total = 0
#     current = 50
#     for instruction in instructions:
#         if instruction[0] == "L":
#             if current == 0:
#                 current += 100
#             current -= instruction[1]
#         else:
#             current += instruction[1]
#         if current == 0:
#             total += 1
#         else:
#             total += abs(current // 100)
#         current = current % 100

#     print(total)

# part2()
# part3()
# print(-100//100)
# 6547 too low
# 5941 too low

# 6554