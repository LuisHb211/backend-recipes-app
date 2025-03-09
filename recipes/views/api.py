from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from ..models import Recipe
from ..serializers import RecipeSerializer

#Allow other types of request @api_view(http_method_names=['get','post'])
@api_view()
def recipe_api_list(request):
  # Gets the first 10 published recipes using the get_published method from the Recipe model. Serializes the obtained recipes to a format suitable for JSON response. Returns the serialized response as a DRF Response object
  recipes = Recipe.objects.get_published()[:10]
  serializer = RecipeSerializer(instance=recipes, many=True)
  return Response(serializer.data)

@api_view()
def recipe_api_detail(request, pk):
  recipe = get_object_or_404(
    Recipe.objects.get_published(),
    pk=pk
  )
  serializer = RecipeSerializer(instance=recipe, many=False)
  return Response(serializer.data)