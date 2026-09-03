from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [path('api/', include('apps.users.urls')), path('api/token/', TokenObtainPairView.as_view()), path('api/token/refresh/', TokenRefreshView.as_view()), path('api/auth/refresh/', TokenRefreshView.as_view())]
