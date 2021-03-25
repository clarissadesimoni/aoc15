data = open('day6/day6.txt').read().split('\n')

def part1():
    grid = [[0] * 1000 for _ in range(1000)]
    for line in data:
        items = line.split(' ')
        if items[0] == 'turn':
            items[0:2] = [' '.join(items[0:2])]
        items.pop(2)
        for i in range(1, 3):
            items[i] = [int(n) for n in items[i].split(',')]
        if items[0] == 'toggle':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] = int(not bool(grid[i][j]))
        elif items[0] == 'turn on':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] = 1
        elif items[0] == 'turn off':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] = 0
    return sum(map(lambda g: sum(g), grid))

def part2():
    grid = [[0] * 1000 for _ in range(1000)]
    for line in data:
        items = line.split(' ')
        if items[0] == 'turn':
            items[0:2] = [' '.join(items[0:2])]
        items.pop(2)
        for i in range(1, 3):
            items[i] = [int(n) for n in items[i].split(',')]
        if items[0] == 'toggle':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] += 2
        elif items[0] == 'turn on':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] += 1
        elif items[0] == 'turn off':
            for i in range(items[1][1], items[2][1] + 1):
                for j in range(items[1][0], items[2][0] + 1):
                    grid[i][j] = max(0, grid[i][j] - 1)
    return sum(map(lambda g: sum(g), grid))

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')