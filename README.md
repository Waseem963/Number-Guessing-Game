# Number Guessing Game

A simple and fun number guessing game built with Python and Kivy.

---

## Overview

First, the player selects a difficulty level: Easy, Medium, or Hard.  
The game then secretly picks a random number based on the chosen difficulty.  
The player must guess the number within a limited number of attempts.

Players can request hints if they get stuck, or restart the game at any time.

---

## How the App is Structured

The app is divided into multiple files for clean organization:

| File Name         | Purpose |
|-------------------|---------|
| **build_layout.py** | Main file that initializes the app and manages screen switching. |
| **menu_screen.py** | Handles the logic for choosing the difficulty level. |
| **number_guessing.py** | Contains the core logic: checking guesses, giving hints, tracking attempts, and handling win/lose conditions. |
| **menu.kv** | Defines the visual layout of the menu screen. |
| **guess.kv** | Defines the visual layout of the guessing screen. |

---

## Gameplay

### First Screen: Menu

When the app starts, the player is presented with a menu containing three difficulty options:

| Difficulty | Range |
|------------|-------|
| Easy       | Number between 0 and 99 |
| Medium     | Number between 100 and 999 |
| Hard       | Number between 1000 and 9999 |

After selecting a difficulty, the game picks a random number and moves to the guessing screen.

---

### Second Screen: Guessing Game

On the guessing screen, players can:

| Component       | Description |
|-----------------|-------------|
| **guess_input**  | A text box where the player types their guess (for example, 345). |
| **submit_button** | Submit the guess and check if it's correct. |
| **hint_button**  | Request a clue about the secret number. |
| **restart_button** | Restart the game and return to the menu screen. |
| **result_label** | Displays feedback ("too high", "too low", "correct") and remaining attempts. |
| **hint_label** | Shows the hints received so far. |

---

## Example Gameplay

1. The player chooses Medium difficulty.  
2. The game randomly selects the number 527.  
3. The player guesses 600 and clicks Submit.  
   The game responds:  
   "Not correct, try again! Attempts left: 3. High number!"
4. The player clicks the Hint button.  
   A hint appears: "The sum of all digits is 14."
5. The player guesses 527 and wins the game!

---

## Game Over

If the player uses all available attempts without guessing correctly:
- The Submit and Hint buttons are disabled.
- A message appears saying:
You don't have any attempts left! Game over! The number was: [secret number].


---

## Restarting

At any time, the player can click the Restart button to:
- Reset the game state.
- Return to the menu.
- Start a new round by selecting a difficulty again.

---

## Requirements

- Python 3.x
- Kivy

Install Kivy using pip:

pip install kivy


---

## How to Run the Game
Simply run the build_layout.py file:

python build_layout.py




