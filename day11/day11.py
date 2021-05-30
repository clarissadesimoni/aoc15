passwd = 'hepxcrrq'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def occurrences(string, sub):
    count, start = 0, string.find(sub)
    while start >= 0:
        count += 1
        start = string.find(sub, start + len(sub))
        if start >= len(string):
            break
    return count

def hasIOL(string):
    return any(c in string for c in 'iol')

def isOK(attempt):
    if hasIOL(attempt):
        return False
    if not any(c in attempt for c in [alphabet[i:i + 3] for i in range(len(alphabet) - 2)]):
        return False
    if sum([occurrences(attempt, c + c) for c in alphabet]) >= 2:
        return True
    else:
        return False

def increment(curr):
    last = alphabet[(alphabet.index(curr[-1]) + 1) % 26]
    if last in 'iol':
        last = alphabet[alphabet.index(last) + 1]
    res = (increment(curr[:-1]) if last == 'a' else curr[:-1]) + last
    if hasIOL(res):
        first = sorted(list(filter(lambda i: i[1] >= 0, {k:res.find(k) for k in 'iol'}.items())), key=lambda e: e[1])[0]
        res = res[:first[1]] + alphabet[alphabet.index(first[0]) + 1] + ('a' * (len(res) - first[1] - 1))
    return res

def part1():
    passwd = 'hepxcrrq'
    res = increment(passwd)
    while not isOK(res):
        res = increment(res)
    return res

def part2():
    passwd = 'hepxxyzz'
    res = increment(passwd)
    while not isOK(res):
        res = increment(res)
    return res

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')