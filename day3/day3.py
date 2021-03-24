directions = open('day3/day3.txt').read()

def part1():
    homes = {(0, 0)}
    x, y = 0, 0
    for d in directions:
        if d == '^':
            y += 1
        elif d == 'v':
            y -= 1
        elif d == '>':
            x += 1
        elif d == '<':
            x -= 1
        homes.add((x, y))
    return len(homes)

def part2():
    homes = {(0, 0)}
    x = [0, 0]
    y = [0, 0]
    for i, d in enumerate(directions):
        if d == '^':
            y[i % 2] += 1
        elif d == 'v':
            y[i % 2] -= 1
        elif d == '>':
            x[i % 2] += 1
        elif d == '<':
            x[i % 2] -= 1
        homes.add((x[i % 2], y[i % 2]))
    return len(homes)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")

# other interesting solution seen on Reddit from u/ilmale:

# def update_pos(c, p):
#     return {'>': (p[0] + 1, p[1]), '<': (p[0] - 1, p[1]), '^': (p[0], p[1] + 1), 'v': (p[0], p[1] - 1)}[c]

# content = directions
# pos = [(0, 0), (0,0)]
# visited_houses = { (0,0): True }
# for i in range( len(content)):
#     t = pos[i%2] = update_pos(content[i], pos[i%2])
#     visited_houses[t] = True
# print(len(visited_houses))