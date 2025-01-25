from django.db import models


class ContactsModel(models.Model):
    phone = models.CharField(max_length=40, help_text="Пример: +7 (123) 123-12-12", verbose_name="Телефон", blank=True, null=True)
    wa = models.CharField(max_length=40, help_text="Пример: 71231231212", verbose_name="WhatsApp", blank=True, null=True)
    tg = models.CharField(max_length=40, help_text="Пример: nickname", verbose_name="Telegram", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", help_text="Пример: zakaz@pskovshevron.ru", blank=True, null=True)

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"

    def save(self, *args, **kwargs):
        if not self.pk and ContactsModel.objects.exists():
            raise ValueError("Вы можете создать только один объект настроек.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "Email, Тел., WhatsApp, Telegram"