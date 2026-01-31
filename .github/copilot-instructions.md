# Copilot Instructions for Guess the Number

## Project Overview
A number guessing game where **GitHub Copilot picks the secret number** and provides hints. This is NOT a random number generator game - Copilot is the "game master."

## Architecture

### Core Flow
1. `CopilotClient` → `create_session()` → `CopilotSession`
2. Session persists for the entire game to maintain context
3. All Copilot interactions use `session.send_and_wait({"prompt": ...})`
4. Response content accessed via `response.data.content`

### Key Functions
- `get_copilot_number(session)` - Asks Copilot to pick a number (extracts with regex for robustness)
- `get_copilot_response(session, prompt)` - Generic wrapper for Copilot prompts
- `play_game()` - Main async game loop with proper client/session lifecycle

## GitHub Copilot SDK Patterns

### Client Initialization (Required Pattern)
```python
from copilot import CopilotClient

client = CopilotClient({"auto_start": False})
await client.start()
session = await client.create_session()
# ... use session ...
await session.destroy()
await client.stop()
```

### Sending Messages
```python
response = await session.send_and_wait({"prompt": "Your prompt here"})
content = response.data.content  # The actual text response
```

### Response Parsing
Copilot responses may include extra text. Use regex extraction for structured data:
```python
match = re.search(r'\d+', response.data.content.strip())
```

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt
# or: pip install github-copilot-sdk

# Run the game
python3 guess_the_number.py
```

## Conventions

- **Async/await throughout** - All Copilot SDK calls are async
- **Session lifecycle** - Always destroy session and stop client in `finally` block
- **Input validation** - Validate user input before processing (0-100 range, numeric)
- **Graceful degradation** - Catch SDK initialization errors with helpful messages

## Testing the Game
The game is interactive. Test by running and playing through:
- Valid guesses (0-100)
- Invalid input (text, out-of-range numbers)
- Quit command
- Win/lose scenarios