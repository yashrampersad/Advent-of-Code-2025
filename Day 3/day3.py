joltage = []
with open("Day 3/input.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        joltage.append([int(i) for i in line])

def part1():
    total = 0
    for jolt in joltage:
        digits = ""
        ordered = sorted(jolt)
        ordered.reverse()
        digindex = len(jolt) - 1
        i = 0
        while digindex == len(jolt)-1:
            dig1 = ordered[i]
            digindex = jolt.index(dig1)
            i += 1
        digits += str(dig1)
        sublist = sorted(jolt[digindex+1:])
        sublist.reverse()
        digits += str(sublist[0])
        total += int(digits)

    print(total)

def part2():

    def selectdigits(sublist, digits):
        if digits <= 0:
            return ""
        largestnum = -1
        for num in sublist[:len(sublist)-digits+1]:
            if num == 9:
                return str(num) + selectdigits(sublist[sublist.index(num)+1:], digits-1)
            elif num > largestnum:
                largestnum = num
        return str(largestnum) + selectdigits(sublist[sublist.index(largestnum)+1:], digits-1)
    

    total = 0
    for jolt in joltage:
        total += int(selectdigits(jolt, 12))

    print(total)



part2()