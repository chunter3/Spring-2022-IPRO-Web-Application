# Generated by Django 4.0.2 on 2022-02-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktitle', models.CharField(max_length=20, verbose_name='Book Title')),
                ('author', models.CharField(max_length=20)),
                ('isbn', models.IntegerField()),
            ],
        ),
    ]
