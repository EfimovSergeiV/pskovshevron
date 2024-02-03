from django.core.management.base import BaseCommand, CommandError
from shop.models import ImageProductModel
from PIL import Image
from pathlib import Path

class Command(BaseCommand):
    args = ''
    help = ''
    
    def handle(self, *args, **options):
        pass

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent



qs = ImageProductModel.objects.all()

# Меняем размер изображений на 340x340
for i in qs:
    img_path = f'{BASE_DIR}{i.image.url}'
    img = Image.open(img_path)
    img = img.resize((340, 340))
    img.save(img_path, quality=90, optimize=True)
    print(f'Изображение {img_path} изменено')