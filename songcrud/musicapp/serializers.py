from rest_framework import serializers
from .models import Artiste, Song, Lyric
from datetime import datetime

class ArtisteSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Artiste.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', validated_data.first_name)
        instance.last_name = validated_data.get('last_name', validated_data.last_name)
        instance.age = validated_data.get('age', validated_data.age)

class SongSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 50)
    date_released = serializers.DateTimeField(default=datetime.today)
    likes = serializers.IntegerField()
    

    def create(self, validated_data):
        return Song.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', validated_data.title)
        instance.date_released = validated_data.get('date_released', validated_data.date_released)
        instance.likes = validated_data.get('likes', validated_data.likes)
       

class LyricSerializer(serializers.Serializer):
    content = serializers.CharField(max_length = 8000)
    

    def create(self, validated_data):
        return Lyric.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', validated_data.content)
        