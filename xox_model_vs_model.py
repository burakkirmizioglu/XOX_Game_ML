import random
import json
from collections import Counter
from collections import defaultdict
import sys
import time

def showboard(board):
    print("/"*11)
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" ")
    print("-----------")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("-----------")
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ") 
    print("/"*11)

def move(team,loc,board):
    if board[loc]==" ":
        board[loc] = team        

def find_winner(board):
    winner_pos =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for x in winner_pos:
        if (board[x[0]]=="O" and board[x[1]]=="O" and board[x[2]]=="O"):
            winner = "O"
            return winner
        if (board[x[0]]=="X" and board[x[1]]=="X" and board[x[2]]=="X"):
            winner = "X"
            return winner
    if " " not in board:
        winner = "draw"
        return winner

def find_empty_loc(board):
    i=0
    board_empty = []
    for x in board:
        if x == " ":
            board_empty.append(i)
        i+=1
    return board_empty

def pc_move(board,team,model):
    try:
        if " " not in board:
            pass
        else:
            e_board = find_empty_loc(board)
            with open(f"trained_{team}_{model}_game.json", "r") as json_file:
                data = json.load(json_file)
                for tboard, mv, _ in data:
                    if board == tboard:
                        pc_move = mv
                        break
                if pc_move in e_board:
                    move(team,pc_move,board)
                else:
                    print("PC move failed")
    except Exception as e:
        print(f"PC move failed : {e}")
        time.sleep(30)
def game(board,model_x,model_o):
    logical = True
    while logical:
        if " " not in board:
            logical = False
            return "draw"
        # Player Move
        pc_move(board,"X",model_x)
        winner = find_winner(board)
        if winner == "X":
            logical = False
            return "X"
        # PC Move
        pc_move(board,"O",model_o)
        winner = find_winner(board)
        if winner == "O":
            logical = False
            return "O"

## match_scores ##
match_scores = []
game_count = 100
loading_counter = 0
i = 1
run = True
while run:
    board = ["b"," "," "," "," "," "," "," "," "," "]
    model_x = "1M_A1"
    model_o = "10M_Q1"
    ms = game(board,model_x,model_o)
    match_scores.append(ms)
    
    print_per_cycle = game_count//10
    if float( i / print_per_cycle) == int( i / print_per_cycle):
        rate = round((i/game_count),2)*100
        print(f"%{rate} completed...")
        
    i+=1
    if i>game_count:
        run = False

draw_score = 0
X_score = 0
O_score = 0
for sb in match_scores:
    if sb == "draw":
        draw_score+=1
    elif sb == "X":
        X_score+=1
    elif sb == "O":
        O_score+=1
    else:
        print("scoreboard error")

print(f"X: %{(X_score/game_count)*100} / O: %{(O_score/game_count)*100} / Draw: %{(draw_score/game_count)*100}")
