from django.shortcuts import render
from .models import Essay
#from .serializers import EssaySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset=Essay.objects.all()
   #serializer_class=EssaySerializer
# Create your views here.
