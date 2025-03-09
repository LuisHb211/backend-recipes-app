# Serializer is a way to convert a model type to a json
from rest_framework import serializers
from django.contrib.auth.models import User
from tag.models import Tag

class TagSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=65)
  slug = serializers.SlugField()


class RecipeSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  title = serializers.CharField(max_length=65)
  description = serializers.CharField(max_length=165)
  public = serializers.BooleanField(source='is_published')
  #field that references a method, the method need 'get_' or use 'method_name=' in the SerializerMethodField
  preparation = serializers.SerializerMethodField()
  
  #There are many ways to use a related field, bellow there are some of them
  category = serializers.StringRelatedField()
  author = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all()
  )
  tags = serializers.PrimaryKeyRelatedField(
    queryset=Tag.objects.all,
    many=True
  )
  tag_objetcs = TagSerializer(
    many=True,
    source='tags'
  )
  
  #hyperlink related field
  tag_links = serializers.HyperlinkedRelatedField(
    many=True,
    source='tags',
    queryset=Tag.objects.all(),
    view_name='recipes:recipes_api_v2_tag',
  )
  def get_preparation(self, recipe):
    return f'{recipe.preparation_time} {recipe.preparation_time_unit}'



