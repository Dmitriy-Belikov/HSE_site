import datetime

from django.db import models


class News(models.Model):
    date = models.DateTimeField()
    label = models.CharField('Название новсти', max_length=250)
    description = models.TextField('Новость')
    image1 = models.ImageField('Фото 1', upload_to='images/news/%Y-%m-%d/', blank=True)
    image2 = models.ImageField('Фото 2', upload_to='images/news/%Y-%m-%d/', blank=True)
    
    def __str__(self):
        return self.label
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'