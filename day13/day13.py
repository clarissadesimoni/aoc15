from pprint import pprint
from itertools import permutations

initial = open('day13/day13.txt').read().split('\n')
initial = [line.split(' ') for line in initial]
extracted = [[line[0], line[-1][:-1], int(line[3]) * {'gain': 1, 'lose': -1}[line[2]]] for line in initial]

names = set([line[0] for line in extracted])

# for name in names:
#     tmp = list(filter(lambda x: name in x, extracted))
#     extracted = list(filter(lambda x: name not in x, extracted))
#     for i in range(len(tmp)):
#         tmp[i][:2] = sorted(tmp[i][:2])
#     tmp.sort(key=lambda x: (x[0], x[1]))
#     for i in range(len(tmp) // 2):
#         tmp[i][2] = tmp[i + 1][2] + tmp[i][2]
#         tmp.pop(i + 1)
#     data[name] = tmp

data = {name:{other:0 for other in list(filter(lambda n: n != name, names.union({'Clarissa'})))} for name in names.union({'Clarissa'})}
res = float('-inf')

for line in extracted:
    data[line[0]][line[1]] += line[2]
    data[line[1]][line[0]] += line[2]

for comb in list(permutations(names.union({'Clarissa'}))):
    res = max(res, sum([data[comb[j]][comb[(j + 1) % len(comb)]] for j in range(len(comb))]))

print(res)