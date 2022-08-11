from django.shortcuts import render
from userpost.models import UserPost
from userpost.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication



class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]
    queryset=UserPost.objects.all()
    serializer_class=UserSerializer

    filter_backends=[SearchFilter]
    search_fields=('title',)
    #어떤 칼럼을 기반으로 검색을 할건지->튜플



    def get_queryset(self):
        authentication_classes=[TokenAuthentication,SessionAuthentication]
        qs=super().get_queryset()
        if self.request.user.is_authenticated:
            
            #qs=qs.filter(author__id=1)
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        return qs

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
# Create your views here.
