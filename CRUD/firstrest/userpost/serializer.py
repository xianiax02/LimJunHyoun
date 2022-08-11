
from .models import UserPost
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    
    author_name=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=UserPost
        fields=['title','body','pk','author_name']

