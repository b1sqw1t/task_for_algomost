from django.db import models

class Profile(models.Model):
    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    first_name = models.CharField(verbose_name='Имя', max_length=64)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64)
    email = models.EmailField(verbose_name='Email', blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст')
    area_of_activity = models.CharField(verbose_name='Область деятельности', max_length=512, choices=[
        ('economy', 'Экономика',),
        ('medical', 'Медицина'),
        ('it', 'Информационные Технологии'),
        ('other', 'Другое')
    ])
    name_of_facebook = models.CharField(verbose_name='Имя в Facebook', max_length=512, blank=True, null=True)
    name_of_instagram = models.CharField(verbose_name='Имя в Instagram', max_length=512, blank=True, null=True)

    def __repr__(self):
        return '{} {}'.format(self.last_name, self.first_name)
