# Generated by Django 4.1.2 on 2022-10-26 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_song_artiste_id_lyrics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lyrics',
            new_name='Lyric',
        ),
    ]
