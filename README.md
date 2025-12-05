# New California State Penal Code Discord Bot

This repository contains a Discord bot that sends the **New California State Penal Code (NCSPC)** as formatted messages when the slash command `/penalcode` is used.

---

## Files in this repository

| File | Description |
|------|-------------|
| `.env` | Stores your Discord bot token securely. |
| `.gitignore` | Ignores sensitive files like `.env`. |
| `NCSPC.txt` | The full New California State Penal Code text. |
| `bot.py` | Main Python bot script. |
| `requirements.txt` | Python dependencies for the bot. |

---

## Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/BlurzzUD/NCRP.git
cd NCRP
```

2. **Create a virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file**  
Create a `.env` file in the project root with your bot token:
```env
DISCORD_TOKEN=YOUR_BOT_TOKEN_HERE
```
Make sure `.env` is listed in `.gitignore` to keep your token private.

5. **Run the bot**  
```bash
python bot.py
```
Once the bot is online, it will respond to the slash command `/penalcode` in your Discord server.

---

## Notes

- The bot fetches `NCSPC.txt` and sends it as formatted Discord messages.  
- Titles (`TITLE I`, `TITLE II`, etc.) are **bolded**, and sections (`§101`, etc.) are displayed in **inline code**.  
- Long messages are automatically split to comply with Discord's 2000-character limit.  

---

## Requirements

All dependencies are listed in `requirements.txt`:
```
discord.py
python-dotenv
requests
```
Install them with:
```bash
pip install -r requirements.txt
```

