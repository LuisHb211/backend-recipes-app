# Serializer is a way to convert a model type to a json
from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  title = serializers.CharField(max_length=65)
  description = serializers.CharField(max_length=165)
  public = serializers.BooleanField(source='is_published')
  #field that references a method, the method need 'get_' or use 'method_name=' in the SerializerMethodField
  preparation = serializers.SerializerMethodField()

  def get_preparation(self, recipe):
    return f'{recipe.preparation_time} {recipe.preparation_time_unit}'

