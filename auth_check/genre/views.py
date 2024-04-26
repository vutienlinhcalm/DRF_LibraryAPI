from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from genre.models import genres
from genre.serializers import genresSerializer

@csrf_exempt
def genreApi(request):

    if request.method == 'GET':
        genre = genres.objects.all()
        genre_serializer = genresSerializer(genre, many=True)
        return JsonResponse(genre_serializer.data, safe=False)
    elif request.method == 'POST':
        genre_data = JSONParser().parse(request)
        genre_serializer = genresSerializer(data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)

@csrf_exempt
def genre_detailApi(request, id):

    try:
        genre = genres.objects.get(id=id)
    except genres.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        genre_serializer = genresSerializer(genre)
        return JsonResponse(genre_serializer.data, safe=False)
    elif request.method == 'PUT':
        genre_data = JSONParser().parse(request)
        # genre = genres.objects.get(id=genre_data['id'])
        genre_serializer = genresSerializer(genre, data = genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse("Delete success", safe = False)