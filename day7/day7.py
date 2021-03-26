import functools

commands = ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT']
data = open('day7/day7.txt').read().split('\n')
data = [d.split(' -> ') for d in data]
data = {d[1]:d[0] for d in data}
seen = {}

OPERATORS = {
    None: lambda arg: int(arg[0]) if arg[0].isdigit() else arg[0],
    "NOT": lambda arg: ~int(arg[1]),
    "AND": lambda arg: int(arg[0]) & int(arg[2]),
    "OR": lambda arg: int(arg[0]) | int(arg[2]),
    "LSHIFT": lambda arg: int(arg[0]) << int(arg[2]),
    "RSHIFT": lambda arg: int(arg[0]) >> int(arg[2]),
}

def get_wire(wire):
    try:
        return int(wire)
    except:
        pass
    cmd = data[wire].split(' ')
    if len(cmd) == 1 and cmd[0] in seen:
        seen[wire] = seen[cmd[0]]
    else:
        if len(cmd) == 1:
            seen[wire] = get_wire(OPERATORS[None](cmd))
        elif 'NOT' in cmd:
            cmd[1] = seen.get(cmd[1], get_wire(cmd[1]))
            seen[wire] = OPERATORS['NOT'](cmd)
        else:
            cmd[0] = seen[cmd[0]] if cmd[0] in seen else get_wire(cmd[0])
            cmd[2] = seen[cmd[2]] if cmd[2] in seen else get_wire(cmd[2])
            seen[wire] = OPERATORS[cmd[1]](cmd)
    return seen[wire]

p1 = get_wire('a')
seen = {}
data['b'] = str(p1)
p2 = get_wire('a')

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')