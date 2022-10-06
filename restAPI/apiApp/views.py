from django.shortcuts import render
from .models import Family
from .serializers import FamilySerializer, FamilySerializerAll
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class FamilyView(APIView):
    
    def get(self,request,id=None):
        
        if(id==None):
            family_members = Family.objects.all()
            family_serializer = FamilySerializerAll(family_members, many=True).data

            if len(family_serializer)>0:
                #return Response({'message':'sucess','items':family_serializer})
                return render(request, 'index.html', {'message':'Exito!','items':family_serializer})
            
            else:
                #return Response({'message':'Empty list'})
                return render(request, 'index.html', {'message':'Lista vacia','items':family_serializer})

        else:
            family_member = Family.objects.filter(id = id).first()
            family_serializer = FamilySerializer(family_member).data

            if len(family_serializer)>0:
                return Response({'message':'sucess!!!!!','item':family_serializer})
            
            else:
                return Response({'message':'Empty list'})

    def post(self,request):
        print(request.data)
        family_serializer = FamilySerializer(data = request.data)

        if family_serializer.is_valid():
            family_serializer.save()
            return Response({'message':'Family memeber added'})
        else:
            return Response(family_serializer.errors)

    def put(self,request,id):

        family_member = Family.objects.filter(id = id).first()
        family_serializer = FamilySerializer(family_member, data = request.data, partial=True)

        if family_serializer.is_valid():
            family_serializer.save()
            return Response({'message':'Family member modified'})
        else:
            return Response(family_serializer.errors)

    def delete(self,request,id):
        family_member = Family.objects.filter(id = id).first()
        family_member.delete()
        
        return Response({'message':'Family member deleted!'})
