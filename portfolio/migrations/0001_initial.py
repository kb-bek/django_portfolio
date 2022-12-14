# Generated by Django 4.1.2 on 2022-10-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Название')),
                ('description', models.CharField(db_index=True, max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='portfolio/images/', verbose_name='Изображение')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
