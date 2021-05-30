import json

data = json.load(open('day12/day12.txt'))
nums1 = []
nums2 = []

def getNums1(obj):
    global nums1
    if isinstance(obj, dict):
        obj = list(obj.values())
    if isinstance(obj, list):
        for o in obj:
            getNums1(o)
    elif isinstance(obj, int):
        nums1.append(obj)

def getNums2(obj):
    global nums2
    if isinstance(obj, dict):
        if 'red' in obj.keys() or 'red' in obj.values():
            return
        obj = list(obj.values())
    if isinstance(obj, list):
        for o in obj:
            getNums2(o)
    elif isinstance(obj, int):
        nums2.append(obj)

def part1():
    getNums1(data)
    return str(sum(nums1))

def part2():
    getNums2(data)
    return str(sum(nums2))

print('Part 1: ' + part1())
print('Part 2: ' + part2())