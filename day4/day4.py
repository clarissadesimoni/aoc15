import hashlib

data = open('day4/day4.txt').read()

def part1():
    i = 1
    while not hashlib.md5(f"{data}{i}".encode()).hexdigest().startswith('00000'):
        i += 1
    return i

def part2():
    i = 1
    while not hashlib.md5(f"{data}{i}".encode()).hexdigest().startswith('000000'):
        i += 1
    return i

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')