import os
import time
import logging
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

BOT_TOKEN   = os.environ["BOT_TOKEN"]       # your bot token from BotFather
CHAT_ID     = int(os.environ.get("CHAT_ID", "0"))   # your group chat ID
MY_USER_ID  = int(os.environ.get("MY_USER_ID", "0")) # your personal Telegram user ID
DELAY       = 2
REACTION    = "🔥"

BASE = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    params = {"timeout": 30, "allowed_updates": ["message"]}
    if offset:
        params["offset"] = offset
    try:
        r = requests.get(f"{BASE}/getUpdates", params=params, timeout=35)
        return r.json().get("result", [])
    except Exception as e:
        logging.warning(f"getUpdates error: {e}")
        return []

def send_reaction(chat_id, message_id):
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": REACTION}]
    }
    try:
        r = requests.post(f"{BASE}/setMessageReaction", json=payload, timeout=10)
        data = r.json()
        if data.get("ok"):
            logging.info(f"Reacted 🔥 to message {message_id}")
        else:
            logging.warning(f"Reaction failed: {data}")
    except Exception as e:
        logging.warning(f"setMessageReaction error: {e}")

def main():
    logging.info("Bot started — watching for messages...")
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            msg = update.get("message")
            if not msg:
                continue
            chat_id    = msg["chat"]["id"]
            sender_id  = msg.get("from", {}).get("id")

            # Only react in the configured chat
            if CHAT_ID and chat_id != CHAT_ID:
                continue
            # Only react to your messages
            if MY_USER_ID and sender_id != MY_USER_ID:
                continue

            time.sleep(DELAY)
            send_reaction(chat_id, msg["message_id"])

if __name__ == "__main__":
    main()
