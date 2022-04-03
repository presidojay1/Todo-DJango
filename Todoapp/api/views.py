from rest_framework.decorators import api_view
from rest_framework.response import Response
from Todoapp.models import *
from .serializers import *
from Todoapp.api import serializers
from Todoapp.forms import *
from django.http import JsonResponse
@api_view(['GET'])

def getTodos(request):
    todos = List.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['Post'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])


def updateTodo(request, id):
    Todo= List.objects.get(id=id)
    serializer = TodoSerializer(instance=Todo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
#     model_id = kwargs.get("id", None)
#     if not model_id:
#         return JsonResponse({"error": "method not allowed"})

#     try:
#         instance = List.objects.get(id=model_id)
#     except:
#         return JsonResponse({"error": "object not existing"})

#     serializer = TodoSerializer(data=request.data, instance=instance)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)

@api_view(['DELETE'])
def deleteTodo(request, id):
    List.objects.get(id=id).delete()
    return Response()