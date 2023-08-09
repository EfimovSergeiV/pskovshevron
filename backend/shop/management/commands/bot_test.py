from django.core.management.base import BaseCommand, CommandError
from main.utils import send_alert_to_agent


class Command(BaseCommand):
    args = ''
    help = ''
    
    def handle(self, *args, **options):
        pass

send_alert_to_agent("""Новый заказ https://api.pskovshevron.ru/admin/shop/ordermodel/""")