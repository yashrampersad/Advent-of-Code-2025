import numpy as np
from itertools import combinations
import random

def part1():

    targets = []
    buttons = []

    with open("Day 10/input.txt") as file:
        for line in file:
            line = line.split(" ")
            light = []
            for char in line[0]:
                if char == ".":
                    light.append(0)
                elif char == "#":
                    light.append(1)
            light = np.array(light)
            targets.append(light)
            button_set = []
            for i in range(1, len(line)-1):
                button = []
                for k in range(len(line[0])-2):
                    button.append(0)
                button = np.array(button)
                line[i] = line[i].replace("(", "")
                line[i] = line[i].replace(")", "")
                for j in [int(x) for x in line[i].split(",")]:
                    button[j] = 1
                button_set.append(button)
            buttons.append(button_set)
        
    total = 0
    for i, target in enumerate(targets):
        found = False
        for j in range(len(buttons[i])):
            combs = list(combinations(buttons[i], j+1))
            for comb in combs:
                result = []
                for k in range(len(target)):
                    result.append(0)
                result = np.array(result)
                for button in comb:
                    result = result ^ button
                if "".join([str(x) for x in target]) == "".join([str(x) for x in result]):
                    total += j+1
                    found = True
                    break
            if found:
                break
            
    print(total)


def part2():
    targets = []
    buttons = []
    with open("Day 10/input.txt") as file:
        for line in file:
            line = line.split(" ")
            line[-1] = line[-1].replace("{", "")
            line[-1] = line[-1].replace("}", "")
            targets.append([int(x) for x in line[-1].split(",")])
            button_set = []
            for i in range(1, len(line)-1):
                line[i] = line[i].replace("(", "")
                line[i] = line[i].replace(")", "")
                button = [int(x) for x in line[i].split(",")]
                button_set.append(button)
            buttons.append(sorted(button_set, key=len, reverse=True))

    # print(buttons)
    # for i in range(len(buttons)):
    #     buttons[i] = buttons[i][::-1]
    #     buttons[i] = sorted(buttons[i], key=len, reverse=True)
    # print(buttons)

    total = 0
    for i, target in enumerate(targets):
        done = False
        while not done:
            presses = 0
            current = target.copy()
            for j in range(len(buttons[i])):
                affected = sorted([current[x] for x in buttons[i][j]])
                presses += affected[0]
                for index in buttons[i][j]: current[index] -= affected[0]
            print(current)
            if all(x==0 for x in current):
                total += presses
                done = True
            else:
                random.shuffle(buttons[i])
                buttons[i] = sorted(buttons[i], key=len, reverse=True)
                print(buttons[i])
            
    print(total)

    #25882 too high

part2()