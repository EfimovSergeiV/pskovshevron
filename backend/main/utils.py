from bot.bot import Bot
from django.conf import settings


bot = Bot(token=settings.MAILBOT_TOKKEN)


def send_alert_to_agent(msg):
    bot.send_text(chat_id=settings.MAILBOT_CONTACTS, text=msg, parse_mode="HTML")