from django.db import models

class Task(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    task = models.TextField('Описание')
    technology = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'