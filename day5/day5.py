data = open('day5/day5.txt').read().split('\n')

def listOccurrences(string, substring):
    count = []
    if substring in string:
        for i in range(len(string)):
            if string[i:].startswith(substring):
                count.append(i)
    return count

def contains3vowels(string):
    return sum(map(lambda x: string.count(x), ['a', 'e', 'i', 'o', 'u'])) >= 3

def containsDoubles(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for a in alphabet:
        if string.count(a + a) >= 1:
            return True
    return False

def containsNoNaughty(string):
    return all(c not in string for c in ['ab', 'cd', 'pq', 'xy'])

def isNice1(string):
    return contains3vowels(string) and containsDoubles(string) and containsNoNaughty(string)

def containsRepeatingCouple(string):
    found = False
    for i in range(len(string) - 1):
        occ = listOccurrences(string, string[i:i + 2])
        occ = list(filter(lambda o: (o - 1) not in occ, occ))
        found = len(occ) - 1 > 0
        if (found):
            break
    return found

def containsAlternatingLetter(string):
    found = False
    for i in range(len(string) - 2):
        found = string[i] == string[i + 2]
        if (found):
            break
    return found

def isNice2(string):
    return containsRepeatingCouple(string) and containsAlternatingLetter(string)

def part1():
    return len(list(filter(lambda l: isNice1(l), data)))

def part2():
    return len(list(filter(lambda l: isNice2(l), data)))

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
