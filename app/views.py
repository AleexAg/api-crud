from rest_framework.response import Response
from rest_framework.decorators import api_view
from app import serializers
# Create your views here.

# IMPORTS
from .models import Project
from .serializers import ProjectSerializer

#First view
@api_view(['GET'])
def getProject(request):
    project = Project.objects.all()
    serializers = ProjectSerializer(project, many=True)
    return Response(serializers.data)

@api_view(['POST'])
def postProject(request):
    data = request.data
    project = Project.objects.create(
        title = data['title'],
        description = data['description'],
        technology = data['technology'],
    )
    serializers = ProjectSerializer(project, many=False)
    return Response(serializers.data)


@api_view(['PUT'])
def putProject(request, id):
    data = request.data
    project = Project.objects.get(id=id)
    serializers = ProjectSerializer(instance=project, data=data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


@api_view(['DELETE'])
def delProject(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return Response(f'Projecto eliminado correctamente! id: {id}')
