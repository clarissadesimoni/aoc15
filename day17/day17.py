import itertools

data = list(map(int, open('day17/day17.txt').read().strip().split('\n')))
data = [int(line) for line in data]

def part1():
    total = 0
    for i in range(len(data)):
        subtotal = 0
        for combination in itertools.combinations(data, i):
            if sum(combination) == 150:
                subtotal += 1
        total += subtotal
    return total

def part2():
    seen = []
    for i in range(len(data)):
        for combination in itertools.combinations(data, i):
            combination = tuple(sorted(combination))
            if sum(combination) == 150:
                seen.append(combination)
    target = min(len(x) for x in seen)
    return len(list(filter(lambda x: len(x) == target, seen)))

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
# high: 402