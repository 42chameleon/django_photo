from rest_framework import serializers


class UploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
