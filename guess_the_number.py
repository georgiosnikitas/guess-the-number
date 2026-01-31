"""
Guess the Number Game using GitHub Copilot SDK

GitHub Copilot picks a secret number between 1 and 100,
and the user tries to guess it with hints from Copilot.
"""

import asyncio
import random
import re
from copilot import CopilotClient


async def get_copilot_number(session):
    """Ask Copilot to pick a secret number."""
    response = await session.send_and_wait({
        "prompt": "Pick a secret number between 1 and 100 (inclusive) for a guessing game. Reply with ONLY the number, nothing else."
    })
    number_str = response.data.content.strip()
    # Extract just the number in case there's extra text
    match = re.search(r'\d+', number_str)
    if match:
        return int(match.group())
    return int(number_str)


async def get_copilot_response(session, prompt):
    """Get a response from Copilot."""
    response = await session.send_and_wait({"prompt": prompt})
    return response.data.content


async def play_game():
    """Main game loop for guessing the number."""
    attempts = 0
    max_attempts = 5
    
    print("=" * 50)
    print("🎮 Welcome to Guess the Number!")
    print("=" * 50)
    print("\n🤖 Copilot is thinking of a number between 1 and 100...")
    
    # Initialize the Copilot client
    try:
        client = CopilotClient({"auto_start": False})
        await client.start()
        session = await client.create_session()
    except Exception as e:
        print(f"❌ Error: Copilot SDK not available ({e})")
        print("This game requires the GitHub Copilot SDK to run.")
        return
    
    try:
        # Have Copilot pick the secret number
        secret_number = await get_copilot_number(session)
        print("🤖 Copilot has picked a number!")
        print(f"You have {max_attempts} attempts to guess it.")
        print("Type 'quit' to exit the game.\n")
    
        while attempts < max_attempts:
            # Get user input
            user_input = (await asyncio.to_thread(input, f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")).strip()
            
            if user_input.lower() == 'quit':
                print(f"\n👋 Thanks for playing! Copilot's secret number was {secret_number}.")
                return
            
            # Validate input
            try:
                guess = int(user_input)
            except ValueError:
                print("❌ Please enter a valid number between 1 and 100.\n")
                continue
            
            if guess < 1 or guess > 100:
                print("❌ Please enter a number between 1 and 100.\n")
                continue
            
            attempts += 1
            remaining = max_attempts - attempts
            
            # Determine the tone based on remaining attempts
            if remaining >= 3:
                tone = "Be friendly and encouraging."
            elif remaining == 2:
                tone = "Be a bit cheeky and playful. Add some light teasing."
            elif remaining == 1:
                tone = "Be dramatically urgent and spicy! Add dramatic flair and witty sarcasm. Make it funny but pressuring."
            else:
                tone = "Be hilariously savage but still helpful. Maximum sass and drama!"
            
            # Check the guess with Copilot
            if guess == secret_number:
                celebrations = [
                    "Give them an epic, over-the-top congratulatory message with dramatic flair!",
                    "Be hilariously impressed and shower them with ridiculous praise!",
                    "React like they just won the lottery - maximum excitement and humor!"
                ]
                import random
                celebration_style = random.choice(celebrations)
                message = await get_copilot_response(
                    session,
                    f"The user correctly guessed your secret number {secret_number} in {attempts} attempts out of {max_attempts}! {celebration_style}"
                )
                print(f"\n🤖 Copilot: {message}\n")
                return
            
            direction = "higher" if guess < secret_number else "lower"
            message = await get_copilot_response(
                session,
                f"In our number guessing game, your secret number is {secret_number}. The user guessed {guess}, which is too {'low' if guess < secret_number else 'high'}. They have {remaining} attempts left. Give a brief hint telling them to go {direction} without revealing the exact number. {tone}"
            )
            print(f"\n🤖 Copilot: {message}\n")
        
        # Out of attempts
        print("\n😢 Game over! You've run out of attempts.")
        print(f"Copilot's secret number was {secret_number}.")
        
        message = await get_copilot_response(
            session,
            "The user just lost the number guessing game after using all attempts. Be dramatically disappointed but hilarious about it. Roast them gently while encouraging them to try again. Maximum sass!"
        )
        print(f"\n🤖 Copilot: {message}")
    
    finally:
        await session.destroy()
        await client.stop()


async def main():
    """Entry point for the game."""
    while True:
        await play_game()
        print("\n" + "=" * 50)
        play_again = (await asyncio.to_thread(input, "Would you like to play again? (yes/no): ")).strip().lower()
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        print()


if __name__ == "__main__":
    asyncio.run(main())
