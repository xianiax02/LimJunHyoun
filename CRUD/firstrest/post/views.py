from django.shortcuts import render
from .models import post
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class Mypagination(PageNumberPagination):
    page_size=5


#CBV
class PostViewSet(viewsets.ModelViewSet):
    queryset=post.objects.all().order_by('id')
    serializer_class=PostSerializer
    pagination_class=Mypagination

# Create your views here.
#페이지네이션을 할 때에는 레코드를 정렬한 상태에서 수행해야한다.


