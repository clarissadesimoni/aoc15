from functools import reduce

data = open('day2/day2.txt').read().split('\n')

def getBoxSurface(line):
    length, width, height = [int(d) for d in line.split('x')]
    areas = [length * width, length * height, width * height]
    return 2 * sum(areas) + min(areas)

def part1():
    return sum([getBoxSurface(l) for l in data])

def getRibbon(line):
    dims = sorted([int(d) for d in line.split('x')])
    return 2 * sum(dims[:-1]) + reduce((lambda x, y: x * y), dims)

def part2():
    return sum([getRibbon(l) for l in data])

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")