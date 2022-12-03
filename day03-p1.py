

# map priority of letters:
#   a-z: 1-26
#   A-Z: 1-26


# strip string
# split string in half 
# find letter that is in both strings
# find the priority of that letter
# sum for all strings 


with open('input/day03input.txt') as f:
    lines = f.readlines()

stripped = [s.strip() for s in lines]

sum = 0

for s in stripped:
    first, second = s[:len(s)//2], s[len(s)//2:]

    match = set(first).intersection(second)
    letter = match.pop()

    if letter.islower():
        sum = sum + (ord(letter)-96)
    else: 
        sum = sum + (ord(letter)-38)

print(sum)


# for lowercase letters ord('')-96
# for uppercase letters ord('')-38



