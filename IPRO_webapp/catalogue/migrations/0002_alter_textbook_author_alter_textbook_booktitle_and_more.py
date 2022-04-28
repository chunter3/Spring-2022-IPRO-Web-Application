# Generated by Django 4.0.2 on 2022-02-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbook',
            name='author',
            field=models.CharField(max_length=30, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='booktitle',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='textbook',
            name='isbn',
            field=models.CharField(max_length=13, verbose_name='ISBN'),
        ),
    ]