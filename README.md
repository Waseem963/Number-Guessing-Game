🎮 Game Idea – What’s it all about?
This is a simple and fun number guessing game. First, you pick a difficulty level: Easy, Medium, or Hard. Then the game secretly picks a random number based on the level you chose.
Your goal is to guess that number within a limited number of attempts.

To help you out, there's a 💡 Hint button that gives you clues, and a 🔁 Restart button if you want to start over.

🧱 How the App is Built
The app is split into multiple files, each handling something specific:

🧠 build_layout.py – The main file that runs the app and manages screen switching.

🧩 menu_screen.py – Handles the logic for choosing difficulty.

🧮 number_guessing.py – Contains the core game logic: checking guesses, hints, attempts, win/lose logic.

🎨 menu.kv – The visual design for the menu screen.

🎨 guess.kv – The visual design for the guessing screen where you play the game.

🖥️ First Screen: Menu
When the game starts, you’ll see a menu with 3 buttons:


🔘 Button	🧾 What it does
🟢 Easy	Sets the game to easy mode (number 0–99).
🟡 Medium	Sets the game to medium mode (number 100–999).
🔴 Hard	Sets the game to hard mode (number 1000–9999).
💡 Example:
If you click Medium:

The game randomly picks a number, let’s say 527.

Then it takes you to the guessing screen so you can start playing.

🎯 Second Screen: The Guessing Game
This is where you play the actual game. Here's what each element on the screen does:


🧩 Component	🛠️ Purpose
✍️ guess_input	A text box where you type your guess (e.g., 345).
✅ submit_button	Click to submit your guess and check if it’s right or wrong.
💡 hint_button	Click to get a hint about the number.
🔁 restart_button	Resets the game and takes you back to the menu.
📢 result_label	Shows feedback like “too high,” “too low,” or “correct,” plus attempts.
🧾 hint_label	Displays the hints you've received so far.
🕹️ Example Gameplay
Let’s say you picked Easy, and the secret number is 23.

Step 1: You type 30 and hit Submit.

The game says:

Not correct, try again!
Attempts left: 3
High number!
Step 2: You click the Hint button.

It gives you something like:


Hint: Total sum of all digits in the number is: 5
Step 3: You try again with 23, and click Submit.

This time, you win!

Congratulation! You win the game from your 2 attempts.
🛑 What If You Run Out of Attempts?
If you use all your guesses (usually 4) without guessing correctly:

The Submit and Hint buttons get disabled.

You’ll see a message like:

You don't have any attempts left!
Game over!
The number is: 23
🔁 Restart Button
Want to try again? Just click Restart, and the app will take you back to the menu screen. You can pick a new difficulty level and play a new round.

