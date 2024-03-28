from django.contrib import admin
from django.urls import path, include
from darabala import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('',views.index,name = 'index'),
    path("darabala/", include("darabala.urls", namespace="darabala")),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("api/token/verify", TokenVerifyView.as_view()),
]
