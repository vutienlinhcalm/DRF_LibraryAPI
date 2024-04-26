from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from author.models import authors
from author.serializers import authorsSerializer
@api_view(['GET', 'POST'])
def authorApi(request,format=None):
    
    if request.method == 'GET':
        author = authors.objects.all()
        author_serializer = authorsSerializer(author, many=True)
        return JsonResponse(author_serializer.data, safe=False)
    elif request.method == 'POST':
        author_data = JSONParser().parse(request)
        author_serializer = authorsSerializer(data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)

@api_view(['GET', 'PUT', 'DELETE'])
def authors_detailApi(request,id,format=None):
    try:
        author = authors.objects.get(id=id)
    except authors.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        author_serializer = authorsSerializer(author)
        return JsonResponse(author_serializer.data )
    elif request.method == 'PUT':
        author_data = JSONParser().parse(request)
        author_serializer = authorsSerializer(author, data = author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        # author = authors.objects.get(id=id)
        author.delete()
        return JsonResponse("Delete success", safe = False)