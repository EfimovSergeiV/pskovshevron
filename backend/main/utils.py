from bot.bot import Bot
from django.conf import settings


bot = Bot(token=settings.MAILBOT_TOKKEN)


def send_alert_to_agent(msg):
    for contact in settings.MAILBOT_CONTACTS:
        bot.send_text(chat_id=contact, text=msg, parse_mode="HTML")