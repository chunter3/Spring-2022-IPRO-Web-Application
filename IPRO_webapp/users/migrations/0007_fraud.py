# Generated by Django 4.0.2 on 2022-03-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_wishlist_textbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fraud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('report', models.TextField()),
            ],
        ),
    ]