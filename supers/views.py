from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):
    


    if request.method == "GET":
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def supers_detail(request, pk):

    try:
        supers = Super.objects.get(pk=pk)
        serializer = SuperSerializer(supers)

        return Response(serializer.data)
    except Super.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


