import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
TELEGRAM_GROUP_ID = os.getenv('TELEGRAM_GROUP_ID')

import httpx


def send_message_telegram_bot(error: str):
    httpx.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendmessage",
        json={
            "chat_id": -int(TELEGRAM_GROUP_ID),
            "text": error,
        },
        timeout=None
    )


send_message_telegram_bot('salom')
