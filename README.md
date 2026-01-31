# 🎮 Guess the Number

A fun number guessing game powered by the GitHub Copilot SDK! GitHub Copilot picks a secret number between 1 and 100, and you try to guess it with helpful hints from Copilot.

## Features

- 🤖 Copilot picks the secret number (1-100)
- 🎯 5 attempts to guess the correct number
- 📈📉 Dynamic hints that get spicier as you run low on attempts!
- 🎭 Personality-driven responses - from friendly to hilariously savage
- 🎉 Epic victory celebrations when you win
- 🔄 Play again option after each game

## Prerequisites

- Python 3.8 or higher
- GitHub Copilot SDK access

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/guess-the-number.git
   cd guess-the-number
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install directly:
   ```bash
   pip install github-copilot-sdk
   ```

## Running the Game

Simply run the Python script:

```bash
python3 guess_the_number.py
```

## How to Play

1. Copilot will pick a secret number between 1 and 100
2. Enter your guess when prompted
3. Copilot will give you hints telling you if your guess is too high or too low
4. Try to guess the number within 5 attempts!
5. Watch the hints get spicier as your attempts run low 🌶️
6. Type `quit` at any time to exit the game

## Example Gameplay

```
==================================================
🎮 Welcome to Guess the Number!
==================================================

🤖 Copilot is thinking of a number between 1 and 100...
🤖 Copilot has picked a number!
You have 5 attempts to guess it.
Type 'quit' to exit the game.

Attempt 1/5 - Enter your guess: 34

🤖 Copilot: 34 is a bit too low! You'll need to aim higher to find the secret number. Keep going, you can do it—4 attempts left!

Attempt 2/5 - Enter your guess: 58

🤖 Copilot: 58 is still too low! You're getting warmer, but you need to guess higher. You have 3 attempts left—keep at it!

Attempt 3/5 - Enter your guess: 69

🤖 Copilot: 69? I see what you did there, but it's still too low! You'll need to aim higher if you want to win. Two attempts left—make 'em count!

Attempt 4/5 - Enter your guess: 85

🤖 Copilot: 85?! You are agonizingly close, but alas, still too low! This is your final stand—one solitary attempt remains to save your dignity. Go higher, darling, for the love of drama, GO HIGHER!

Attempt 5/5 - Enter your guess: 92

🤖 Copilot: 92?! Oh, you flew too close to the sun, darling, and now you're burnt to a crisp! You needed to go *lower*, but instead, you overshot it completely. Zero attempts left—a spectacular tragedy of errors!


😢 Game over! You've run out of attempts.
Copilot's secret number was 88.

🤖 Copilot: Oh, the tragedy! The agony! You had multiple chances, and you squandered them all like loose change in a wishing well. You didn't just lose; you lost with *flair*. But don't just sit there wallowing in your numerical shame—dust yourself off and try again! I promise not to laugh... much.

==================================================
Would you like to play again? (yes/no): 
```

## Requirements

This game requires the GitHub Copilot SDK to be installed and configured. The SDK is essential as Copilot acts as the game master, picking the secret number and providing hints.

## License

MIT License - feel free to use and modify!
