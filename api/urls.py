from django.urls import path
from .views import PostViewSetAPIView  #PostListView, PostDetailAPIView #PostCreateAPIView
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)
from rest_framework.routers import SimpleRouter
app_name = "api"
urlpatterns = [
    # path("<int:pk>/", PostDetailAPIView.as_view(), name="detail"),
    # path('', PostListView.as_view(), name="list"),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh")

    # path("create/", PostCreateAPIView.as_view(), name="create")
]
router = SimpleRouter()
router.register("", PostViewSetAPIView, basename='post')
urlpatterns += router.urls