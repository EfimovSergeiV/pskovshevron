from django.db import models
from django_resized import ResizedImageField


class ProductModel(models.Model):
    """ Модель товара """

    activated = models.BooleanField(verbose_name='Показывать на сайте', default=True)
    title = models.CharField(verbose_name='Название товара', max_length=250)
    price = models.PositiveIntegerField(verbose_name='Стоимость', default=0)
    description = models.TextField(verbose_name="Описание товара", max_length=5000)

    last_update = models.DateTimeField(verbose_name="Последнее обновление", auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-last_update',]

    def __str__(self) -> str:
        return str(self.title)
    

class ImageProductModel(models.Model):
    """ Модель изображения товара """

    image = ResizedImageField(
        size = [800, 800],
        verbose_name="",
        crop = ['middle', 'center'],
        upload_to='product/images/',
        help_text="Изображение товара",
        quality=100,
        default='product/images/default.webp',
        force_format='WEBP',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения товара'

    product = models.ForeignKey(ProductModel, related_name="product_images", verbose_name="Изображение", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Изображение'
    

class ProductPropertyModel(models.Model):
    """ Модель свойств товара """

    name = models.CharField(verbose_name='Название свойства', max_length=250, null=True, blank=True)
    value = models.CharField(verbose_name='Значение свойства', max_length=200)
    product = models.ForeignKey(ProductModel, related_name="product_properties", verbose_name="Свойство", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Свойство товара'
        verbose_name_plural = 'Свойства товара'

    def __str__(self) -> str:
        return f'{ self.name }: { self.value }'
    


class OrderModel(models.Model):
    """ Модель заказа товара """

    client_name = models.CharField(verbose_name='Клиент', max_length=300)
    contact_data = models.CharField(verbose_name='Контакты клиента', max_length=300)
    comment = models.TextField(verbose_name='Комментарий к заказу', max_length=1000)

    image = models.ImageField(verbose_name='Изображение',upload_to='order/images/', help_text='Если кастомный заказ', null=True, blank=True)
    products = models.JSONField(verbose_name='Заказанные товары', null=True, blank=True)

    created_data = models.DateTimeField(verbose_name="Дата создания", auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'Клиент: { self.client_name }'