# Generated by Django 3.2 on 2021-05-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='next_question',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tarot',
            name='card_number',
            field=models.IntegerField(unique=True),
        ),
    ]
