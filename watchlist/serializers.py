from rest_framework import serializers
from rest_framework.response import Response

from .models import WatchList

class WatchlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WatchList
        fields = ('id', 'tmdb_id', 'title', 'status', 'comment')

    def create(self, validated_data):
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance    