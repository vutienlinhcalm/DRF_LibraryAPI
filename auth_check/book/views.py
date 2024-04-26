from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from book.models import books
from book.serializers import booksSerializer

@csrf_exempt
def bookApi(request):

    if request.method == 'GET':
        book = books.objects.all()
        book_serializer = booksSerializer(book, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
        book_serializer = booksSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)
    
@csrf_exempt
def book_detailApi(request, id):

    try:
        book = books.objects.get(id=id)
    except books.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        book_serializer = booksSerializer(book)
        return JsonResponse(book_serializer.data )
    elif request.method == 'PUT':
        book_data = JSONParser().parse(request)
        # book = books.objects.get(id=id)
        book_serializer = booksSerializer(book, data = book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        # book = books.objects.get(id=id)
        book.delete()
        return JsonResponse("Delete success", safe = False)
