from django.contrib import admin
from django.urls import path, include
from darabala import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('',views.index,name = 'index'),
    path("darabala/", include("darabala.urls", namespace="darabala")),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh", TokenRefreshView.as_view()),
    path("api/token/verify", TokenVerifyView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
