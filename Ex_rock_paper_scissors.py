import random, sys

print('ROCK, PAPER, SCISSORS')


wins = 0
losses = 0
ties = 0

while True: # main game loop
    print("%s Wins, %s Losses %s Ties" % (wins, losses, ties))
    while True: # input loop
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playermove = input()
        if playermove == 'q':
            sys.exit() # quit program
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break # Break out of the player input loop.
        if playermove != 'r' or playermove != 'p' or playermove != 's':
            print('INVALID OPTION!!!')
        print('Type one r, p, s, or q.')

    # Players choice
    if playermove == 'r':
        print('ROCK vs. ', end='')
    elif playermove == 'p':
        print('PAPER vs. ', end='')
    elif playermove == 's':
        print('SCISSORS vs. ', end='')

    # Random Computer Choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    if random_number == 2:
        computer_move = 'p'
        print('PAPER')
    if random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display & Record win / lose / ties
    if playermove == computer_move:
        print('It\'s a TIE!!!')
        ties = ties + 1
    elif playermove == 'r' and computer_move == 's':
        print("You WIN!!!")
        wins = wins + 1
    elif playermove == 's' and computer_move == 'p':
        print('You WIN!!!')
        wins = wins + 1
    elif playermove == 'p' and computer_move == 'r':
        print('You WIN!!!')
        wins = wins + 1
    elif playermove == 'r' and computer_move == 'p':
        print('You LOSE!!!')
        losses = losses + 1
    elif playermove == 'p' and computer_move == 's':
        print('You LOSE!!!')
        losses = losses + 1
    elif playermove == 's' and computer_move == 'r':
        print('You LOSE!!!')
        losses = losses + 1
