import random,sys
print('ROCK ,  PAPER , SCISSORS')
 # These variables keep track of the number of wins, losses, and ties.
wins = 0
losses=0
ties=0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties'%(wins,losses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        