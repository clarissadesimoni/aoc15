data = open('day1/day1.txt').read()
print(f"Part 1: {data.count('(') - data.count(')')}")
floor = 0
for i, c in enumerate(data):
    if floor == -1:
        print('Part 2: ' + str(i))
        break
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1