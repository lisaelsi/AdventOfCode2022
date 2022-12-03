
with open('input/day03input.txt') as f:
    lines = f.readlines()

stripped = [s.strip() for s in lines]

group_list = list(zip(*(iter(stripped),) * 3))

sum = 0 

for group in group_list:
    match = set(group[0]) & set (group[1]) & set(group[2])

    letter = match.pop()

    if letter.islower():
        sum = sum + (ord(letter)-96)
    else: 
        sum = sum + (ord(letter)-38)

print(sum)

