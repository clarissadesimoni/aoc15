data = open('day8/day8.txt').read().split('\n')

def countChars1(string):
    i, code, memory = 0, 0, 0
    hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    while i < len(string):
        if string[i] == '\\':
            if string[i + 1] == 'x' and string[i + 2] in hexChars and string[i + 3] in hexChars:
                memory += 3
                i += 3
            else:
                memory += 1
                i += 1
        elif string[i] == '\"':
            code -= 1
        code += 1
        memory += 1
        i += 1
    return memory - code

def part1():
    return sum(map(lambda x: countChars1(x), data))

def countChars2(string):
    i, memory, encoded = 0, 0, 0
    hexChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    while i < len(string):
        if string[i] == '\\':
            if string[i + 1] == 'x' and string[i + 2] in hexChars and string[i + 3] in hexChars:
                memory += 3
                encoded += 4
                i += 3
            else:
                memory += 1
                encoded += 3
                i += 1
        elif string[i] == '\"':
            encoded += 2
        encoded += 1
        memory += 1
        i += 1
    return encoded - memory

def part2():
    return sum(map(lambda x: countChars2(x), data))

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')