import platform
import os
from math import inf as infinity


class Connect4:   
    """
    this class is An implementation of connect4 game with Alpha-Beta pruning AI Algorithm .
    """

    SYMBOLS = ('X','O')

    def __init__(self,board,lign,column):
        self.board = board
        self.lign = lign
        self.column = column

    def remove_element(self,col):
        """
        method remove element in a specific column
        :param col : the column where to remove
        """
        for i in range(self.lign-1,-1,-1):
            if self.board[i][col] == Connect4.SYMBOLS[0] or self.board[i][col] == Connect4.SYMBOLS[1]:
                self.board[i][col] = ' '
                break
    

    def insert_element(self,symbol,col):
        """
        method insert symbol in a specific column
        :param symbol: the symbol to insert
        :param col : the column where to insert  
        """
        for i in range(self.lign):
            if self.board[i][col] == ' ':
                self.board[i][col] = symbol
                break

    def is_full_column(self,col):
        """
        test is the column is full 
        :param board: current state of the board
        :param col: which column 
        :return :False if not full ,True if full
        """
        for i in range(self.lign):
            if self.board[i][col] == ' ':
                return False
        return True

    def show_board(self):
        """
        Print the board on console
        :param board: current state of the board
        """
        print("\n"+ "-----------------------------------------------")
        for i in range(self.lign-1,-1,-1):
            for j in range(self.column):
                print('| '+str(self.board[i][j])+' |', end="  ")
            print("\n" + "-----------------------------------------------")
        print("  0      1      2      3      4      5      6") 

    def end_check(self):
        """
        This function test if the board is full 
        :param board: the state of the current board
        :return: True if the board is full 
        """
        for i in range(self.lign):
            for j in range(self.column):
                if self.board[i][j] == ' ':
                    return True
        return False 

    def win_check(self,symbol):
        """
        This method tests if a someone wins.
        :param board: the state of the current board
        :param symbol: X or O 
        :return: 10 if X win , -10 if O win and 0 for draw 
        """
        # check win horizontally
        for c in range(self.column-3):
            for r in range(self.lign):
                if self.board[r][c] == symbol and self.board[r][c+1] == symbol and self.board[r][c+2] == symbol and self.board[r][c+3] == symbol:
                    if symbol == Connect4.SYMBOLS[0]:
                        return 10
                    if symbol == Connect4.SYMBOLS[1]:
                        return -10

        # check win vertically
        for r in range(self.lign-3):
            for c in range(self.column):
                if self.board[r][c] == symbol and self.board[r+1][c] == symbol and self.board[r+2][c] == symbol and self.board[r+3][c] == symbol:
                    if symbol == Connect4.SYMBOLS[0]:
                        return 10
                    if symbol == Connect4.SYMBOLS[1]:
                        return -10

        # check win diagonally
        for r in range(self.lign-3):
            for c in range(self.column-3):
                if self.board[r][c] == symbol and self.board[r+1][c+1] == symbol and self.board[r+2][c+2] == symbol and self.board[r+3][c+3] == symbol:
                    if symbol == Connect4.SYMBOLS[0]:
                        return 10
                    if symbol == Connect4.SYMBOLS[1]:
                        return -10  

        for r in range(self.lign):
            for c in range(self.column-3):
                if self.board[r][c] == symbol and self.board[r-1][c+1] == symbol and self.board[r-2][c+2] == symbol and self.board[r-3][c+3] == symbol:
                    if symbol == Connect4.SYMBOLS[0]:
                        return 10
                    if symbol == Connect4.SYMBOLS[1]:
                        return -10

        for r in range(self.lign-3):
            for c in range(self.column):
                if self.board[r][c] == symbol and self.board[r+1][c-1] == symbol and self.board[r+2][c-2] == symbol and self.board[r+3][c-3] == symbol:
                    if symbol == Connect4.SYMBOLS[0]:
                        return 10
                    if symbol == Connect4.SYMBOLS[1]:
                        return -10
        
        return 0


    def minimax(self,depth,isMax,alpha,beta,cpt) :
        """
        Consider all the possible ways the game can go and returns the best value for that move
        :param depth:depth of the tree 
        :param isMax: turn of the X or the O , True for X and False for O 
        :param alpha: is the best value that the maximizer currently can guarantee at that level or above
        :param beta: is the best value that the minimizer currently can guarantee at that level or above
        :param cpt:is the depth that will not exceed minimax method
        :return:
        """
        if depth == cpt:
                return 0

        if Connect4.win_check(self,Connect4.SYMBOLS[1]):
            return Connect4.win_check(self,Connect4.SYMBOLS[1])

        if Connect4.win_check(self,Connect4.SYMBOLS[0]):
            return Connect4.win_check(self,Connect4.SYMBOLS[0])
              

        if not Connect4.end_check(self) :
            return 0

        if (isMax) :    
            best = -infinity

            for j in range(self.column): 
                if not Connect4.is_full_column(self,j):
                    Connect4.insert_element(self,Connect4.SYMBOLS[0],j)
                    best_score = Connect4.minimax(self,depth+1,False,alpha,beta,cpt)
                    best = max( best_score,best)  
                    alpha = max(alpha, best_score)
                    Connect4.remove_element(self,j)
                    if beta <= alpha:
                        break                            
            return best

        else :
            best = infinity

            for j in range(self.column):     
                if not Connect4.is_full_column(self,j):
                    Connect4.insert_element(self,Connect4.SYMBOLS[1],j)
                    best_score = Connect4.minimax(self,depth+1,True,alpha,beta,cpt)
                    best = min(best_score,best)
                    beta = min(beta, best_score)
                    Connect4.remove_element(self,j)
                    if beta <= alpha:
                        break
            return best


    def find_best_move(self,symbol,cpt):
        """
        Check whether or not the current move is better than the best move we take the help of minimax method
        :param symbol: for which symbol to choose the best move
        :param cpt:is the depth that will not exceed minimax method
        :return :the best move (column)
        """
        best_move = -1
        if symbol == Connect4.SYMBOLS[1]:
            best_val = infinity
            for j in range(self.column): 
                if not Connect4.is_full_column(self,j):
                    Connect4.insert_element(self,Connect4.SYMBOLS[1],j)
                    move_val = Connect4.minimax(self,0,True,-infinity,infinity,cpt)
                    Connect4.remove_element(self,j)
                    if (move_val < best_val) :     
                        best_move = j
                        best_val = move_val
                            
        if  symbol == Connect4.SYMBOLS[0]:
            best_val = -infinity
            for j in range(self.column): 
                if not Connect4.is_full_column(self,j):
                    Connect4.insert_element(self,Connect4.SYMBOLS[0],j)
                    move_val = Connect4.minimax(self,0,False,-infinity,infinity,cpt)
                    Connect4.remove_element(self,j)
                    if (move_val > best_val) :     
                        best_move = j
                        best_val = move_val

        return best_move
    
    def clean():
        """
        Clears the console
        """
        os_name = platform.system().lower()
        if 'windows' in os_name:
            os.system('cls')
        else:
            os.system('clear')

    def player_turn(self,symbol):
        """
        The player plays choosing a valid move.
        :param symbol: palyer choice
        :return:
        """
        while 1:
            try:
                nb = int(input("Player " + str(symbol) +", please select a number:"))
            except KeyboardInterrupt:
                print("\nBye")
                exit()
            except ValueError:
                print("The input must be a number !!!")
                continue

            if nb < 7 and nb > -1 :
                if not Connect4.is_full_column(self,nb):
                    break
                else:
                    print("The column is full !!!")
                    continue
            else:
                print("The number must be between 0 and 6!!!")
                continue

        Connect4.insert_element(self,symbol,nb)
        Connect4.clean()
        Connect4.show_board(self)


    def robot_turn(self,symbol,cpt):
        """
        It calls the find_best_move method to define the best move for computer
        :param symbol: if player choose X ,robot takes O else robot takes X
        :param cpt: is the depth that will not exceed minimax method
        :return: the best move for robot 
        """
        nb = Connect4.find_best_move(self,symbol,cpt)
        Connect4.insert_element(self,symbol,nb)
        Connect4.clean()
        Connect4.show_board(self)


    def main(self):
        """
        main method that launch connect 4 game  
        """

        print("Welcome to the Connect 4 Game!")
        print("1:playing against computer")
        print("2:playing against another player")

        while 1:
            try:
                option_choice = int(input('Choose 1 or 2 : '))
            except KeyboardInterrupt:
                print("\nBye")
                exit()
            except ValueError:
                print("Input must be a number !!!")
                continue

            if not (option_choice == 1 or option_choice == 2):
                print("The number must be 1 or 2 !!!")
            else:
                break
        
        Connect4.clean()
        
        if option_choice == 1:
            print("starting with:")
            print("1:X")
            print("2:O")

            while True:
                try:
                    start_with_choice = int(input("choose one of the options:"))
                except KeyboardInterrupt:
                    print("\nBye")
                    exit()
                except ValueError:
                    print("Input must be a number !!!")
                    continue
                
                if not (start_with_choice == 1 or start_with_choice == 2):
                    print("The number must be 1 or 2 !!!")
                else:
                    break

        Connect4.clean()

        Connect4.show_board(self)

        print("Game just started ....")

        if option_choice == 1:
            cost=0
            if start_with_choice == 1:
                cpt = 1
                while Connect4.end_check(self) and  not((Connect4.win_check(self,Connect4.SYMBOLS[0]) or Connect4.win_check(self,Connect4.SYMBOLS[1]))):
                    cpt += 1    
                    if cpt % 2 == 0:
                        Connect4.player_turn(self,Connect4.SYMBOLS[0])
                    else:
                        cost=+10
                        Connect4.robot_turn(self,Connect4.SYMBOLS[1],cost)

                if not Connect4.end_check(self):
                        print("DRAW!!")
                else:
                    if cpt % 2 == 0:
                        print("The player win!!!")
                    else:
                        print("The robot win!!!")    
            else:
                cpt = 0
                while Connect4.end_check(self) and  not((Connect4.win_check(self,Connect4.SYMBOLS[0]) or Connect4.win_check(self,Connect4.SYMBOLS[1]))):
                    cpt += 1    
                    if cpt % 2 == 0:
                        Connect4.player_turn(self,Connect4.SYMBOLS[1])
                    else:
                        cost=+10
                        Connect4.robot_turn(self,Connect4.SYMBOLS[0],cost)

                if not Connect4.end_check(self):
                    print("DRAW!!")
                else:
                    if cpt % 2 == 0:
                        print("The player win!!!")
                    else:
                        print("The robot win!!!")
        else:
            cpt = 1 
            while  Connect4.end_check(self) and  not((Connect4.win_check(self,Connect4.SYMBOLS[0]) or Connect4.win_check(self,Connect4.SYMBOLS[1]))):
                cpt += 1    
                if cpt % 2 == 0:
                    Connect4.player_turn(self,Connect4.SYMBOLS[0])
                else:
                    Connect4.player_turn(self,Connect4.SYMBOLS[1])

                if not Connect4.end_check(self):
                    print("DRAW!!")
                else:
                    if cpt % 2 == 0:
                        print("The X player win!!!")
                    else:
                        print("The O player win!!!")

        
        