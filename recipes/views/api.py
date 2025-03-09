from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


#para permitir outros tipos de request @api_view(http_method_names=['get','post'])
@api_view()
def recipe_api_list(request):
  return Response("ok")