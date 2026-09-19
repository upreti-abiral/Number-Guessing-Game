# Number Guessing Game

A command-line Number Guessing Game built with Python.

## Overview

The computer randomly selects a number within a range, and the player tries to guess it.

After each valid guess, the program tells the player whether the guess is too high or too low. The game also counts the number of attempts.

There are three difficulty levels with different number ranges and attempt limits.

## Features

- Random number generation
- Three difficulty levels
- Different number ranges for each difficulty
- Attempt tracking
- Too high / too low hints
- Limited attempts on Medium and Hard
- Unlimited attempts on Easy
- Input validation
- Option to play again
- Option to quit during the game

## Difficulty Levels

| Level | Range | Attempts |
|---|---|---|
| Easy | 1 - 50 | Unlimited |
| Medium | 1 - 100 | 10 |
| Hard | 1 - 500 | 12 |

## How It Works

1. The player selects a difficulty level.
2. The program generates a random number within the selected range.
3. The player enters a guess.
4. The program checks whether the guess is valid.
5. The player receives a hint if the guess is too high or too low.
6. The number of attempts is tracked.
7. The game ends when the player guesses correctly or reaches the attempt limit.
8. The player can choose to play another round.

The game uses Python's `random` module to generate the secret number.

## Project Structure

number-guessing-game/
├── game.py
└── README.md

## Technologies Used

- Python
- `random`
- `sys`

## How to Run

Make sure Python 3 is installed.

Open the project folder in a terminal and run:

    python game.py

## Concepts Practised

- Functions
- `while` loops
- Conditional statements
- User input
- Input validation
- Random number generation
- Variables and data types
- Function return values
- Nested loops
- Program termination

## Possible Improvements

- Add a scoring system
- Save high scores
- Add a maximum and minimum range chosen by the player
- Add statistics across multiple rounds
- Add a graphical interface

These features are not currently implemented.

## Author

Abiral Upreti

A Python project focused on practising programming fundamentals, input handling, and game logic.
