# Project Name: XOX Game - Machine Learning

**Version:** 1.0.0

## Description

This project involves the development of machine learning models to play the XOX (Tic-Tac-Toe) game. The models are trained using different reinforcement learning techniques to improve their gameplay strategies.
# Clone the repository
```js
git clone https://github.com/burakkirmizioglu/XOX_Game_ML.git
```
# Create a virtual environment (optional but recommended)
```js
python -m venv venv
```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install dependencies
numpy
```js
pip install numpy
```

## Files

### `basic_X_trainer`
This file contains the training code for the "X" player using a basic reinforcement learning method. Since "X" is the first player, a relatively simple method was sufficient. If you want to create a new "X" model, you can use this file. In this file, you can change how many games the model you will train will learn by playing with the "game_count" variable. You can change the reward and penalty system of the model by changing the point variables in the "Give points to moves for "X" " section.
```js
python basic_X_trainer.py
```

### `q_learning_O_trainer`
This file contains the training code for the "O" player using the Q-learning method. The "O" player required more defensive moves compared to the "X" player, hence the use of Q-learning was necessary. If you want to create a new "O" model, you can use this file. In this file, you can change how many games the model you will train will learn by playing with the "num_games" variable. You can change the reward and penalty system of the model by changing the "reward" variables in the scoring section.
```js
python q_learning_O_trainer.py
```

### `xox_model_vs_model`
This code is used to play the created models against each other and observe the results. In this file, you can change the number of games to be played between the two models with the "game_count" variable. You can change the models you will use with the "model_x" and "model_o" variables.
```js
python xox_model_vs_model.py
```

### `xox_player_vs_model`
This code allows a human player to play against the trained models. This code provides a terminal test environment without any visualizations. After running the code you will see an XOX board in the terminal. Each number entered between 1-9 will determine the move you will make.
The game board will look like this;
```js
///////////
   |   |   
-----------
   |   |   
-----------
   |   |   
///////////
```
The moves that the numbers represent are as follows;
```js
/////////// 
1 |  2  | 3 
-----------
4 |  5  | 6  
-----------
7 |  8  | 9
///////////
```
```js
python xox_player_vs_model.py
```

## Trained Models
# `trained_X_1M_A1_game`
This model was trained for the "X" player by playing 1 million games.

# `trained_O_10M_Q1_game`
This model was trained for the "O" player by playing 10 million games.

## Trained Old Models
These models were used during the development phase. Shared for information purposes. If you want, you can try moving the model to the main file path.
