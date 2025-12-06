def part1():
    symbols = []
    numbers = []
    addingnumbers = True
    with open("Day 6/input.txt") as file:
        for line in file:
            if not line[0].isnumeric() and line[0] != " ":
                addingnumbers = False
            if addingnumbers:
                numbers.append([int(x) for x in line.split(" ") if x != "" and x != "\n"])
            else:
                symbols = [x for x in line.split(" ") if x != ""]

    grandtotal = 0
    for i in range(len(numbers[0])):
        total = numbers[0][i]
        if symbols[i] == "*":
            for j in range(1, len(numbers)):
                total *= numbers[j][i]
        else:
            for j in range(1, len(numbers)):
                total += numbers[j][i]
        grandtotal += total

    print(grandtotal)

def part2():
    symbols = []
    numbers = []
    addingnumbers = True
    with open("Day 6/input.txt") as file:
        for line in file:
            if not line[0].isnumeric() and line[0] != " ":
                addingnumbers = False
            if addingnumbers:
                numbers.append([x for x in line if x != "\n"])
            else:
                symbols = [x for x in line.split(" ") if x != ""]
    for num in numbers:
        num.append(" ")
    
    grandtotal = 0
    total = 0
    question = 0
    for x in range(len(numbers[0])):
        num = ""
        for y in range(len(numbers)):
            num += numbers[y][x] # put together the vertical number
        try:
            num = int(num) # "  2" conveniently converts to 2
            if total == 0 or symbols[question] == "+":
                total += num
            else:
                total *= num
        except ValueError: # "   " fully blank space indicates that question is finished
            grandtotal += total
            total = 0
            question += 1
    print(grandtotal)

part2()
        


# a = "  2    "
# print(int(a))