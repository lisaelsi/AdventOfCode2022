with open('input/day06input.txt') as f:
    lines = f.readlines()

characters = lines[0]

# PART 1
for i in range(1, len(characters)):
    four = characters[i:i+4]
    if(len(set(four)) == 4):
        print('First positions of start-of-message markers (4 distinct characters): {}'.format(4+i))
        break


# PART 2
for i in range(1, len(characters)):
    fourteen = characters[i:i+14]
    if(len(set(fourteen)) == 14):
        print('first positions of start-of-message markers (14 distinct characters): {}'.format(14+i))
        break


