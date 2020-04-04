from django.db import models
import random, string


class AppData(models.Model):
    name = models.CharField(max_length=128, null=False, verbose_name=u"Заголовок")

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=128, null=False, verbose_name=u"Название приложения")
    api_key = models.CharField(max_length=128, blank=True)
    data = models.ManyToManyField(AppData, blank=True)

    def create_new_api_key(self):
        self.api_key = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=12))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.create_new_api_key()
        super(Application, self).save(*args, **kwargs)
