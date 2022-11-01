from django.db import models

class Project(models.Model):

    title = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name="Название"
    )

    description = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name="Описание"
    )

    image = models.ImageField(
        upload_to='portfolio/images/',
        verbose_name='Изображение'
    )

    url = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.title


class Skill(models.Model):

    title = models.CharField(
        db_index=True,
        max_length=60,
        blank=True,
        verbose_name='Название'
    )

    score = models.IntegerField(
        db_index=True,
        blank=True,
        default=70
    )

    def __str__(self):
        return self.title


class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        verbose_name="Name", max_length=100
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    message = models.TextField(
        verbose_name="Message"
    )

    def __str__(self):
        return f'{self.name}'


class Certificate(models.Model):

    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Название'
    )

    date = models.DateTimeField(
        blank=True,
        null=True
    )

    name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Название курса"
    )

    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title




