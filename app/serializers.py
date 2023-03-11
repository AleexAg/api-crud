from rest_framework.serializers import ModelSerializer
from .models import Project

#CODE
class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'   #Use all camps