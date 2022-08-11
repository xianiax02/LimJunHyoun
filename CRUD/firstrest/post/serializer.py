from .models import post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=post
        fields='__all__'
        #fields=['title','body']
        read_only_fields=('title','id')#혼자 있으면 (00,)식으로 써줘야 튜플로 인식
        #write only  

