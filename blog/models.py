from django.db import models

class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        blank=True,
        db_index=True,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Текст'
    )


    date = models.DateTimeField(
        verbose_name='Дата'
    )



    def __str__(self):
        return self.title