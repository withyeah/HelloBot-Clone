# Generated by Django 3.2 on 2021-05-02 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20210502_0727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarot',
            name='card_image',
        ),
    ]
