from django.contrib import admin
from django.urls import path, include
from core.views import HomeView, WelcomeAPIView, PostListView
from core.views import RankedProductsView, ProductListCreate, ProductRetrieveUpdateDestroy
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# JWT
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from core.views import ManagerOnlyView
from core.views import TestWelcomeEmailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', WelcomeAPIView.as_view()),
    path('blog/', PostListView.as_view()),
    path('ranked-products/', RankedProductsView.as_view(), name='ranked-products'),
    path('api-auth/', include('rest_framework.urls')),

    # DRF Product API
    path('products/', ProductListCreate.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),

    # drf-spectacular schema and docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('manager-only/', ManagerOnlyView.as_view(), name='manager-only'),


    path("test-email/", TestWelcomeEmailView.as_view()),


]
