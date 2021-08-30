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
            print('%s Wins, %s Losses, %s Ties'%(wins,losses,ties))
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  #Break
        print('Type one of r, p, s, or q.')
    # Display what the player chose:
    if playerMove == 'r':
        print("Rock versus.....")
    elif playerMove == 'p':
        print("paper versus...")
    elif playerMove == 's':
        print('Scissors versus...')
    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if  randomNumber == 1:
        computerMove  = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove == 's'
        print('SCISSORS')
    #DISPLAY and Record the W/L/T:
    if playerMove == computerMove :
        ties+=1
    elif playerMove == 'r' and computerMove =='s':
        wins+=1
        print("You Won ...!!!")
    elif playerMove == 'p' and computerMove == 'r':
        wins+=1
        print("You Won ...!!!")
    elif playerMove == 's' and computerMove == 'p':
        wins+=1
        print("You Won ...!!!")
    elif computerMove == 'r' and playerMove == 's':
        losses+=1
        print("COM Won ...!!!")
    elif computerMove == 's' and playerMove == 'p':
        losses+=1
        print("COM Won ...")
    elif computerMove == 'p' and playerMove == 'r':
        print("COM Won ...")
        losses+=1

