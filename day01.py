with open('input/day01input.txt') as f:
    lines = f.readlines()

sums = []
count = 0

lines.append('')

for line in lines:
    line = line.strip("'/\n")

    if line != '':
        line = int(line)
        count = count + line

    if not line:
        sums.append(count)
        count = 0    

print('max: {}'.format(sorted(sums)[-1]))
print("top three sum: {}".format(sum(sorted(sums)[-3:])))