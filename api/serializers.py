from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.models import Post
from django.contrib.auth.models import User



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['username'] = user.username
        token['email'] = user.email
        token['password'] = user.password


        return token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class PostSerializer(ModelSerializer):
    # author = UserSerializer()

    class Meta:
        model = Post
        fields= ['id', 'author', 'title', 'body', 'creates', 'updates']
