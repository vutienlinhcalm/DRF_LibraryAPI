from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from borrow.models import borrows
from borrow.serializers import borrowSerializer

@csrf_exempt
def borrowApi(request):

    if request.method == 'GET':
        borrow = borrows.objects.all()
        borrow_serializer = borrowSerializer(borrow, many=True)
        return JsonResponse(borrow_serializer.data, safe=False)
    elif request.method == 'POST':
        borrow_data = JSONParser().parse(request)
        borrow_serializer = borrowSerializer(data=borrow_data)
        if borrow_serializer.is_valid():
            borrow_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)

@csrf_exempt
def borrow_detailApi(request, id):

    try:
        borrow = borrows.objects.get(id=id)
    except borrows.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        borrow_serializer = borrowSerializer(borrow)
        return JsonResponse(borrow_serializer.data, safe=False)
    elif request.method == 'PUT':
        borrow_data = JSONParser().parse(request)
        # borrow = borrow.objects.get(id=borrow_data['id'])
        borrow_serializer = borrowSerializer(borrow, data = borrow_data)
        if borrow_serializer.is_valid():
            borrow_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        borrow.delete()
        return JsonResponse("Delete success", safe = False)

