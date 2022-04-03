from rest_framework.serializers import ModelSerializer
from Todoapp.models import *


class TodoSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'