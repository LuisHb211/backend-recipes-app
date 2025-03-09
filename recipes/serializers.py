# Serializer is a way to convert a model type to a json
from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  title = serializers.CharField(max_length=65)
  description = serializers.CharField(max_length=165)

