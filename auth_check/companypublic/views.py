from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from companypublic.models import companypublics
from companypublic.serializers import companypublicsSerializer
@csrf_exempt
def companypublicApi(request):

    if request.method == 'GET':
        companypublic = companypublics.objects.all()
        companypublic_serializer = companypublicsSerializer(companypublic, many=True)
        return JsonResponse(companypublic_serializer.data, safe=False)
    elif request.method == 'POST':
        companypublic_data = JSONParser().parse(request)
        companypublic_serializer = companypublicsSerializer(data=companypublic_data)
        if companypublic_serializer.is_valid():
            companypublic_serializer.save()
            return JsonResponse("add success fully",safe=False) 
        return JsonResponse("Fair to add", safe=False)
    

@csrf_exempt
def companypublic_detailApi(request, id):

    try:
        companypublic = companypublics.objects.get(id=id)
    except companypublics.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        companypublic_serializer = companypublicsSerializer(companypublic)
        return JsonResponse(companypublic_serializer.data, safe=False)
    elif request.method == 'PUT':
        companypublic_data = JSONParser().parse(request)
        companypublic_serializer = companypublicsSerializer(companypublic, data = companypublic_data)
        if companypublic_serializer.is_valid():
            companypublic_serializer.save()
            return JsonResponse("Update success", safe=False)
        return JsonResponse("Update failure", safe=False)
    elif request.method == 'DELETE':
        companypublic.delete()
        return JsonResponse("Delete success", safe = False)

