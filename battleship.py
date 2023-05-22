from random import randint

Hidden_Pattern = [[' ']*8 for _ in range(8)]
Guess_Pattern = [[' ']*8 for _ in range(8)]

let_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print('  A B C D E F G H')
    print(' ┌─┬─┬─┬─┬─┬─┬─┬─┐')
    for row_num, row in enumerate(board, start=1):
        print(f'{row_num}│' + '│'.join(row) + '│')
        if row_num < 8:
            print(' ├─┼─┼─┼─┼─┼─┼─┼─┤')
    print(' └─┴─┴─┴─┴─┴─┴─┴─┘')

def get_ship_location():
    while True:
        guess = input('Enter a guess (e.g., B4): ').upper()
        if len(guess) == 2 and guess[0] in 'ABCDEFGH' and guess[1] in '12345678':
            return int(guess[1]) - 1, let_to_num[guess[0]]
        print('Please enter a valid guess.')

def create_ships(board):
    ship_sizes = [4, 2, 1, 1, 1]
    for size in ship_sizes:
        ship_placed = False
        while not ship_placed:
            direction = randint(0, 1)  # 0 for horizontal, 1 for vertical
            if direction == 0:  # horizontal placement
                ship_r = randint(0, 7)
                ship_cl = randint(0, 8 - size)
                for i in range(size):
                    if board[ship_r][ship_cl + i] != ' ':
                        break
                else:
                    for i in range(size):
                        board[ship_r][ship_cl + i] = '■'
                    ship_placed = True
            else:  # vertical placement
                ship_r = randint(0, 8 - size)
                ship_cl = randint(0, 7)
                for i in range(size):
                    if board[ship_r + i][ship_cl] != ' ':
                        break
                else:
                    for i in range(size):
                        board[ship_r + i][ship_cl] = '■'
                    ship_placed = True

def count_hit_ships(board):
    hit_count = 0
    for row in board:
        hit_count += row.count('■')
    return hit_count

def calculate_accuracy(guesses):
    total_guesses = 10
    hits = guesses.count('X')
    accuracy = (hits / total_guesses) * 100
    return accuracy

def play_again():
    answer = input('Do you want to play again? (yes/no): ').lower()
    return answer == 'yes'

def print_intro():
    print('-----------------------')
    print('|  The Battleship  |')
    print('-----------------------')
    print('  Guess the location of')
    print('  the hidden battleships')
    print('  using row and column')
    print('  coordinates (e.g., B4).')
    print('  You have 10 turns.')
    print('-----------------------')
    print('    BATTLE START      ')

def print_outro(accuracy):
    print('-----------------------')
    print('|     GAME OVER     |')
    print('-----------------------')
    print('    Accuracy: {:.2f}%'.format(accuracy))
    print('-----------------------')

print_intro()
while True:
    create_ships(Hidden_Pattern)
    turns = 10
    guesses = []
    while turns > 0:
        print_board(Guess_Pattern)
        guess = get_ship_location()

        if Guess_Pattern[guess[0]][guess[1]] == '-':
            print('You already guessed that.')
        elif Hidden_Pattern[guess[0]][guess[1]] == '■':
            print('Congratulations! You hit a battleship.')
            Guess_Pattern[guess[0]][guess[1]] = 'X'
            guesses.append('X')
            turns -= 1
        else:
            print('Sorry, you missed.')
            Guess_Pattern[guess[0]][guess[1]] = '-'
            guesses.append('-')
            turns -= 1

        print(f'You have {turns} turns remaining.')

    accuracy = calculate_accuracy(guesses)
    print_outro(accuracy)

    if not play_again():
        break
    else:
        Hidden_Pattern = [[' ']*8 for _ in range(8)]
        Guess_Pattern = [[' ']*8 for _ in range(8)]
        print_intro()
