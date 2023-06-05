from django.shortcuts import render
from api.serializers import  PostSerializer
from app.models import Post
from rest_framework.views import  APIView, Response
from rest_framework import generics, viewsets
from .permissions import IsAuthorForEdit
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class PostViewSetAPIView(viewsets.ModelViewSet):# all in one
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorForEdit
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'title', 'body']

# class PostListView(APIView):
#
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
# class PostListView(generics.ListCreateAPIView): #Yoki ListCreateView ni ishlatishni o'rniga CreateAPIView ishlatsa ham bo'ladi  va pastdagi comment ni ochib qo'yish shart Aks Holda Api Create qila olmay qolinadi
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView ): # 3tasi 1da Pastdagilar
#     permission_classes = [IsAuthorForEdit]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
