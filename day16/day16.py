import re

data = open('day16/day16.txt').read().split('\n')
sues = {}
for line in data:
	m = re.match(r"Sue (\d+): (.*)", line)
	if m:
		i = int(m.group(1))

		sue = {}
		remaining = m.group(2)
		toks = remaining.split(", ")
		for tok in toks:
			a, b = tok.split(": ")
			sue[a] = int(b)
		sues[i] = sue

solution_sue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# def parse_aunt(details):
#     res = {}
#     details = details.split(', ')
#     for detail in details:
#         tmp = detail.split(': ')
#         res[tmp[0]] = int(tmp[1])
#     return res

def is_she_the_one1(details):
    for detail, value in details.items():
        if solution_sue.get(detail, -1) != value:
            return False
    return True

def is_she_the_one2(details):
    for detail, value in details.items():
        if solution_sue.get(detail, -1) != value and detail not in ['cats', 'trees', 'pomeranians', 'goldfish']:
            return False
        elif solution_sue.get(detail, -1) < value and detail not in ['cats', 'trees']:
            return False
        elif solution_sue.get(detail, -1) > value and detail not in ['pomeranians', 'goldfish']:
            return False
    return True

def part1():
    return list(filter(lambda s: is_she_the_one1(sues[s]), sues))

def part2():
    return list(filter(lambda s: is_she_the_one2(sues[s]), sues))

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

#low: 213