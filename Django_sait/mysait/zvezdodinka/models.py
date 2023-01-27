from django.db import models

class Baza(models.Model):
    title = models.CharField('название', max_length=200, default='Новость')
    anons = models.CharField('Анонс', max_length=200, default='Новость')
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'