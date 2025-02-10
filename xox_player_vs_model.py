import random
import json
from collections import Counter
from collections import defaultdict
import sys

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
        e_board = find_empty_loc(board)
        with open(f"trained_O_{model}_game.json", "r") as json_file:
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

def player_move(board,team):
    try:
        loc = input("Enter a number 1-9 for the move")
        loc = int(loc)
        e_board = find_empty_loc(board)
        if loc in e_board:
            move(team,loc,board)
        else:
            print("The field you entered is full, enter another number")
            player_move(board,team)
    except:
        print("You made a mistake, try again")
        player_move(board,team)

def game(board):
    logical = True
    showboard(board)
    while logical:
        # Player Move
        player_move(board,"X")
        winner = find_winner(board)
        if winner == "X":
            showboard(board)
            logical = False
            break
        # PC Move
        pc_move(board,"O","10M_Q1")
        winner = find_winner(board)
        showboard(board)
        if winner == "O":
            logical = False
            break
        if " " not in board:
            logical = False
            break

    print(f"============= Winner : {winner} =============")
    new_game=input("Do you want to start a new game? y/n")
    if new_game=="y" or new_game=="Y":
        board = ["b"," "," "," "," "," "," "," "," "," "]
        game(board)
    else:
        pass

board = ["b"," "," "," "," "," "," "," "," "," "]
game(board)

