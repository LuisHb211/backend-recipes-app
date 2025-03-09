from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tag.models import Tag

from ..models import Recipe
from ..serializers import RecipeSerializer, TagSerializer

#Allow other types of request @api_view(http_method_names=['get','post'])
@api_view()
def recipe_api_list(request):
  # Gets the first 10 published recipes using the get_published method from the Recipe model. Serializes the obtained recipes to a format suitable for JSON response. Returns the serialized response as a DRF Response object
  recipes = Recipe.objects.get_published()[:10]
  serializer = RecipeSerializer(
    instance=recipes, 
    many=True,
    context={'request':request}
    )
  return Response(serializer.data)

@api_view()
def recipe_api_detail(request, pk):
  recipe = get_object_or_404(
    Recipe.objects.get_published(),
    pk=pk
  )
  serializer = RecipeSerializer(
    instance=recipe, 
    many=False,
    context={'request':request},
)
  return Response(serializer.data)

@api_view()
def tag_api_detail(request, pk):
  tag = get_object_or_404(
    Tag.objects.all(),
    pk=pk
  )
  serializer = TagSerializer(
    instance=tag,
    many=False,
    context={'request':request}
  )
  return Response(serializer.data)