# 🔥 Telegram Fire Reaction Bot

Automatically reacts with 🔥 to every message in your chat after 2 seconds.

---

## Deploy to Railway (free, 5 minutes)

### 1. Upload to GitHub
- Go to github.com → New repository → name it `fire-bot`
- Upload all 3 files: `bot.py`, `requirements.txt`, `Procfile`

### 2. Deploy on Railway
- Go to railway.app → sign in with GitHub
- Click **New Project** → **Deploy from GitHub repo** → select `fire-bot`
- Click **Add Variables** and add:

| Variable   | Value                        |
|------------|------------------------------|
| BOT_TOKEN  | your new token from BotFather |
| CHAT_ID    |                              |

- Click **Deploy** — done! ✅

### 3. Make sure the bot is admin in your chat
The bot needs to be added to the group and given **admin rights** so it can react to messages.

---

## How it works
- Listens for every new message in the chat
- Waits 2 seconds
- Sends a 🔥 reaction via Telegram's `setMessageReaction` API
