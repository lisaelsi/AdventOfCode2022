
''''

    [S] [C]         [Z]            
[F] [J] [P]         [T]     [N]    
[G] [H] [G] [Q]     [G]     [D]    
[V] [V] [D] [G] [F] [D]     [V]    
[R] [B] [F] [N] [N] [Q] [L] [S]    
[J] [M] [M] [P] [H] [V] [B] [B] [D]
[L] [P] [H] [D] [L] [F] [D] [J] [L]
[D] [T] [V] [M] [J] [N] [F] [M] [G]
 1   2   3   4   5   6   7   8   9 

'''


s1 = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
s2 = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
s3 = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
s4 = ['M', 'D', 'P', 'N', 'G', 'Q']
s5 = ['J', 'L', 'H', 'N', 'F']
s6 = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
s7 = ['F', 'D', 'B', 'L']
s8 = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
s9 = ['G', 'L', 'D']
stack_map = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7,
            8: s8, 9: s9}


with open('input/day05input.txt') as f:
    instructions = f.readlines()


instructions = instructions[10:]

for instruction in instructions:
    instruction = instruction.strip()
    instruction = instruction.split(' ')
    i = 0

    move = []
    while i < int(instruction[1]):
        move.append(stack_map[int(instruction[3])].pop())
        i += 1

    for item in range(len(move)):
        stack_map[int(instruction[5])].append(move.pop())

for i, a in stack_map.items():
    print(a[-1], end='')