from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super


@api_view(['GET', 'POST'])
def supers_list(request):
    


    if request.method == "GET":
        super = Super.objects.all()
        serializer = SuperSerializer(super, many=True)    
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):

    super = get_object_or_404(super, pk=pk)

    if request.method == 'GET':

        super_type_name = request.query_params.get('super_type')
        print(super_type_name)

        queryset = Super.objects.all()
        serializer = SuperSerializer(super)


        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


