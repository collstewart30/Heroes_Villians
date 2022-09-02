from distutils.sysconfig import customize_compiler
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super


# custom dictionary response 
# “heroes” key set equal to a list of supers # of type “Hero” and a 
# “villains” key set equal to a list of supers # of type “Villain” 
# Custom_response = {“heroes” = [], “villains” = []



@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == "GET":

        super_type_name = request.query_params.get('type')        #changed to 'type' in 1:1

        queryset = Super.objects.all()


        if super_type_name:
            queryset = queryset.filter(super_type__type=super_type_name)

        else:
            super_types = SuperType.objects.all()

            super_type_dictionary = {} 

            for super_type in super_types:
                
                if super_type.id == 1:
                    heroes = Super.objects.filter(super_type_id=1)

                    heroes_serializer = SuperSerializer(heroes, many=True)

                    super_type_dictionary[super_type.type] = {
                        "Heroes": heroes_serializer.data,
                    }           
                
                else:
                    villians = Super.objects.filter(super_type_id=2)

                    villians_serializer = SuperSerializer(villians, many=True)

                    super_type_dictionary[super_type.type] = {
                        "Villians": villians_serializer.data,
                    }    
                
            return Response(super_type_dictionary)

        serializer = SuperSerializer(queryset, many=True)    
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# you are close, try getting all of the heroes together, pass them through the serializer and then display them in the custom dict. 
# Try making those changes and see how that displays. After that you could do the same steps for villains!

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#custmom ditionary display all hreoes/billians: "heroes":hero_serializer.data, then "villains":villain_serializer.data


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):

    super = get_object_or_404(Super, pk=pk)

    if request.method == 'GET':
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


