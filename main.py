from Connect4 import Connect4

if __name__ == '__main__':
    board = [[' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' '],]

    connect4 = Connect4(board,6,7)
    connect4.main()