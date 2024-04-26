from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from borrowdetail.models import borrowdetails
from borrowdetail.serializers import borrowdetailSerializer
@csrf_exempt
def borrowdetailApi(request):

    if request.method == 'GET':
        borrowdetail = borrowdetails.objects.all()
        borrowdetail_serializer = borrowdetailSerializer(borrowdetail, many=True)
        return JsonResponse(borrowdetail_serializer.data, safe=False)
    elif request.method == 'POST':
        borrowdetail_data = JSONParser().parse(request)
        borrowdetail_serializer = borrowdetailSerializer(data=borrowdetail_data)
        if borrowdetail_serializer.is_valid():
            borrowdetail_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)
    

@csrf_exempt
def borrowdetail_detailApi(request, id):

    try:
        borrowdetail = borrowdetails.objects.get(id=id)
    except borrowdetails.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        borrowdetail_serializer = borrowdetailSerializer(borrowdetail)
        return JsonResponse(borrowdetail_serializer.data, safe=False)
    elif request.method == 'PUT':
        borrowdetail_data = JSONParser().parse(request)
        borrowdetail_serializer = borrowdetailSerializer(borrowdetail, data = borrowdetail_data)
        if borrowdetail_serializer.is_valid():
            borrowdetail_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        borrowdetail.delete()
        return JsonResponse("Delete success", safe = False)


