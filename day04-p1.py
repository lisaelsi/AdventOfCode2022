with open('input/day04input.txt') as f:
    lines = f.readlines()


stripped = [s.strip() for s in lines]

count = 0

for entry in stripped:
    pair1, pair2 = (entry.split(','))

    start1, end1 = pair1.split('-')
    start2, end2 = pair2.split('-')

    interval1 = list(range(int(start1), int(end1)+1))
    interval2 = list(range(int(start2), int(end2)+1))

    if all(x in interval1 for x in interval2) or all(x in interval2 for x in interval1):
        count += 1
    

print('Number of assignment pairs where one range fully contain the other: {}'.format(count))
