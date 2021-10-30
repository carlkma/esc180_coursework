# ESC180 Lab 6
# lab6_ttt.py
# Oct 15, 2021

# Done in collaboration by:
# Ma, Carl Ka To (macarl1) and
# Xu, Shen Xiao Zhu (xushenxi)


'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    print("\n\n")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# ------------------- PROBLEM 1---------------------------------------

def getCoord(square_num): # Problem 1a
    return [((square_num - 1) // 3), ((square_num - 1) % 3)]
    
def put_in_board(board, mark, square_num): # Problem 1b
    board[square_num[0]][square_num[1]] = mark


# ------------------- PROBLEM 2---------------------------------------
def get_free_squares(board): # Problem 2a
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                free_squares.append([i,j])
    return free_squares


def make_random_move(board, mark): # Problem 2b
    free_squares = get_free_squares(board)
    n = int(len(free_squares) * random.random())
    square_num = free_squares[n]
    board[square_num[0]][square_num[1]] = mark
    return (square_num[0])*3 + (square_num[1]+1)


# ------------------- PROBLEM 3---------------------------------------
def is_row_all_marks(board, row_i, mark): # Problem 3a
    if board[row_i] == [mark] * 3:
        return True
    else:
        return False

def is_col_all_marks(board, col_i, mark): # Problem 3b
    col = []
    for row in range(len(board)):
        col.append(board[row][col_i])
    if col == [mark] * 3:
        return True
    else:
        return False


def is_win(board, mark): # Problem 3c
    dia_win = board[0][0]==board[1][1]==board[2][2]==mark or board[0][2]==board[1][1]==board[2][0]==mark
    if dia_win:
        return True
    for i in range(3):
        if is_row_all_marks(board, i, mark) or is_col_all_marks(board, i, mark):
            return True
    return False
    
# ------------------- PROBLEM 4---------------------------------------

def make_improved_move(board, mark): # Problem 4a
    free_squares = get_free_squares(board)
    for square_num in free_squares:
    
        temp_board = [inner_list[:] for inner_list in board]
        temp_board[square_num[0]][square_num[1]] = mark
    
        if is_win(temp_board,mark):
            board[square_num[0]][square_num[1]] = mark
    
            return (square_num[0])*3 + (square_num[1]+1)
    return make_random_move(board, mark)

def minimax(board, to_max):
    # Here we follow our assumption that the player goes first
    # i.e. player's mark == "X"; computer's mark == "O"
    
    if is_win(board, "X") or board[0][0]==board[1][1]==board[2][2]=="X":
        return -10
    if is_win(board, "O")or board[0][0]==board[1][1]==board[2][2]=="O":
        return 10
    free_squares = get_free_squares(board)
    if len(free_squares)==0:
        return 0
    
    if to_max:
        
        best = -1000
        for square_num in free_squares:
            board[square_num[0]][square_num[1]] = "O"
            best = max(best, minimax(board, not to_max))
            board[square_num[0]][square_num[1]] = " "
        return best
    else:
        
        best = 1000
        for square_num in free_squares:
            
            board[square_num[0]][square_num[1]] = "X"
            best = min(best, minimax(board, not to_max))
            board[square_num[0]][square_num[1]] = " "
        return best
        
def make_minimax_move(board):
    best_value = -1000
    best_move = None
    free_squares = get_free_squares(board)
    for square_num in free_squares:
            
            board[square_num[0]][square_num[1]] = "O"
            minimax_value = minimax(board, False)
            board[square_num[0]][square_num[1]] = " "
            if minimax_value > best_value:
                best_move = square_num
                best_value = minimax_value
    board[best_move[0]][best_move[1]] = "O"
    print("The computer has made a move!")
        
    return (best_move[0])*3 + (best_move[1]+1)
        
        

# ----------------------------------------------------------


if __name__ == '__main__':
    tie = True
    board = make_empty_board()
    print_board_and_legend(board)    

    
    '''board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]'''
    
    print_board_and_legend(board)
    print(getCoord(6)) # Problem 1

    move = ""
    valid_moves = list(range(1,10))
    print(valid_moves)


    '''board = [["O", " ", "X"],
             [" ", "X", " "],
             ["O", " ", " "]]
    print(get_free_squares(board))'''

'''
    for i in range(9):
        
        while move not in valid_moves:
            move = int(input("Enter your move: "))
    
        valid_moves.remove(move)
        
        if i % 2 == 0:
            put_in_board(board,"X",getCoord(move))
        else:
            put_in_board(board,"O",getCoord(move))
            
        print_board_and_legend(board)'''

for i in range(9):
        
        if i % 2 == 0:
            while move not in valid_moves:
                move = int(input("Enter your move: "))
            valid_moves.remove(move)
            put_in_board(board,"X",getCoord(move))

            if is_win(board,"X"):
                print("X wins")
                tie = False
                    
                break
            
            
        else:
            #temp = make_improved_move(board, "O")
            temp = make_minimax_move(board)
            valid_moves.remove(temp)
            if is_win(board,"O"):
                print("O wins")
                tie = False
                break

        
            
            
        print_board_and_legend(board)

print_board_and_legend(board)
if tie:
    print("Tie!")



        


