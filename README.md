Game Idea – What’s it all about?
This is a simple and fun number guessing game. First, you pick a difficulty level: Easy, Medium, or Hard. Then the game secretly generates a random number based on the level you chose. Your goal is to guess that number within a limited number of attempts.

To help you, there's a Hint button that gives you clues about the number, and a Restart button in case you want to start over.

How the App is Built
The app is divided into multiple files, each handling a specific part of the program:

build_layout.py – This is the main file that launches the app and manages the screens.

menu_screen.py – This file contains the logic for the menu screen, including what happens when you select a difficulty level.

number_guessing.py – This file holds all the game logic: checking guesses, tracking attempts, giving hints, and ending the game.

menu.kv – This is the design layout for the menu screen.

guess.kv – This is the design layout for the guessing screen where the game takes place.

First Screen: Menu
The menu screen lets you choose how hard the game should be. It includes three buttons:


Button	What it does
Easy	Sets the game to easy (number between 0–99).
Medium	Sets the game to medium (100–999).
Hard	Sets the game to hard (1000–9999).
Example:
If you click on "Medium", the game will generate a random number like 527, then take you to the guessing screen so you can start playing.

Second Screen: The Guessing Game
This is where the actual game takes place. Here's what each part of the screen does:


Component	Purpose

guess_input	A text field where you type your guess (e.g., 345).
submit_button	A button to submit your guess and check if it’s correct.
hint_button	A button that gives you a hint about the hidden number.
restart_button	A button that takes you back to the main menu and resets the game.
result_label	Displays feedback (too high, too low, correct, attempts left, etc.).
hint_label	Shows any hints you’ve received so far.
Example Gameplay
Let’s say you chose "Easy", and the game secretly picked the number 23.

Step 1: You type 30 and press Submit.

The game responds with:


Not correct, try again!
Attempts left: 3
High number!
Step 2: You press the Hint button.

It shows:


Hint: Total sum of all digits in the number is: 5
Step 3: You type 23 and press Submit again.

This time, you win! The message says:


Congratulation! You win the game from your 2 attempts.
What Happens When You Run Out of Attempts?
If you use up all your guesses (usually 4 tries) and still don’t get the number:

The submit and hint buttons become disabled.

You’ll see a message like:


You don't have any attempts left!
Game over!
The number is: 23
Restart Button
If you want to play again, just click the Restart button. It sends you back to the menu so you can choose a difficulty level and start fresh.








