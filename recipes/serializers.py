# Serializer is a way to convert a model type to a json
from rest_framework import serializers
from django.contrib.auth.models import User
from tag.models import Tag
from .models import Recipe

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['id', 'name', 'slug']

class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = ['id', 'title', 'description', 'author', 'public', 'category', 'preparation', 'tags', 'tag_objects', 'tag_links']
    
  public = serializers.BooleanField(
    source='is_published',
    read_only=True,
  )
  preparation = serializers.SerializerMethodField(
    method_name='any_method_name',
    read_only=True,
  )
  category = serializers.StringRelatedField(
    read_only=True,
  )
  tag_objects = TagSerializer(
    many=True,
    source='tags'
  )
  tag_links = serializers.HyperlinkedRelatedField(
    many=True,
    source='tags',
    queryset=Tag.objects.all(),
    view_name='recipes:recipes_api_v2_tag',
  )
  def any_method_name(self, recipe):
    return f'{recipe.preparation_time} {recipe.preparation_time_unit}'