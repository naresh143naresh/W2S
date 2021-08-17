from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from .models import Postion,company
from .serializers import postionSerializer, companySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.generic import View

class postionView(viewsets.ModelViewSet):
    def get(self,request,*args,**kwargs):
        return render(request='index.html')
    queryset = Postion.objects.all()
    serializer_class = postionSerializer


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        skillsrate = [0,1,2,3,4,5,6,7
        ]
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data = {
            "skillsrate": skillsrate,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
        }
    return Response(content)
class companyView(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializer
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exa_view(request, format=None):
    content = {
        'status': 'request was permitted'
        }
    return Response(content)






