# Generated by Django 4.0.2 on 2022-04-13 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_alter_textbook_author_alter_textbook_booktitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
    ]
