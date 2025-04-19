Game Idea (Summary):
This is a number guessing game. First, you choose a difficulty level (Easy, Medium, Hard), then you try to guess a random number within a limited number of attempts. You also have a hint button and a restart button.

App Structure:
The project is split into multiple files:

build_layout.py: The main file that runs the app.

menu_screen.py: Contains the level selection menu logic.

number_guessing.py: Contains the game logic and result checking.

menu.kv: The design of the menu screen.

guess.kv: The design of the guessing game screen.

First Screen: Menu (menu.kv + menu_screen.py)
It has 3 buttons:

Button	What it does
Easy	Sets the game to Easy level (number between 0 and 99).
Medium	Sets the game to Medium level (number between 100 and 999).
Hard	Sets the game to Hard level (number between 1000 and 9999).
Example:
If you click on "Medium":

The game will generate a random number, e.g., 527.

Then it switches to the game screen so you can start guessing.

Second Screen: Game Screen (guess.kv + number_guessing.py)
Buttons and Components:

Component	Purpose
 guess_input	Input field where you type your guess (e.g., 345).
 submit_button	Button to check your guess.
 hint_button	Button to get a hint about the number.
 restart_button	Button to restart the game.
 result_label	Shows the result (if guess is high, low, or correct, and remaining attempts).
 hint_label	Shows the hints you've received.
 Example Gameplay:
Scenario:
You chose "Easy", and the random number is 23 (you don't know that).

Step 1:
You type 30 in the input field and click Submit.

The program shows:

typescript
Copy
Edit
Not correct, try again!
Attempts left: 3
High number!
Step 2:
You click the Hint button.

It gives a hint like:

python
Copy
Edit
Hint: Total sum of all digits in the number is: 5
Step 3:
You type 23 and press Submit.

You win, and the message shows:

csharp
Copy
Edit
Congratulation! you win the game from your 2 attempts
 What happens if attempts are over?
If you fail to guess the number after all allowed attempts (usually 4):

The submit and hint buttons are disabled.

A message is shown like:

vbnet
Copy
Edit
You don't have any attempts left!
Game over!
The number is: 23
Restart Button:
If you click on it, it sends you back to the main menu so you can choose a new difficulty and start fresh.

