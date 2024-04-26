from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.models import users
from users.serializers import usersSerializer


# @csrf_exempt
# def userApi(request):

#     if request.method == 'GET':
#         user = users.objects.all()
#         user_serializer = usersSerializer(user, many=True)
#         return JsonResponse(user_serializer.data, safe=False)
#     elif request.method == 'POST':
#         user_data = JSONParser().parse(request)
#         user_serializer = usersSerializer(data=user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("add success fully",safe=False) 
#         return JsonResponse("Fair to add", safe=False)

# @csrf_exempt
# def user_detailApi(request, id):
#     try:
#         user = users.objects.get(id=id)
#     except users.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         user_serializer = usersSerializer(user)
#         return JsonResponse(user_serializer.data, safe=False)
#     elif request.method == 'PUT':
#         user_data = JSONParser().parse(request)
#         # user = users.objects.get(id=user_data['id'])
#         user_serializer = usersSerializer(user, data = user_data)
#         if user_serializer.is_valid():
#             user_serializer.save()
#             return JsonResponse("Update success", safe=False)
#         return JsonResponse("Update failure", safe=False)
#     elif request.method == 'DELETE':
#         user.delete()
#         return JsonResponse("Delete success", safe = False)
    

class register(APIView):
    # def get(self,request):
    #      user = users.objects.all()
    #      user_serializer = usersSerializer(user, many=True)
    #      return JsonResponse(user_serializer.data, safe=False)
    def post(self, request):
        serializer = usersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = users.objects.get(username=request.data['username'])
            user.password(request.data['password'])
            user.save()
            # kiểm tra lại lỗi để lấy được token
            # token = MyJwt.createJtiToken(self,user=user)
            # return JsonResponse({'token': token.key, 'user': serializer.data})
        return JsonResponse(serializer.errors, status=status.HTTP_200_OK)