import random
import json
from collections import Counter
from collections import defaultdict

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

def pc_move(board,team,move_log):
    board_ss = tuple(board)
    empty_board = find_empty_loc(board)
    if len(empty_board)>0:
        loc = random.choice(empty_board)
        log_temp = []
        log_temp.append(board_ss)
        log_temp.append(loc)
        move_log.append(log_temp)
        move(team,loc,board)

def game(board):
    logical = True
    move_log_X = []
    move_log_O = []
    while logical:
        #PC-1 Move
        pc_move(board,"X",move_log_X)
        winner = find_winner(board)
        if winner == "X":
            logical = False
            break
        #PC-2 Move
        pc_move(board,"O",move_log_O)
        winner = find_winner(board)
        if winner == "O":
            logical = False
            break
        if " " not in board:
            logical = False
            break

    # Give points to moves for "    X"
    if winner=="X":
        for m in move_log_X:
            c = Counter(m[0])
            point = (10 - c.get(" ", 0))
            m.append(point)
    if winner=="O":
        for m in move_log_X:
            c = Counter(m[0])
            point = -(10 - c.get(" ", 0))
            m.append(point)
    if winner=="draw":
        for m in move_log_X:
            c = Counter(m[0])
            point = (10 - c.get(" ", 0))/2
            m.append(point)
    
    return move_log_X

#### machine learning phase ####
## training ##
move_results = []
game_count = 15000
loading_counter = 0
i = 1
run = True
while run:
    board = ["b"," "," "," "," "," "," "," "," "," "]
    mr = game(board)
    move_results.extend(mr)

    print_per_cycle = game_count//10
    if float( i / print_per_cycle) == int( i / print_per_cycle):
        rate = round((i/game_count)*100,0)
        print(f"%{rate} completed...")
        
    i+=1
    if i>game_count:
        run = False

## summary of training data
move_dict = defaultdict(int)

for board, mv, point in move_results:
    move_dict[(tuple(board), mv)] += point

aggregated_results = [[list(board), move, total_points] for (board, move), total_points in move_dict.items()]
aggregated_results.sort(key=lambda x: x[2], reverse=True)


with open(f"trained_X_{game_count}_game.json", "w") as json_file:
    json.dump(aggregated_results, json_file, separators=(",", ":"))
print("Results saved to aggregated_results.json")
print(f"move_results : {len(move_results)}")
print(f"aggregated_results : {len(aggregated_results)}")







