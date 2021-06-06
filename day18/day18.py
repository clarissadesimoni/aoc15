def part1():
    corners = set()
    with open('day18/day18.txt') as f:
        lights = corners | {(x,y) for y, line in enumerate(f) for x, char in enumerate(line.strip()) if char == '#'}
    neighbours = lambda x,y: sum((_x,_y) in lights for _x in (x - 1, x, x + 1) for _y in (y - 1, y, y + 1) if (_x, _y) != (x, y))
    for _ in range(100):
        lights = corners | {(x,y) for x in range(100) for y in range(100) if (x,y) in lights and 2 <= neighbours(x,y) <= 3 or (x,y) not in lights and neighbours(x,y) == 3}
    return len(lights)


def part2():
    corners = {(0,0), (0,99), (99,0), (99,99)}
    with open('day18/day18.txt') as f:
        lights = corners | {(x,y) for y, line in enumerate(f) for x, char in enumerate(line.strip()) if char == '#'}
    neighbours = lambda x,y: sum((_x,_y) in lights for _x in (x - 1, x, x + 1) for _y in (y - 1, y, y + 1) if (_x, _y) != (x, y))
    for _ in range(100):
        lights = corners | {(x,y) for x in range(100) for y in range(100) if (x,y) in lights and 2 <= neighbours(x,y) <= 3 or (x,y) not in lights and neighbours(x,y) == 3}
    return len(lights)

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
# low: 865
#high: 1294