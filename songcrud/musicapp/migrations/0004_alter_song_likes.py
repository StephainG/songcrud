# Generated by Django 4.1.2 on 2022-10-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_rename_lyrics_lyric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
