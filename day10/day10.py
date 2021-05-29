res = open('day10/day10.txt').read().strip()

# for t in range(40):
    # tmp = ''
    # currChar = res[0]
    # currCount = 1
    # for i, c in enumerate(res):
        # print(f'In the inner loop, index {i}')
        # if i == 0:
            # continue
        # if c == currChar:
            # currCount += 1
        # else:
            # tmp += f'{int(currCount)}{currChar}'
            # currChar = c
            # currCount = 1
        # print(tmp)
    # tmp += f'{int(currCount)}{currChar}'
    # res = tmp
    # print(res + '\n')

# print(res)

# 3113322113

from itertools import groupby

for i in range(50):
    res = ''.join([str(len(list(g))) + str(k) for k, g in groupby(res)])

print(len(res))
