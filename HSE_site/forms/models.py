import datetime

from django.db import models


class Articles(models.Model):
    date = models.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    form = models.CharField('Форма заполнения', max_length=250)
    name = models.CharField('ФИО', max_length=250)#ФИО
    email = models.CharField('e-mail', max_length=250)#эл.почта
    departament = models.CharField('Департамент', max_length=250)#департамент
    data_incident = models.DateTimeField('Дата и время инцидента')#Дата инцидента
    locations = models.CharField('Буровая, цех, прочее', max_length=250)
    city = models.CharField('Город', max_length=250)
    company = models.CharField('Вы сотрудник', max_length=250)
    conditions = models.CharField('Опасные/Безопасные действия или условия?', max_length=250)
    stop_work = models.CharField('Была ли остановка работ', max_length=250)
    observation_in = models.CharField('Наблюдение в отношении', max_length=250)
    description = models.TextField('Опишите наблюдение')
    corrective = models.TextField('Корректирующие действия')
    category = models.CharField('Отметьте соответствующую категорию', max_length=250)
    control = models.CharField('Необходим ли контроль, со стороны ответственного?', max_length=250)
    victims = models.CharField('Есть ли пострадавшие при инциденте/происшествии?', max_length=250)
    incident_class = models.CharField('Классификация инцидента/происшествия', max_length=250)
    incident_class_fatal = models.CharField('Классификация инцидента', max_length=250)
    image1 = models.ImageField('Фото 1', upload_to='images/%Y-%m-%d/', blank=False)
    image2 = models.ImageField('Фото 2', upload_to='images/%Y-%m-%d/', blank=False)
    image3 = models.ImageField('Фото 3', upload_to='images/%Y-%m-%d/', blank=False)
    image4 = models.ImageField('Фото 4', upload_to='images/%Y-%m-%d/', blank=False)
    image5 = models.ImageField('Фото 5', upload_to='images/%Y-%m-%d/', blank=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Наблюдение'
        verbose_name_plural = 'Карты наблюдений'