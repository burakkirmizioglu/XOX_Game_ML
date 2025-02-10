# Project Name: XOX Game - Machine Learning

**Version:** 1.0.0

## Description

This project involves the development of machine learning models to play the XOX (Tic-Tac-Toe) game. The models are trained using different reinforcement learning techniques to improve their gameplay strategies.
# Clone the repository
"""git clone https://github.com/burakkirmizioglu/XOX_Game_ML.git"""
"""cd XOX_Game_ML"""
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
# Install dependencies
pip install -r requirements.txt

## Files

### `basic_X_trainer`
This file contains the training code for the "X" player using a basic reinforcement learning method. Since "X" is the first player, a relatively simple method was sufficient.
# Train the "X" player model (optional, if you want to train from scratch)
python basic_X_trainer.py

### `q_learning_O_trainer`
This file contains the training code for the "O" player using the Q-learning method. The "O" player required more defensive moves compared to the "X" player, hence the use of Q-learning was necessary.
# Train the "O" player model (optional, if you want to train from scratch)
python q_learning_O_trainer.py

### `xox_model_vs_model`
This code is used to play the created models against each other and observe the results.
# Evaluate the models by playing them against each other
python xox_model_vs_model.py

### `xox_player_vs_model`
This code allows a human player to play against the trained models.
# Play against the trained model as a human player
python xox_player_vs_model.py

## Trained Models

### `trained_X_1M_A1_game`
This model was trained for the "X" player by playing 1 million games.

### `trained_O_10M_Q1_game`
This model was trained for the "O" player by playing 10 million games.

