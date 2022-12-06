with open('input/day06input.txt') as f:
    lines = f.readlines()


characters = lines[0]

# PART 2
for i in range(1, len(characters)):
    four = characters[i:i+4]
    if(len(set(four)) == 4):
        print(4+i)
        break


# PART 2
for i in range(1, len(characters)):
    fourteen = characters[i:i+14]
    if(len(set(fourteen)) == 14):
        print(14+i)
        break


