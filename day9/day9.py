import itertools as it

def parseString(s):
    res = s.split(' ')
    res.remove('to')
    res.remove('=')
    res[-1] = int(res[-1])
    return res

data = open('day9/day9.txt').read().split('\n')
data = [parseString(l) for l in data]
cities = {l[0] for l in data}.union({l[1] for l in data})
rides = {l:{} for l in cities}
for l in data:
    rides[l[0]][l[1]] = l[2]
    rides[l[1]][l[0]] = l[2]

def part1():
    perm = list(it.permutations(rides.keys()))
    for i in range(len(perm)):
        perm[i] = list(perm[i])
        for j in range(len(perm[i]) - 1):
            perm[i][j] = rides[perm[i][j]][perm[i][j + 1]]
        perm[i].pop()
        perm[i] = sum(perm[i])
    return min(perm)

def part2():
    perm = list(it.permutations(rides.keys()))
    for i in range(len(perm)):
        perm[i] = list(perm[i])
        for j in range(len(perm[i]) - 1):
            perm[i][j] = rides[perm[i][j]][perm[i][j + 1]]
        perm[i].pop()
        perm[i] = sum(perm[i])
    return max(perm)

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')