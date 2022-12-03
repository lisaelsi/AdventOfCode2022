
with open('input/day02input.txt') as f:
    lines = f.readlines()

stripped = [s.strip() for s in lines]

''''

1 for Rock, 2 for Paper, and 3 for Scissors
    plus the score for the outcome of the round 
0 if you lost, 3 if the round was a draw, and 6 if you won

A/X  ROCK
B/Y  PAPER
C/Z  SCISSORS

rock beats scissors 
scisscors beats paper
paper beats rock
                         
A X     1 + 3        3 + 0
B X     1 + 0        1 + 0
C X     1 + 6        2 + 0

A Y     2 + 6        1 + 3
B Y     2 + 3        2 + 3
C Y     2 + 0        3 + 3

A Z     3 + 0        2 + 6       
B Z     3 + 6        3 + 6
C Z     3 + 3        1 + 6 

'''


# PART 1

sum1 = 0
for i in stripped:
    if i == 'A X':
        sum1 = sum1 + 4
  
    elif i == 'B X':
        sum1 = sum1 + 1

    elif i == 'C X':
        sum1 = sum1 + 7

    elif i == 'A Y':
        sum1 = sum1 + 8

    elif i == 'B Y':
        sum1 = sum1 + 5

    elif i == 'C Y':
        sum1 = sum1 + 2

    elif i == 'A Z':
        sum1 = sum1 + 3

    elif i == 'B Z':
        sum1 = sum1 + 9

    elif i == 'C Z':
        sum1 = sum1 + 6

print('answer part 1: {}'.format(sum1))

# PART 2
sum2 = 0
for i in stripped:
    if i == 'A X':
        sum2 = sum2 + 3
  
    elif i == 'B X':
        sum2 = sum2 + 1

    elif i == 'C X':
        sum2 = sum2 + 2

    elif i == 'A Y':
        sum2 = sum2 + 4

    elif i == 'B Y':
        sum2 = sum2 + 5

    elif i == 'C Y':
        sum2 = sum2 + 6

    elif i == 'A Z':
        sum2 = sum2 + 8

    elif i == 'B Z':
        sum2 = sum2 + 9

    elif i == 'C Z':
        sum2 = sum2 + 7

print('answer part 2: {}'.format(sum2))

