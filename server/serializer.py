from rest_framework import serializers
from .models import Server, Category, Channel


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = "__all__"

class ServerSerializer(serializers.ModelSerializer):
    channel_server = ChannelSerializer(many=True)

    class Meta:
        model = Server
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
