import numpy as np
import random
import json
from collections import defaultdict

# Q-table ve hiperparametreler
q_table = defaultdict(lambda: np.zeros(9))  
alpha = 0.1  
gamma = 0.9  
epsilon = 0.1  
num_games = 10000000

def reset_board():
    return ["b", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def find_winner(board):
    winner_pos = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for x in winner_pos:
        if board[x[0]] == "O" and board[x[1]] == "O" and board[x[2]] == "O":
            return "O"
        if board[x[0]] == "X" and board[x[1]] == "X" and board[x[2]] == "X":
            return "X"
    if " " not in board:
        return "draw"
    return None  

def find_empty_loc(board):
    return [i for i in range(1, 10) if board[i] == " "]  

def choose_action(state, epsilon):
    empty_locs = find_empty_loc(state)  
    if not empty_locs:
        return None  

    if random.uniform(0, 1) < epsilon:
        return random.choice(empty_locs)  
    else:
        q_values = q_table["".join(state)]
        best_action = np.argmax(q_values) + 1  
        return best_action if best_action in empty_locs else random.choice(empty_locs)

def update_q_table(state, action, reward, new_state):
    state_str = "".join(state)  
    new_state_str = "".join(new_state)

    best_next_action = np.max(q_table[new_state_str])  
    q_table[state_str][action - 1] += alpha * (reward + gamma * best_next_action - q_table[state_str][action - 1])

def game():
    board = reset_board()
    move_log = []  
    winner = None

    while True:
        x_move = random.choice(find_empty_loc(board))
        board[x_move] = "X"
        if find_winner(board) == "X":
            winner = "X"
            break

        empty_locs = find_empty_loc(board)
        if empty_locs:  
            state_before_move = board.copy()  
            action = choose_action(board, epsilon)
            if action and action in empty_locs:  
                board[action] = "O"  
                move_log.append(("".join(state_before_move), action))  
        
        winner = find_winner(board)
        if winner:
            break

    reward = 0
    if winner == "O":
        reward = 10
    elif winner == "X":
        reward = -10
    elif winner == "draw":
        reward = 2

    for state, action in move_log:
        update_q_table(list(state), action, reward, board)

    return move_log, reward

all_moves = []
for i in range(num_games):
    moves, final_reward = game()
    for state, action in moves:
        all_moves.append([state, action, final_reward])  

    if i % (num_games // 10) == 0:
        print(f"%{(i / num_games) * 100} tamamlandı...")

move_dict = defaultdict(int)

for board, mv, point in all_moves:
    move_dict[(board, mv)] += point  

# Sonuçları sıralama

aggregated_results = sorted(
    [[list(board), int(move), int(total_points)] for (board, move), total_points in move_dict.items()], 
    key=lambda x: x[2],  # **Sadece puana göre sıralıyoruz!**
    reverse=True  
)

if num_games >= 1000000:
    div = 1000000
    mark = "M"
else:
    div = 1000
    mark = "K"

games = int(num_games / div)
# JSON olarak kaydetmeden önce int64'leri normal int'e dönüştürelim
with open(f"trained_O_{games}{mark}_Q1_game.json", "w") as json_file:
    json.dump(aggregated_results, json_file, separators=(",", ":"))

print("Eğitim tamamlandı ve model kaydedildi.")
