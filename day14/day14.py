import re

def distance(fly_rate, fly_time, rest_time, stop_time):
    d, r = divmod(stop_time, fly_time + rest_time)
    return d * fly_rate * fly_time + min(r, fly_time) * fly_rate

tok = re.compile(r'(?P<name>\w+) can fly (?P<fly_rate>\d+) km/s for (?P<fly_time>\d+) seconds, but then must rest for (?P<rest_time>\d+) seconds.')

def parse_line(line):
    m = tok.search(line)
    return m.group('name'), int(m.group('fly_rate')), int(m.group('fly_time')), int(m.group('rest_time'))

def day14_part1():
    print(max(distance(*parse_line(line)[1:], stop_time=2503) for line in open('day14/day14.txt')))

def day14_part2():
    deer = [parse_line(line) for line in open('day14/day14.txt')]
    points = {d[0]: 0 for d in deer}
    stop_time = 2503
    for t in range(1, stop_time+1):
        dists = [(distance(*d[1:], stop_time=t), d[0]) for d in deer]
        dists.sort()
        dists.reverse()
        m = dists[0][0]
        i = 0
        while i < len(dists) and dists[i][0] == m:
            points[dists[i][1]] += 1
            i += 1
    print(max(points.values()))

day14_part2()