# 🎮 Guess the Number

A fun number guessing game powered by the GitHub Copilot SDK! GitHub Copilot picks a secret number between 1 and 100, and you try to guess it with helpful hints from Copilot.

## Features

- 🤖 Copilot picks the secret number (1-100)
- 🎯 5 attempts to guess the correct number
- 📈📉 "Too high" / "Too low" hints after each guess
- 🤖 AI-powered hints and messages from GitHub Copilot
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
4. Try to guess the number within 10 attempts!
5. Type `quit` at any time to exit the game

## Example Gameplay

```
==================================================
🎮 Welcome to Guess the Number!
==================================================

🤖 Copilot is thinking of a number between 1 and 100...
🤖 Copilot has picked a number!
You have 10 attempts to guess it.
Type 'quit' to exit the game.

Attempt 1/10 - Enter your guess: 50

🤖 Copilot: 50 is too high. Try guessing a lower number!

Attempt 2/10 - Enter your guess: 25

🤖 Copilot: 25 is too low. Try guessing a higher number!

Attempt 3/10 - Enter your guess: 37

🤖 Copilot: 37 is too high. Try guessing a lower number!

Attempt 4/10 - Enter your guess: 31

🤖 Copilot: 🎉 Congratulations! You guessed the secret number 31 correctly in 4 attempts!
```

## Requirements

This game requires the GitHub Copilot SDK to be installed and configured. The SDK is essential as Copilot acts as the game master, picking the secret number and providing hints.

## License

MIT License - feel free to use and modify!
